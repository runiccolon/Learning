import threading
from multiprocessing import Pool
import asyncio
import time
import requests
import aiohttp
import time


async def spider(tid):
    url = f'https://tieba.baidu.com/p/{tid}'
    async with aiohttp.ClientSession() as session:
        for i in range(100):
            async with session.get(url) as res:
                await res.text()
                # print(await res.text())


# res = requests.get(url).text
# print(res)


async def get():
    start_time = time.time()
    tid_list = [6922860745, 6921532674, 6921266765]
    futures = [spider(tid) for tid in tid_list]
    await asyncio.gather(*futures)
    end_time = time.time()
    exec_time = end_time - start_time
    print(exec_time)


def common_get():
    start_time = time.time()
    tid_list = [6922860745, 6921532674, 6921266765]
    for tid in tid_list:
        url = f'https://tieba.baidu.com/p/{tid}'
        res = requests.get(url).content
        print(res)
    end_time = time.time()
    print(end_time - start_time)


def thread_main():
    start_time = time.time()
    tid_list = [6922860745, 6921532674, 6921266765]
    thread_list = []
    for i in range(1000):
        thread = threading.Thread(target=thread_get, args=(i,))
        thread_list.append(thread)
    for j in thread_list:
        j.setDaemon(True)
        j.start()
    for k in thread_list:
        k.join()
    end_time = time.time()
    print(end_time - start_time)


def thread_get(tid):
    url = f'https://www.baidu.com'
    res = requests.get(url).text
    print(res)


def multiprocessing_and_thread_main():
    start_time = time.time()
    p = Pool(4)  # 进程数量限制
    for i in range(4):
        p.apply_async(thread_main, args=())
    p.close()
    p.join()
    end_time = time.time()
    exec_time = end_time - start_time
    print(exec_time)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(get())
    # common_get()
    thread_main()
    # multiprocessing_and_thread_main()
