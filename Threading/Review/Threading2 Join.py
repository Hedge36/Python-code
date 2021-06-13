import threading
import time


def thread_job():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish\n")


def T2_job():
    print("T2 start")
    print('T2 finish')


def main():
    added_thread = threading.Thread(target=thread_job, name='T1')
    thread2 = threading.Thread(target=T2_job, name='T2')
    added_thread.start()    # 运行线程
    thread2.start()
    added_thread.join()     # 所有线程等待added_thread线程完成
    thread2.join()
    print('all done\n')


if __name__ == '__main__':
    main()

'''
运行结果分析：
T1 start
T2 start
T2 finish
T1 finish
all done
等待线程1，线程2完成后方进行下一个步骤，因而最后打印 "all done"。
'''
