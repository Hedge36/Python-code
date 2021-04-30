import numpy as np
from math import*
from matplotlib import pyplot as plt
#lambda函数
func=lambda x:(exp(x)-exp(-x))/x**2
x=np.linspace(-10,0)#定义域
y=[func(x[i]) for i in range(len(x))]
f = plt.figure(figsize=(6,4))
plt.plot(x,y)
plt.savefig('D:/Study/Python/作业源代码/work.png')
plt.show()
'''
#自定义函数
x=np.linspace(-10,10)#定义域
def y(x):
    y=(exp(x)-exp(-x))/x**2
    return y
y=[y(x[i]) for i in range(len(x))]
f = plt.figure(figsize=(6,4))
plt.plot(x,y)
plt.savefig('D:/Study/Python/作业源代码/work.png')
plt.show()
'''



