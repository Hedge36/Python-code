#PythonWorkT8         程序流程设计作业
'''问题分析：
一本书的页码为1、2、3、4、…，她的中间一页被撕掉了，余下
的各页码之和正好是300549，请问该书总页数是____，被撕掉的
是第__页。
'''
left=0                          #剩余总面数
n=0                             #总面数
while left!=300549:
    n+=1;sum_=(n+1)*n/2;i=1
    while i<n:                  #记录答案
        if left==300549:
            break
        else:
            if i%2==0:          #奇偶判断
                left=sum_+1-2*i
            else:
                left=sum_-1-2*i
        i+=1
print("该书的总页数为{}页，撕下的页数为{}页。".format(n%2+n//2,i//2+i%2))

        
    
