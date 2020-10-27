"""
通过 socketserver 模块完成网络并发
"""

from socketserver import *


# 创建tcp多进程并发
class Server(ForkingMixIn, TCPServer):
    pass


# 具体请求处理类
class Handler(StreamRequestHandler):
    # 重写方法
    def handle(self):
        print("Connect from", self.client_address)
        while True:
            data = self.request.recv(1024)
            # self.request ==>  accept-> connfd
            if not data:
                break
            print(data.decode())
            self.request.send(b"ok")

    def finish(self):
        pass


# 创建服务器对象
serv = Server(("0.0.0.0", 8888), Handler)
serv.serve_forever()  # 启动服务