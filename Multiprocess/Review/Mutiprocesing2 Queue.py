import multiprocessing as mp
import threading as td


def job1(q):
    rs = 0
    for i in range(100):
        rs += i + i ** 2 + i ** 3
    # rs作为公共资源
    q.put(rs)
    # queue


if __name__ == "__main__":
    q = mp.Queue()
    p1 = mp.Process(target=job1, args=(q,))
    p2 = mp.Process(target=job1, args=(q,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    rs1 = q.get()
    rs2 = q.get()
    print(rs1, rs2)
