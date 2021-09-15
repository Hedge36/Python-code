# threading

我们进行程序开发的时候，肯定避免不了要处理**并发**的情况。（并发不是并行）

一般并发的手段有采用多进程和多线程。

但线程比进程更轻量化，系统开销一般也更低，所以大家更倾向于用多线程的方式处理并发的情况。

Python 提供多线程编程的方式。

本文基于 Python3 讲解,Python 实现多线程编程需要借助于 threading 模块。

所以，我们要在代码中引用它。

```python
import threading
```

threading 模块中最核心的内容是 **Thread** 这个类。

我们要创建 Thread 对象,然后让它们运行，每个 Thread 对象代表一个线程，在每个线程中我们可以让程序处理不同的任务，这就是多线程编程。

**值得注意的是，程序运行时默认就是在主线程上**

创建 Thread 对象有 2 种手段。

1. 直接创建 Thread ，将一个 callable 对象从类的构造器传递进去，这个 callable 就是回调函数，用来处理任务。
2. 编写一个自定义类继承 Thread，然后复写 run() 方法，在 run() 方法中编写任务处理代码，然后创建这个 Thread 的子类。

## 1. 直接创建 Thread 对象

```python
class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
```

Thread 的构造方法中，最重要的参数是 **target**，所以我们需要将一个 callable 对象赋值给它，线程才能正常运行。

如果要让一个 Thread 对象启动，调用它的 start() 方法就好了。

下面是代码示例。

```python
import threading
import time
def test():
    for i in range(5):
        print('test ',i)
        time.sleep(1)
thread = threading.Thread(target=test)
thread.start()
for i in range(5):
    print('main ', i)
    time.sleep(1)
```

上面代码很简单，在主线程上打印 5 次，在一个子线程上打印 5 次。

运行结果如下：

```
test  0
main  0
main  1
test  1
main  2
test  2
main  3
test  3
main  4
test  4
```

上面的 callable 没有参数，如果需要传递参数的话，args 是固定参数，kwargs 是可变参数。

### Thread 的名字

每一个 Thread 都有一个 name 的属性，代表的就是线程的名字，这个可以在构造方法中赋值。

如果在构造方法中没有个 name 赋值的话，默认就是 “Thread-N” 的形式，N 是数字。

```python
import threading
import time

def test():
    for i in range(5):
        print(threading.current_thread().name+' test ',i)
        time.sleep(1)

thread = threading.Thread(target=test)
thread.start()

for i in range(5):
    print(threading.current_thread().name+' main ', i)
    time.sleep(1)
```

通过 thread.current_thread() 方法可以返回线程本身，然后就可以访问它的 name 属性。

上面代码运行结果如下：

```
Thread-1 test  0
MainThread main  0
Thread-1 test  1
MainThread main  1
Thread-1 test  2
MainThread main  2
Thread-1 test  3
MainThread main  3
Thread-1 test  4
MainThread main  4
```

如果我们在 Thread 对象创建时，构造方法里面赋值。

```python
thread = threading.Thread(target=test,name='TestThread')
```

那么，运行结果会变成这个样子。

```
TestThread test  0
MainThread main  0
MainThread main  1
TestThread test  1
MainThread main  2
TestThread test  2
MainThread main  3
TestThread test  3
MainThread main  4
TestThread test  4
```

### Thread 的生命周期

1. 创建对象时，代表 Thread 内部被初始化。
2. 调用 start() 方法后，thread 会开始运行。
3. thread 代码正常运行结束或者是遇到异常，线程会终止。

可以通过 Thread 的 is_alive() 方法查询线程是否还在运行。

值得注意的是，is_alive() 返回 True 的情况是 Thread 对象被正常初始化，start() 方法被调用，然后线程的代码还在正常运行。

```python
import threading
import time

def test():

    for i in range(5):
        print(threading.current_thread().name+' test ',i)
        time.sleep(0.5)


thread = threading.Thread(target=test,name='TestThread')
# thread = threading.Thread(target=test)
thread.start()

for i in range(5):
    print(threading.current_thread().name+' main ', i)
    print(thread.name+' is alive ', thread.isAlive())
    time.sleep(1)
123456789101112131415161718
```

在上面的代码中，我让 TestThread 比 MainThread 早一点结束，代码运行结果如下。

```
TestThread test  0
MainThread main  0
TestThread is alive  True
TestThread test  1
MainThread main  1
TestThread is alive  True
TestThread test  2
TestThread test  3
MainThread main  2
TestThread is alive  True
TestThread test  4
MainThread main  3
TestThread is alive  False
MainThread main  4
TestThread is alive  False
123456789101112131415
```

我们可以看到，主线程通过调用 TestThread 的 isAlive() 方法，准确查询到了它的存货状态。

### join() 提供线程阻塞手段。

上面代码两个线程是同时运行的，但如果让一个先运行，一个后运行，怎么做呢？

**调用一个 Thread 的 join() 方法，可以阻塞自身所在的线程。**

```python
import threading
import time

def test():

    for i in range(5):
        print(threading.current_thread().name+' test ',i)
        time.sleep(0.5)


thread = threading.Thread(target=test,name='TestThread')
thread.start()
thread.join()

for i in range(5):
    print(threading.current_thread().name+' main ', i)
    print(thread.name+' is alive ', thread.isAlive())
    time.sleep(1)
123456789101112131415161718
```

主线程创建了 TestThread 对象后，让其 start，然后通过调用 join() 方法，实现等待。程序运行结果如下：

```
TestThread test  0
TestThread test  1
TestThread test  2
TestThread test  3
TestThread test  4
MainThread main  0
TestThread is alive  False
MainThread main  1
TestThread is alive  False
MainThread main  2
TestThread is alive  False
MainThread main  3
TestThread is alive  False
MainThread main  4
TestThread is alive  False
123456789101112131415
```

默认的情况是，join() 会一直等待对应线程的结束，但可以通过参数赋值，等待规定的时间就好了。

```python
def join(self, timeout=None):
1
```

timeout 是一个浮点参数，单位是秒。

如果我们更改上面的代码。

```python
thread.join(1.0)
1
```

它的结果会是这样。

```
TestThread test  0
TestThread test  1
MainThread main  0
TestThread is alive  True
TestThread test  2
TestThread test  3
MainThread main  1
TestThread is alive  True
TestThread test  4
MainThread main  2
TestThread is alive  False
MainThread main  3
TestThread is alive  False
MainThread main  4
TestThread is alive  False
123456789101112131415
```

主线程只等待了 1 秒钟。

### Thread 中的 daemon 属性

有同学可能会注意到，Thread 的构造方法中有一个 daemon 参数。默认是 None。

那么，daemon 起什么作用呢？

我们先看一段示例代码。

```python
import threading
import time

def test():

    for i in range(5):
        print(threading.current_thread().name+' test ',i)
        time.sleep(2)


thread = threading.Thread(target=test,name='TestThread')
# thread = threading.Thread(target=test,name='TestThread',daemon=True)
thread.start()


for i in range(5):
    print(threading.current_thread().name+' main ', i)
    print(thread.name+' is alive ', thread.isAlive())
    time.sleep(1)
12345678910111213141516171819
```

我们让主线程执行代码的时长比 TestThread 要短。

程序运行结果如下。

```
TestThread test  0
MainThread main  0
TestThread is alive  True
MainThread main  1
TestThread is alive  True
TestThread test  1
MainThread main  2
TestThread is alive  True
MainThread main  3
TestThread is alive  True
TestThread test  2
MainThread main  4
TestThread is alive  True
TestThread test  3
TestThread test  4
123456789101112131415
```

MainThread 没有代码运行的时候，TestThread 还在运行。

这是因为 MainThread 在等待其他线程的结束。

TestThread 中 daemon 属性默认是 False，这使得 MainThread 需要等待它的结束，自身才结束。

**如果要达到，MainThread 结束，子线程也立马结束，怎么做呢？**

其实很简单，只需要在子线程调用 start() 方法之前设置 daemon 就好了。

当然也可以在子线程的构造器中传递 daemon 的值为 True。

```python
thread = threading.Thread(target=test,name='TestThread',daemon=True)
# thread.setDaemon(True)
12
```

更改前面代码示例，运行结果如下

```
TestThread test  0
MainThread main  0
TestThread is alive  True
MainThread main  1
TestThread is alive  True
TestThread test  1
MainThread main  2
TestThread is alive  True
MainThread main  3
TestThread is alive  True
TestThread test  2
MainThread main  4
TestThread is alive  True
12345678910111213
```

可以看到 MainThread 结束了 TestThread 也结束了。

## 2.自定义类继承 Thread

前面讲过，直接初始化一个 Thread，然后，现在还有一种方式就是自定义一个 Thread 的子类，然后复写它的 run() 方法。

```python
import threading
import time

class TestThread(threading.Thread):

    def __init__(self,name=None):
        threading.Thread.__init__(self,name=name)

    def run(self):
        for i in range(5):
            print(threading.current_thread().name + ' test ', i)
            time.sleep(1)


thread = TestThread(name='TestThread')
thread.start()
for i in range(5):
    print(threading.current_thread().name+' main ', i)
    print(thread.name+' is alive ', thread.isAlive())
    time.sleep(1)
1234567891011121314151617181920212223
```

上面的代码，我们自定义了 TestThread 这个类，然后继承了 threading.Thread。

只有在 run() 方法中处理逻辑。最终代码运行结果如下：

```
TestThread test  0
MainThread main  0
TestThread is alive  True
TestThread test  1
MainThread main  1
TestThread is alive  True
TestThread test  2
MainThread main  2
TestThread is alive  True
MainThread main  3
TestThread is alive  True
TestThread test  3
MainThread main  4
TestThread test  4
TestThread is alive  True
123456789101112131415
```

这与之前的效果并无差异，但我还是推荐用这种方法，毕竟面向对象编程嘛。

自此，Python 多线程编码技术就大致介绍完毕，大家可以进行实际代码编写了。

但是，多线程编程的难点在于多个线程之间共享数据的同步，这是非常容易出错的地方，我将分别编写相应的博文去介绍一些高级的技术点。



# Queue

## 1、队列（Queue）

Python的Queue模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列PriorityQueue。这些队列都实现了锁原语，能够在多线程中直接使用。可以使用队列来实现线程间的同步。

常用方法：

- Queue.qsize() 返回队列的大小
- Queue.empty() 如果队列为空，返回True,反之False
- Queue.full() 如果队列满了，返回True,反之False，Queue.full 与 maxsize 大小对应
- Queue.get([block[, timeout]])获取队列，timeout等待时间
- Queue.get_nowait() 相当于Queue.get(False)，非阻塞方法
- Queue.put(item) 写入队列，timeout等待时间
- Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号。每个get()调用得到一个任务，接下来task_done()调用告诉队列该任务已经处理完毕。
- Queue.join() 实际上意味着等到队列为空，再执行别的操作

示例代码如下：

```python
from Queue import Queue,LifoQueue,PriorityQueue
#先进先出队列
q=Queue(maxsize=5)
#后进先出队列
lq=LifoQueue(maxsize=6)
#优先级队列
pq=PriorityQueue(maxsize=5)
for i in range(5):
    q.put(i)
    lq.put(i)
    pq.put(i)
print "先进先出队列：%s;是否为空：%s；多大,%s;是否满,%s" %(q.queue,q.empty(),q.qsize(),q.full())
print "后进先出队列：%s;是否为空：%s;多大,%s;是否满,%s" %(lq.queue,lq.empty(),lq.qsize(),lq.full())
print "优先级队列：%s;是否为空：%s,多大,%s;是否满,%s" %(pq.queue,pq.empty(),pq.qsize(),pq.full())
print q.get(),lq.get(),pq.get()
print "先进先出队列：%s;是否为空：%s；多大,%s;是否满,%s" %(q.queue,q.empty(),q.qsize(),q.full())
print "后进先出队列：%s;是否为空：%s;多大,%s;是否满,%s" %(lq.queue,lq.empty(),lq.qsize(),lq.full())
print "优先级队列：%s;是否为空：%s,多大,%s;是否满,%s" %(pq.queue,pq.empty(),pq.qsize(),pq.full())
先进先出队列：deque([0, 1, 2, 3, 4]);是否为空：False；多大,5;是否满,True
后进先出队列：[0, 1, 2, 3, 4];是否为空：False;多大,5;是否满,False
优先级队列：[0, 1, 2, 3, 4];是否为空：False,多大,5;是否满,True
0 4 0
先进先出队列：deque([1, 2, 3, 4]);是否为空：False；多大,4;是否满,False
后进先出队列：[0, 1, 2, 3];是否为空：False;多大,4;是否满,False
优先级队列：[1, 3, 2, 4];是否为空：False,多大,4;是否满,False
```

 还有一种队列是双边队列，示例代码如下：

```python
from Queue import deque
dq=deque(['a','b'])
dq.append('c')
print(dq)
print(dq.pop())
print(dq)
print (dq.popleft())
print(dq)
dq.appendleft('d')
print(dq)
print(len(dq))
```

Output:

```python
deque(['a', 'b', 'c'])
c
deque(['a', 'b'])
a
deque(['b'])
deque(['d', 'b'])
2
```

##  2、生产者消费者模式

生产者消费者模式并不是[GOF](https://baike.baidu.com/item/GoF/6406151?fr=aladdin)提出的众多模式之一，但它依然是开发同学编程过程中最常用的一种模式

![img](https://img-blog.csdnimg.cn/20190410143333666.jpg)

生产者模块儿负责产生数据，放入缓冲区，这些数据由另一个消费者模块儿来从缓冲区取出并进行消费者相应的处理。该模式的优点在于：

- **解耦**：缓冲区的存在可以让生产者和消费者降低互相之间的依赖性，一个模块代码变化，不会直接影响另一个模块。
- **并发**：由于缓冲区，生产者和消费者不是直接调用，而是两个独立的并发主体，生产者产生数据之后把它放入缓冲区，就继续生产数据，不依赖消费者的处理速度。

## 3、采用生产者消费者模式开发的Python多线程

在Python中，队列是最常用的线程间的通信方法，因为它是线程安全的，自带锁。而Condition等需要额外加锁的代码操作，在编程对死锁现象要很小心，Queue就不用担心这个问题。

Queue多线程代码示例如下：

```python
from Queue import Queue
import time,threading

q=Queue(maxsize=0)
def product(name):
    count=1
    while True:
        q.put('气球兵{}'.format(count))
        print ('{}训练气球兵{}只'.format(name,count))
        count+=1
        time.sleep(5)
        
        
def consume(name):
    while True:
        print ('{}使用了{}'.format(name,q.get()))
        time.sleep(1)
        q.task_done()
        
        
t1=threading.Thread(target=product,args=('wpp',))
t2=threading.Thread(target=consume,args=('ypp',))
t3=threading.Thread(target=consume,args=('others',))
t1.start()
t2.start()
t3.start()
```

网上还有很多非常好的生产者消费者模式的Queue代码例子，开发同学需要根据具体的实际需求去设计实际模式