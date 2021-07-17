# 代码优化原则

## 1. 局部变量原则

优先使用局部变量，减少全局变量的使用，可以加快程序，大概每个变量可以节省0.005s左右。

**Tip :** 

> When you use a number, you can store it in a var first. Data like int 3 is a global var, we can firstly define a var like a, make a equal 3, then call a instead of 3 can run faster.

for example : 

```python
# Method 1
for i in range(1000000):
  print("lower")
  
# Method 2
a = 1000000
for i in range(a):
  print("Faster")
```



## 2. 精准调用

在导入库时，尽量精准导入函数，而不是导入整个库，这样可以节省一定的内存。

此外，在调用库函数时，一定要注意，部分占内存的函数，不要出现在循环结构中，比如：`plt.plt()` , 应当处理好所有数据再一次画完，而不是每次画一个点。



## 3. 数据处理

涉及大量数据处理时，优先使用 `numpy` 库的 `ndarray` ，其次`array`，以加快运行速度。

