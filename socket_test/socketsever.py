import logging
import sys
import socketserver
import socket
import threading

logging.basicConfig(format="%(asctime)s %(thread)d %(threadName)s %(message)s", stream=sys.stdout, level=logging.INFO)
log = logging.getLogger()


class Handler(socketserver.BaseRequestHandler):
    lock = threading.Lock()
    clients = {}

    def setup(self):
        super().setup()
        self.event = threading.Event()
        with self.lock:
            self.clients[self.client_address] = self.request
        log.info("新加入了一个连接{}".format(self.client_address))

    def handle(self):
        super().handle()
        sock: socket.socket = self.request
        while not self.event.is_set():
            try:
                data = sock.recv(1024)
            except Exception as e:
                log.error(e)
                data = b""
            log.info(data)
            if data == b"by" or data == b"":
                break
            msg = "service:{}-->{}".format(self.client_address, data).encode()
            expc = []  # 记录sock出错时对应的clients
            with self.lock:
                for c, sk in self.clients.items():
                    try:
                        sk.send(msg)  # 可能在发送消息是就出错
                    except:
                        expc.append(c)
                for c in expc:
                    self.clients.pop(c)

    def finish(self):
        super().finish()
        self.event.set()
        with self.lock:
            if self.client_address in self.clients:
                self.clients.pop(self.client_address)
        self.request.close()
        log.info("{}退出了".format(self.client_address))


if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(("0.0.0.0", 3999), Handler)
    server.daemon_threads = True  # 设置所有创建的线程都为Daemo线程
    threading.Thread(target=server.serve_forever, name="server", daemon=True).start()
    while True:
        cmd = input(">>>")
        if cmd.strip() == "quit":
            server.shutdown()  # 告诉serve_forever循环停止。
            server.server_close()
            break
        logging.info(threading.enumerate())
