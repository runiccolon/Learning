import multiprocessing  # 导入进程包
import os, time  # 这两个包的作用皆为更好的体现出我们的进程
import threading
import requests


def do(i):
    print("workor id :%s" % i)

    # 获取threading对象的标识ident
    print(threading.currentThread().name)

    print(threading.currentThread().ident)

    d = requests.get("http://www.google.com")
    # time.sleep(100)
    return


def main():
    thread_list = []
    thread_num = 3
    for i in range(thread_num):
        thread_list.append(threading.Thread(target=do, args=(i,)))
    for m in thread_list:
        m.start()
    os.system("ps -p" + str(os.getpid()))
    for n in thread_list:
        n.join()


if __name__ == '__main__':
    pool = multiprocessing.Pool(3)  # 导入进程池，括号内为最大进程数
    for i in range(10):
        pool.apply_async(main)
    pool.close()
    pool.join()
    print('finish')

    # for i in range(10):     # 阻塞式
    #     pool.apply(copy, (i,))

    # main()
