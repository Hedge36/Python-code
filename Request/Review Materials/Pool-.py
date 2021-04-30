#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/3/3 17:02
# @Author : Hedge
# @File : Pool.py.py
# @Software: PyCharm
from multiprocessing.dummy import Pool
import time
start = time.time()

def job(target):
    print(target, "working\n")
    time.sleep(2)
    print(target, "finish")

target = [str(i) for i in range(3)]

pool =  Pool(3)

pool.map(job, target)

time = time.time() - start

print(time)