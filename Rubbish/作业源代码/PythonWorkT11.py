#PythonWorkT11
#插入排序法
def insert_sort(ls):
    N = len(ls)
    for i in range(1,N):
        # 插入数据，对插入区冒泡排序
        for j in range(i,0,-1):
            # 判断大小
            if ls[j]<ls[j-1]:
                # 交换
                a = ls[j]
                ls[j] = ls[j-1]
                ls[j-1] = a

#测试区
from numpy import*
a=random.permutation(arange(1,10+1))
b=random.permutation(arange(1,100+1))
for ls in [a,b]:
    print("排序前：\n%s"%ls)
    insert_sort(ls)
    print("排序后：\n%s"%ls)
