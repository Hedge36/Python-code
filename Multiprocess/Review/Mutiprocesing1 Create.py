import multiprocessing as mp
import threading as td


def job1(a):
    print("balabala")


if __name__ == "__main__":
    t1 = td.Thread(target=job1, args=(1,))
    p1 = mp.Process(target=job1, args=(1,))

    t1.start()
    p1.start()
    t1.join()
    p1.join()
