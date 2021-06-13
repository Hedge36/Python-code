import threading


def job1():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 1
        print('job1', A)
    lock.release()


def job2():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 10
        print('job2', A)
    lock.release()


if __name__ == '__main__':
    lock = threading.Lock()
    A = 0
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

"""
lock函数，锁定公共资源，防止双线程公共变量处理混乱。
上锁结果：
job1 1
job1 2
job1 3
job1 4
job1 5
job1 6
job1 7
job1 8
job1 9
job1 10
job2 20
job2 30
job2 40
job2 50
job2 60
job2 70
job2 80
job2 90
job2 100
job2 110
job1运行完毕后进行job2，question：那和单独各自运行有什么区别?

未上锁结果：
job1 1
job1 2
job2 12
job1 13
job2 23
job1 24
job2 34
job1 35
job2 45
job1 46
job2 56
job1 57
job1 68
job2 78
job1 79
job2 89
job1 90
job2 100
job2 110
job1与job2交叉进行
"""
