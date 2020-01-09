from time import time
# from threading import Thread
from multiprocessing import Process as Thread


def counter():
    i = 0

    for _ in range(10000000):
        i += 1


def main1():
    start = time()

    for _ in range(5):

        t = Thread(target=counter)

        t.start()
        t.join()

    print('单线程: ', time() - start)


def main2():
    start = time()

    t_list = []
    for _ in range(5):
        t = Thread(target=counter)

        t.start()
        t_list.append(t)

    for t in t_list:
        t.join()

    print('多线程并发:', time() - start)


if __name__ == '__main__':
    main1()
    main2()
