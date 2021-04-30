import multiprocessing as mp
import threading as td
import time


def job1(q):
    rs = 0
    for i in range(100):
        rs += i + i ** 2 + i ** 3
    # rs作为公共资源
    q.put(rs)
    # queue


def multipcore():
    q = mp.Queue()
    p1 = mp.Process(target=job1, args=(q,))
    p2 = mp.Process(target=job1, args=(q,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    rs1 = q.get()
    rs2 = q.get()
    print("process:", rs1, rs2)


def normal():
    rs = 0
    for _ in range(2):
        for i in range(100):
            rs += i + i ** 2 + i ** 3
    # rs作为公共资源
    print("normal:", rs)
    # queue


def multithread():
    q = mp.Queue()
    t1 = td.Thread(target=job1, args=(q,))
    t2 = td.Thread(target=job1, args=(q,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    rs1 = q.get()
    rs2 = q.get()
    print("threading:", rs1, rs2)


if __name__ == '__main__':
    st = time.time()
    normal()
    st1 = time.time()
    print("normal", st1-st)
    st2 = time.time()
    multithread()
    print("thread", st2-st1)
    st = time.time()
    multipcore()
    print("process", time.time()-st2)
