import threading
import time


def thread_job():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish\n")


def main():
    added_thread = threading.Thread(target=thread_job, name='T1')
    added_thread.start()    # 运行线程
    print('all done\n')


if __name__ == '__main__':
    main()

'''
结果呈现：
T1 start
all done
T1 finish
原因分析：
双线程同时进行，主线程运行分线程added_thread后直接运行print，而此时分线程
added_thread仍未运行完毕。
'''
