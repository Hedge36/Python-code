# Numpy

#### np.arange(start, end, size)

start, end can be float.

#### np.lispace

#### np.argmax

#### np.argmin

#### np.mgrid 

*nd_grid* instance which returns a dense multi-dimensional “meshgrid”.

An instance of `numpy.lib.index_tricks.nd_grid` which returns an dense (or fleshed out) mesh-grid when indexed, so that each returned argument has the same shape. The dimensions and number of the output arrays are equal to the number of indexing dimensions. If the step length is not a complex number, then the stop is not inclusive.

However, if the step length is a **complex number** (e.g. 5j), then the integer part of its magnitude is interpreted as specifying the number of points to create between the start and stop values, where the stop value **is inclusive**.

**Returns**

> mesh-grid *ndarrays* all of the same dimensions

**Examples**

```python
>>> np.mgrid[0:5,0:5]
array([[[0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4]],
       [[0, 1, 2, 3, 4],
        [0, 1, 2, 3, 4],
        [0, 1, 2, 3, 4],
        [0, 1, 2, 3, 4],
        [0, 1, 2, 3, 4]]])
>>> np.mgrid[-1:1:5j]
array([-1. , -0.5,  0. ,  0.5,  1. ])
```

### ndarray.flat

> A 1-D iterator over the array. 将数组转换为1-D的迭代器
> flat返回的是一个**迭代器**，可以用for访问数组每一个元素

```python
import numpy as np
a = np.arange(4).reshape(2,2)
print(a)
for i in a.flat:
    print(i)
#迭代器可以用list进行输出
print(list(a.flat))
print(type(a.flat))#返回类型为 numpy.flatiter
#可以用索引对迭代器进行引号
a.flat[3]12345678910
[[0 1]
 [2 3]]
0
1
2
3
[0, 1, 2, 3]
<class 'numpy.flatiter'>
3
123456789
```

**ndarray.flatten(order=’C’)**

> Return a copy of the array collapsed into one dimension.
> 将数组的**`副本`**转换为一个维度，并返回

**可选参数，order：{'C’,'F’,'A’,'K’}**

- 'C’：C-style，行序优先
- 'F’：Fortran-style，列序优先
- 'A’：if a is Fortran contiguous in memory ,flatten in column_major order
- 'K’：按照元素在内存出现的顺序进行排序
  默认为’C’

**举例如下:**

```python
a = np.array([[4,5],[4,9]])
#默认按行转换
b= a.flatten()
print(b)
#换成列来划分
c = a.flatten('F')
print(c)1234567
[4 5 4 9]
[4 4 5 9]
```

numpy中的ravel()、flatten()、squeeze()都有将多维数组转换为一维数组的功能，区别：

ravel()：如果没有必要，不会产生源数据的副本

flatten()：返回源数据的副本

squeeze()：只能对维数为1的维度降维



ogrid函数作为产生numpy数组与numpy的arange函数功能有点类似，不同的是：

1、arange函数产生的是一维数组，而ogrid函数产生的是二维数组

2、arange函数产生的是一个数组，而ogrid函数产生的是二个数组

3、ogrid函数产生的数组，第一个数组是以纵向产生的，即数组第二维的大小始终为1。第二个数组是以横向产生的，即数组第一维的大小始终为1。

下面详细介绍ogrid函数的两种用法：

1、整数步长
第一个数组的步长为1，第二数组的步长为2

    x,y = np.ogrid[0:10:1,0:10:2]
    print(x,np.shape(x))
    print(y,np.shape(y))


注意：不设置步长，默认为1。

2、复数步长
复数步长的设置是通过j进行设置的，如5j。复数前表示的是，用几个数值来等分整个区间。

    x,y = np.ogrid[0:10:6j,0:10:4j]
    print(x,np.shape(x))
    print(y,np.shape(y))



## numpy.random

1、numpy中有一些常用的用来产生随机数的函数，randn()和rand()就属于这其中。 

numpy.random.randn(d0, d1, …, dn)是从标准正态分布中返回一个或多个样本值。 

numpy.random.rand(d0, d1, …, dn)的随机样本位于[0, 1)中。 

代码：

```python
import numpy as np 
arr1 = np.random.randn(2,4)
print(arr1)
print('**************************')
arr2 = np.random.rand(2,4)
print(arr2)
```

在使用Python进行数据处理时，往往需要用到大量的随机数据，那如何构造这么多数据呢？Python的第三方库numpy库中提供了random函数来实现这个功能。 


2、首先说下**numpy.random.seed()与numpy.random.RandomState()**这两个在数据处理中比较常用的函数，两者实现的作用是一样的，都是使每次随机生成数一样，具体可见下图

![numpy.random.seed()](https://img-blog.csdn.net/20170803093330447?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbTBfMzgwNjE5Mjc=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

![random.RandomState()](https://img-blog.csdn.net/20170803094020163?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbTBfMzgwNjE5Mjc=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

**1.numpy.random.rand()** 

官方文档中给出的用法是：

```Python
numpy.random.rand(d0,d1,…dn) 
```

以给定的形状创建一个数组，并在数组中加入在[0,1]之间均匀分布的随机样本。 

**用法及实现**： 
![这里写图片描述](https://img-blog.csdn.net/20170719094221011?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbTBfMzgwNjE5Mjc=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

**2.numpy.random.randn()** 

官方文档中给出的用法是：

```python
numpy.random.rand(d0,d1,…dn) 
```

以给定的形状创建一个数组，数组元素来符合标准正态分布N(0,1) 

若要获得一般正态分则可用**sigma \* np.random.randn(…) + mu**进行表示 

**用法及实现**： 
![这里写图片描述](https://img-blog.csdn.net/20170719204112233?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbTBfMzgwNjE5Mjc=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

**3.numpy.random.randint()** 

官方文档中给出的用法是：

```python
numpy.random.randint(low,high=None,size=None,dtype) 
```

生成在半开半闭区间**[low,high)**上离散均匀分布的整数值;若**high=None**，则取值区间变为**[0,low)** 

**用法及实现** 

high=None的情形 
![这里写图片描述](https://img-blog.csdn.net/20170719205047270?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbTBfMzgwNjE5Mjc=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

high≠None 
![这里写图片描述](https://img-blog.csdn.net/20170719205416499?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbTBfMzgwNjE5Mjc=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

**4.numpy.random.random_integers()** 

官方文档中给出的用法是： 

```python
numpy.random.random_integers(low,high=None,size=None) 
```

生成闭区间**[low,high]**上离散均匀分布的整数值;若**high=None**，则取值区间变为**[1,low]** 
**用法及实现** 
high=None的情形 
![什么傻逼东西](https://img-blog.csdn.net/20170719210021131?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbTBfMzgwNjE5Mjc=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

high≠None的情形 
![这里写图片描述](https://img-blog.csdn.net/20170719210211915?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbTBfMzgwNjE5Mjc=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

此外，若要将【a,b】区间分成N等分，也可以用此函数实现 
**a+(b-a)\*(numpy.random.random_integers(N)-1)/(N-1)**

5.numpy.random_sanmple() 

官方文档中给出的用法是： 

```python
numpy.random.random_sample(size=None) 
```

以给定形状返回[0,1)之间的随机浮点数 

**用法及实现** 
![这里写图片描述](https://img-blog.csdn.net/20170719211839070?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbTBfMzgwNjE5Mjc=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

其他函数，**numpy.random.random()** **;numpy.random.ranf()** 
**numpy.random.sample()**用法及实现都与它相同

**6.numpy.random.choice()** 

官方文档中给出的用法： 

```python
numpy.random.choice(a,size=None,replace=True,p=None) 
```

若a为数组，则从a中选取元素；若a为单个int类型数，则选取range(a)中的数

replace是bool类型，为True，则选取的元素会出现重复；反之不会出现重复 
p为数组，里面存放选到每个数的可能性，即概率 。

**用法及实现** 
![这里写图片描述](https://img-blog.csdn.net/20170719213657298?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbTBfMzgwNjE5Mjc=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)



## random

在数据分析中，数据的获取是第一步，numpy.random 模块提供了非常全的自动产生数据API，是学习数据分析的第一步。 
总体来说，numpy.random模块分为四个部分，对应四种功能： 

1. 简单随机数： 产生简单的随机数据，可以是任何维度 
2. 排列：将所给对象随机排列 
3. 分布：产生指定分布的数据，如高斯分布等 
4. 生成器：种随机数种子，根据同一种子产生的随机数是相同的 

以下是详细内容以及代码实例：（以下代码默认已导入numpy： import numpy as np ）

------

### 1. 生成器

电脑产生随机数需要明白以下几点： 

1. 随机数是由随机种子根据一定的计算方法计算出来的数值。所以，只要计算方法一定，随机种子一定，那么产生的随机数就不会变。 
2. 只要用户不设置随机种子，那么在默认情况下随机种子来自系统时钟（即定时/计数器的值） 
3. 随机数产生的算法与系统有关，Windows和Linux是不同的，也就是说，即便是随机种子一样，不同系统产生的随机数也不一样。 

numpy.random 设置种子的方法有：

| 函数名称     | 函数功能     | 参数说明                                                |
| ------------ | ------------ | ------------------------------------------------------- |
| RandomState  | 定义种子类   | RandomState是一个种子类，提供了各种种子方法，最常用seed |
| seed([seed]) | 定义全局种子 | 参数为整数或者矩阵                                      |

代码示例：

```python
np.random.seed(1234) #设置随机种子为1234
```

------

### 2. 简单随机数

| 函数名称                          | 函数功能                | 参数说明                                                     |
| --------------------------------- | ----------------------- | ------------------------------------------------------------ |
| rand(d0, d1, …, dn)               | 产生均匀分布的随机数    | dn为第n维数据的维度                                          |
| randn(d0, d1, …, dn)              | 产生标准正态分布随机数  | dn为第n维数据的维度                                          |
| randint(low[, high, size, dtype]) | 产生随机整数            | low：最小值；high：最大值；size：数据个数                    |
| random_sample([size])             | 在[0,1）内产生随机数    | size：随机数的shape，可以为元祖或者列表，[2,3]表示2维随机数，维度为（2,3） |
| random([size])                    | 同random_sample([size]) | 同random_sample([size])                                      |
| ranf([size])                      | 同random_sample([size]) | 同random_sample([size])                                      |
| sample([size]))                   | 同random_sample([size]) | 同random_sample([size])                                      |
| choice(a[, size, replace, p])     | 从a中随机选择指定数据   | a：1维数组 size：返回数据形状                                |
| bytes(length)                     | 返回随机位              | length：位的长度                                             |

代码示例:

```python
(1) np.random.rand(2,3) #产生2行三列均匀分布随机数组
Out[7]: 
array([[ 0.35369993,  0.0086019 ,  0.52609906],
       [ 0.31978928,  0.27069309,  0.21930115]])

(2）In [8]: np.random.randn(3,3) #三行三列正态分布随机数据
Out[8]: 
array([[ 2.29864491,  0.52591291, -0.80812825],
       [ 0.37035029, -0.07191693, -0.76625886],
       [-1.264493  ,  1.12006474, -0.45698648]])
(3）In [9]: np.random.randint(1,100,[5,5]) #(1,100）以内的5行5列随机整数
Out[9]: 
array([[87, 69,  3, 86, 85],
       [13, 49, 59,  7, 31],
       [19, 96, 70, 10, 71],
       [91, 10, 52, 38, 49],
       [ 8, 21, 55, 96, 34]])
(4）In [10]: np.random.random(10) #(0,1）以内10个随机浮点数
Out[10]: 
array([ 0.33846136,  0.06517708,  0.41138166,  0.34638839,  0.41977818,
        0.37188863,  0.2508949 ,  0.89923638,  0.51341298,  0.71233872])
(5）In [11]: np.random.choice(10) #[0,10)内随机选择一个数
Out[11]: 7
```

------

### 3. 分布

numpy.random模块提供了产生各种分布随机数的API：

| 函数名称                                     | 函数功能                                                     |
| -------------------------------------------- | ------------------------------------------------------------ |
| beta(a, b[, size])                           | 贝塔分布样本，在 [0, 1]内。                                  |
| binomial(n, p[, size])                       | 二项分布的样本。                                             |
| chisquare(df[, size])                        | 卡方分布样本。                                               |
| dirichlet(alpha[, size])                     | 狄利克雷分布样本。                                           |
| exponential([scale, size])                   | 指数分布                                                     |
| f(dfnum, dfden[, size])                      | F分布样本。                                                  |
| gamma(shape[, scale, size])                  | 伽马分布                                                     |
| geometric(p[, size])                         | 几何分布                                                     |
| gumbel([loc, scale, size])                   | 耿贝尔分布。                                                 |
| hypergeometric(ngood, nbad, nsample[, size]) | 超几何分布样本。                                             |
| laplace([loc, scale, size])                  | 拉普拉斯或双指数分布样本                                     |
| logistic([loc, scale, size])                 | Logistic分布样本                                             |
| lognormal([mean, sigma, size])               | 对数正态分布                                                 |
| logseries(p[, size])                         | 对数级数分布。                                               |
| multinomial(n, pvals[, size])                | 多项分布                                                     |
| multivariate_normal(mean, cov[, size])       | 多元正态分布。                                               |
| negative_binomial(n, p[, size])              | 负二项分布                                                   |
| noncentral_chisquare(df, nonc[, size])       | 非中心卡方分布                                               |
| noncentral_f(dfnum, dfden, nonc[, size])     | 非中心F分布                                                  |
| normal([loc, scale, size])                   | 正态(高斯)分布                                               |
| pareto(a[, size])                            | 帕累托（Lomax）分布                                          |
| poisson([lam, size])                         | 泊松分布                                                     |
| power(a[, size])                             | Draws samples in [0, 1] from a power distribution with positive exponent a - 1. |
| rayleigh([scale, size])                      | Rayleigh 分布                                                |
| standard_cauchy([size])                      | 标准柯西分布                                                 |
| standard_exponential([size])                 | 标准的指数分布                                               |
| standard_gamma(shape[, size])                | 标准伽马分布                                                 |
| standard_normal([size])                      | 标准正态分布 (mean=0, stdev=1).                              |
| standard_t(df[, size])                       | Standard Student’s t distribution with df degrees of freedom. |
| triangular(left, mode, right[, size])        | 三角形分布                                                   |
| uniform([low, high, size])                   | 均匀分布                                                     |
| vonmises(mu, kappa[, size])                  | von Mises分布                                                |
| wald(mean, scale[, size])                    | 瓦尔德（逆高斯）分布                                         |
| weibull(a[, size])                           | Weibull 分布                                                 |
| zipf(a[, size])                              | 齐普夫分布                                                   |

代码示例:

```python
(1)正态分布
import numpy as np
import matplotlib.pyplot as plt

mu = 1  #期望为1
sigma = 3  #标准差为3
num = 10000  #个数为10000

rand_data = np.random.normal(mu, sigma, num)
count, bins, ignored = plt.hist(rand_data, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
         np.exp( - (bins - mu)**2 / (2 * sigma**2)), linewidth=2, color='r')
plt.show()
```

得到图像： 

![img](https://images2018.cnblogs.com/blog/1176635/201809/1176635-20180912112442496-461573591.png)

 

------

### 4. 排列

| 函数名称       | 函数功能                                   | 参数说明     |
| -------------- | ------------------------------------------ | ------------ |
| shuffle(x)     | 打乱对象x（多维矩阵按照第一维打乱）        | 矩阵或者列表 |
| permutation(x) | 打乱并返回该对象（多维矩阵按照第一维打乱） | 整数或者矩阵 |

代码示例:

```python
(1)正态分布
import numpy as np
rand_data = np.random.randint(1, 10, (3, 4))
print(rand_data)
np.random.shuffle(rand_data)
print(rand_data)

out：
[[4 4 4 8]
 [5 6 8 2]
 [1 7 6 6]]
[[4 4 4 8]
 [1 7 6 6]
 [5 6 8 2]]
#按照行打乱了，也就是交换了行
```



## np.where

```python
numpy.where(condition[, x, y])
```

Return elements chosen from *x* or *y* depending on *condition*.

**Note**

> When only *condition* is provided, this function is a shorthand for `np.asarray(condition).nonzero()`. Using [`nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero) directly should be preferred, as it behaves correctly for subclasses. The rest of this documentation covers only the case where all three arguments are provided.

**Parameters**

**condition**

array_like, boolWhere True, yield *x*, otherwise yield *y*.

**x, y**array_likeValues from which to choose. *x*, *y* and *condition* need to be broadcastable to some shape.

**Returns**

**out**

ndarray An array with elements from *x* where *condition* is True, and elements from *y* elsewhere.

For example：

```python
a = np.arange(10)
a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.where(a < 5, a, 10*a)
array([ 0,  1,  2,  3,  4, 50, 60, 70, 80, 90])
```



## Nan处理

### 删除所有的缺失值（NaN）

使用函数np.isnan（）来确定是否含有缺失值NaN，缺失值的位置的返回值为True。

```python
print(np.isnan(a))
```

通过使用取反运算符〜在此ndarray中将缺失值NaN的位置设置为False，可以删除缺失值（提取不缺失值的元素），但由于剩余元素的数量不同，因此可以删除原始数组ndarray的形状不会保留，而是被展平。

```python
print(~np.isnan(a))

print(a[~np.isnan(a)])
```



### 删除包含缺失值（NaN）的行

要删除包含缺失值NaN的行，可以使用any（）方法，如果NumPy数组行中有一个缺失值则整行返回True。
如果参axis= 1，则确定每一行是否有缺失值。

```python
print(np.isnan(a).any(axis=1))
```

使用取反运算符〜将没有缺失值的行设置为True。

```python
print(~np.isnan(a).any(axis=1))
```

删除包含缺失值的行。

```python
print(a[~np.isnan(a).any(axis=1), :])

print(a[~np.isnan(a).any(axis=1)])
```



### 删除包含缺失值（NaN）的列

删除包含缺失值NaN的列时也是如此。 如果在any（）中参数axis= 0，则确定每一列是否至少有一个True。使用取反运算符〜将没有任何缺失值的列设置为True。

```python
print(~np.isnan(a).any(axis=0))
```

删除包含缺失值的列。

```python
print(a[:, ~np.isnan(a).any(axis=0)])
```

如果只想删除缺少值的列，请使用all（）而不是any（）。

```python
a = np.genfromtxt('data/src/sample_nan.csv', delimiter=',')
a[2, 2] = np.nan
print(a)
print(a[:, ~np.isnan(a).any(axis=0)])
print(a[:, ~np.isnan(a).all(axis=0)])
```



# Pandas

##  Synopsis

pandas是一个强大的分析结构化数据的工具集；它的使用基础是Numpy（提供高性能的矩阵运算）；用于数据挖掘和数据分析，同时也提供数据清洗功能。

Pandas中常见的数据结构有两种：

| 数据类型    | 数据说明                                                     |
| ----------- | :----------------------------------------------------------- |
| Series      | 类似一维数组的对象，也即一维DataFrame                        |
| DateFrame   | 二维数组/表格数组；每列数据可以是不同的类型；索引包括列索引和行索引。 |
| Time-Series | 以时间为索引的Series                                         |
| Panel       | 三维数组                                                     |

**Series**

- 构建Series：`ser_obj = pd.Series(range(10))`
- 由索引和数据组成（索引在左<自动创建的>，数据在右）。
- 获取数据和索引：`ser_obj.index; ser_obj.values` （注意，当改变了索引后索引方式也需更改）
- 预览数据： `ser_obj.head(n);ser_obj.tail(n)`

**DateFrame**

- 获取列数据：`df_obj[col_idx]或df_obj.col_idx`
- 增加列数据：`df_obj[new_col_idx] = data`
- 删除列：`del df_obj[col_idx]`
- 按值排序：`sort_values(by = “label_name”)`

**常用方法**

| Count         | 非NA值得数量                           |
| ------------- | -------------------------------------- |
| describe      | 针对Series或各DataFrame列计算汇总统计  |
| min\max       | 计算最小值和最大值                     |
| argmin\argmax | 计算能够获取到最大值或最小值的索引位置 |
| idxmin\idxmax | 计算能够获取到最小值和最大值的索引值   |
| quantile      | 计算样本的分位数（0-1）                |
| sum           | 值得总和                               |
| mean          | 值得平均值                             |
| median        | 值的算术中位数（50%分位数）            |
| mad           | 根据平均值计算平均绝对离差             |
| var           | 样本值得方差                           |
| std           | 样本值得标准差                         |
| skew          | 样本值的偏度（三阶距）                 |
| kurt          | 样本值的峰度（四阶距）                 |
| cumsum        | 样本值的累计和                         |
| cummin\cummax | 样本值的累计最大值和累计最小值         |
| cumprod       | 样本值的累计积                         |
| diff          | 计算一阶差分（对时间序列很有用）       |
| pct_change    | 计算百分数变化                         |

**处理缺失数据**

- Dropna()丢弃缺失数据
- Fillna()填充缺失数据

**数据过滤**

Df[filter_condition]依据filter_condition(条件)对Df(数据)进行过滤。

**绘图功能**

```
Plot(kind, x, y, title, figsize)
```

保存图片：`plt.savefig()`

## 1. IO

| 格式类型  | 数据描述      | Reader         | Writer       |
| --------- | ------------- | -------------- | ------------ |
| text      | CSV           | read_ csv      | to_csv       |
| text      | JSON          | read_json      | to_json      |
| text      | HTML          | read_html      | to_html      |
| text      | clipboard     | read_clipboard | to_clipboard |
| binary    | Excel         | read_excel     | to_excel     |
| binary    | HDF5          | read_hdf       | to_hdf       |
| binary    | Feather       | read_feather   | to_feather   |
| binary    | Msgpack       | read_msgpack   | to_msgpack   |
| binary    | Stata         | read_stata     | to_stata     |
| binary    | SAS           | read_sas       | \            |
| binary    | Python Pickle | read_pickle    | to_pickle    |
| SQL       | SQL           | read_sql       | to_sql       |
| SQLGoogle | Big Query     | read_gbq       | to_gbq       |



### 1.1 读取CSV文件

```python
import pandas as pd
import os

file_path = os.path.join("test.csv")
data = pd.read_csv(open(file_path, 'r', encoding='utf-8'), sep='|')

#定义一个列表来获取name列中的内容
name_list = []
for column,  row in data.iterrows():
    name_list.append(row['name'])
    print(row['name'])
```

### 1.2 读取excel文件

**现版本pandas(xlrd)不支持xlsx格式，仅支持xls，如需打开，需退版本，xlsx可使用openpyxl打开。**

excel文件的读取都可以用以下函数来实现

> pd.read_excel( 
>
> io,  sheetname=0,   header=0,  skiprows=None,  index_col=None,  names=None,  arse_cols=None,  date_parser=None,  na_values=None,  thousands=None,  convert_float=True,  has_index_names=None,  converters=None,  dtype=None,  true_values=None,  false_values=None,  engine=None,   squeeze=False,  **kwds
>
> )

**参数详解：**

- `io`：excel文件路径；
- `sheetname`：默认是sheetname为0，返回多表使用sheetname=[0, 1]，若sheetname=None是返回全表 。注意：int/string返回的是dataframe，而none和list返回的是dict of dataframe。
- `header`：指定作为列名的行，默认0，即取第一行，数据为列名行以下的数据；若数据不含列名，则设定 header = None；
- `skiprows`：省略指定行数的数据，比如省略第三行，`skiprows=2`；
- `skip_footer`：省略从尾部数的行数据
- `index_col`：指定列为索引列；
- `names`：指定列的名字，传入一个list数据

### 1.3 读取txt文件

这里使用`read_table()`函数。

```python
import pandas as pd
data=pd.read_table('../data/datingTestSet2.txt', sep='\t', header=None)
data.head()
"""
输出：
0	1	2	3
0	40920	8.326976	0.953952	3
1	14488	7.153469	1.673904	2
2	26052	1.441871	0.805124	1
3	75136	13.147394	0.428964	1
4	38344	1.669788	0.134296	1
"""
```

**常用参数简介：**

- `filepath_or_buffer`：文件路径。
- `sep`：分隔符，默认为\t。
- `header`：用作列名的行号，默认为0（第一行），如果没有header行就应该设置为None。
- `names`：用于结果的列名列表，结合header=None。
- `skiprows`：跳过指定行。
- `na_values`：缺失值处理，`na_values= ["null"]`，用null字符替换缺失值。
- `nrows`：定需要读取的行数：`nrows = 100`， 指定读取前100行数据。

### 1.4 写CSV文件

```python
#任意的多组列表
a = [1, 2, 3]
b = [4, 5, 6]

#字典中的key值即为csv中的列名
data_dict = {'a_name':a, 'b_name':b}

#设置DataFrame中列的排列顺序
#如果无需重命名，columns这一参数可以省略
dataFrame = pd.DataFrame(data_dict,  columns=['a_name',  'b_name'])

#将DataFrame存储到csv文件中, index表示是否显示行名，default=True
dataFrame.to_csv("test.csv",  index=False,  sep='|')
#如果希望在不覆盖原文件内容的情况下将信息写入文件，可以加上mode="a"
dataFrame.to_csv("test.csv",  mode="a",  index=False, sep='|')
123456789101112131415
```

## 2. DataFrame

### 2.1 iter

遍历DataFrame数据。

```python
for index,  row in df.iterrows():
    print(row["column"])
```

### 2.2 concat

> pd.concat(objs,  axis=0,  join ='outer’,  join_axes=None,  ignore_index=False, keys=None,  levels=None,  names=None,  verify_integrity=False)

| 参数 | 可选项 | 参数说明|
| :-----------: | :------------------------------------: | ------------- |
| objs | \ | series，dataFrame或者是panel构成的序列list |
|axis |<u>0, </u> 1|需要合并链接的轴，0是行，1是列|
|join | <u>outer</u>,  inner | 连接方式 ，inner交集，outer并集并用nan填充 |
|join_axes | index | 以index轴作为合并后的表头 |
|ignore_index | <u>False</u>,   True | 忽略行表头并重置为默认序号 |

#### 2.2.1 相同字段的表首尾相接

```python
# 现将表构成list，然后在作为concat的输入
frames = [df1,  df2,  df3]
result = pd.concat(frames)
```

![img](https://img-blog.csdnimg.cn/20181126153414217.png)

#### 2.2.2 横向表拼接（行对齐）

##### 2.2.2.1 axis

当axis = 1的时候，concat就是行对齐，然后将不同列名称的两张表合并。

```pyhon
result = pd.concat([df1,  df4],  axis=1)
```

![img](https://img-blog.csdnimg.cn/20181126153930416.png)

##### 2.2.2.2 join

加上join参数的属性，如果为’inner’得到的是两表的交集，如果是outer，得到的是两表的并集。

```python
result = pd.concat([df1,  df4],  axis=1,  join='inner')
```

![img](https://img-blog.csdnimg.cn/20181126154119830.png)

##### 2.2.2.3 join_axes

如果有join_axes的参数传入，可以指定根据那个轴来对齐数据
例如根据df1表对齐数据，就会保留指定的df1表的轴，然后将df4的表与之拼接

```python
result = pd.concat([df1,  df4],  axis=1,  join_axes=[df1.index])
```

![img](https://img-blog.csdnimg.cn/20181207144453655.png)

### 2.3 merge

> merge (left ,  right,  how='inner',  on=None,  left_on=None,  right_on=None,  left_index=False,  right_index=False,  sort=False,  suffixes=('\_x',  '_y'),  copy=True,  indicator=False,  validate=None)

| 参数 |参数说明|
|----|----------|
| left |参与合并的左侧DataFrame|
|right |参与合并的右侧DataFrame|
|how |连接方式：**'inner'（默认）**；还有，'outer',  **'left',  'right'**|
|on |用于连接的列名，必须同时存在于左右两个DataFrame对象中，如果未指定，则以left和right列名的交集作为中轴|
|left_on |左侧DataFarme中用作连接键的列|
|right_on |右侧DataFarme中用作连接键的列|
|left_index |将左侧的行索引用作其连接键|
|right_index |将右侧的行索引用作其连接键|
|sort |根据连接键对合并后的数据进行排序，默认为True。有时在处理大数据集时，禁用该选项可获得更好的性能|
|suffixes |字符串值元组，用于追加到重叠列名的末尾，默认为（'\_x’, '_y’）.例如，左右两个DataFrame对象|
|copy |默认为False，可以在某些特殊情况下避免将数据复制到结果数据结构中。默认总是赋值。|
|indicator |参数为'True'时，显示合并具体情况|


**1.merge默认按相同字段合并，且取两个都有的。**

```python
df1 = pd.DataFrame({'name':['kate', 'herz', 'catherine', 'sally'], 
									'age':[25, 28, 39, 35]})

df2 = pd.DataFrame({'name':['kate', 'herz', 'sally'], 
									'score':[70, 60, 90]})
pd.merge(df1, df2)
```

age	 name 	score
0 	25 	kate 		70
1 	28	 herz 		60
2 	35	 sally 		90

**2.当左右连接字段不相同时，使用left_on, right_on**

```python
pd.merge(df1,  df2,  left_on="name",  right_on='call_name')
```

age	 name 	call_name  score
0	25		kate		kate			70
1	28		herz		herz			60
2	35		sally		sally			90

**3.合并后，删除重复的列**

```python
pd.merge(df1, df2, left_on='name', right_on='call_name').drop('name', axis=1)
```

​	age 	call_name 	score
0 		25 		kate 			70
1 		28 		herz 			60
2 		35 		sally 			90

**4.参数how的使用**

**1)默认：inner 内连接，取交集**

```python
pd.merge(df1, df2, on='name', how='inner')
```

​	age 	name 		score
0 		25		 kate 		70
1 		28		 herz		 60
2		 35		 sally 		90

**2)outer 外连接，取并集，并用nan填充**

```python
df3=pd.DataFrame({'name':['kate', 'herz', 'sally', 'cristin'], 
'score':[70, 60, 90, 30]})
pd.merge(df1, df3, on='name', how='outer')
```

age 		name 		score
0 	25 		kate 			70
1 	28 		herz 			60
2 	39 		catherine 	NaN
3 	35 		sally 			90
4 	NaN 	cristin 		 30

**3)left 左连接， 左侧取全部，右侧取部分**

```python
pd.merge(df1, df3, on='name', how='left')
```

​	age 		name 		score
0 		25 		kate 			70
1 		28 		herz 			60
2 		39 		catherine 	NaN
3 		35 		sally 			90

**4) right 有连接，左侧取部分，右侧取全部**

```python
pd.merge(df1, df3, on='name', how='right')
```

​	age 		name		 score
0 		25		 kate 			70
1 		28 		herz 			60
2 		35 		sally 			90
3 		NaN 	cristin 		30



### 2.4 append



## 3. Line and Row

### 3.1 Index

查找DataFrame数据类型中的某一（多）行或或列，这里记录两个可以实现该功能的函数：loc、iloc。获取dataframe的行列标题可以通过下面的命令实现：

```python
df.rows
df.columns
```



#### 3.1.1 loc

通过**label**选取数据，即通过**index**或**column**进行选取。loc方法有两个参数，按顺序控制行列选取，**当只输入一个参数时默认作为column**。

```python
#1.定位单行
df.loc['e']

#2.定位单列
df.loc[:, 'a']

#3.定位多行
df.loc['e':]

#4.定位多行多列
df.loc['e':, ["a", "b"]]	# 访问不连续的多行或多列
```

#### 3.1.2 iloc

通过**index_number**选取数据（只接受数字），即通过数据所在的自然行列数为选取数据。iloc方法也有两个参数，按顺序控制行列选取，**显示行列顺序与参数顺序有关**。

```python
#1.定位单行
df.iloc[1]
'''
a    3
b    4
c    5
Name: e,  dtype: int32
===================================
'''
#2.定位单列
df.iloc[:, 1]
'''
d     1
e     4
f     7
g    10
Name: b,  dtype: int32
===================================
'''
#3.定位多行
df.iloc[1:3]
'''
	a	b	c
e	3	4	5
f	6	7	8
===================================
'''
#4.定义多行多列
df.iloc[1:3, 1:2]
'''
	b
e	4
f	7
===================================
'''
```

#### 3.1.3 Getitem

> 通过中括号对列名直接索引，单括号索引返回结果为Series，双括号返回类型为二维列表。

```python
df[colsname]	# Series
df[[colsname]]	# DataFrame
```





### 3.2 Drop

> **DataFrame.drop**(*labels=None*, *axis=0*, *index=None*, *columns=None*,*level=None*, *inplace=False*, *errors='raise'*)

Drop specified labels from rows or columns.

Remove rows or columns by specifying label names and corresponding axis, or by specifying directly index or column names. When using a multi-index, labels on different levels can be removed by specifying the level.

Parameters

- **labels**single label or list-like

	Index or column labels to drop.

- **axis**{0 or ‘index’, 1 or ‘columns’}, default 0

	Whether to drop labels from the index (0 or ‘index’) or columns (1 or ‘columns’).

- **index**single label or list-like

	Alternative to specifying axis (`labels, axis=0` is equivalent to `index=labels`).

- **columns**single label or list-like

	Alternative to specifying axis (`labels, axis=1` is equivalent to `columns=labels`).

- **level**int or level name, optional

	For MultiIndex, level from which the labels will be removed.

- **inplace**bool, default False

	If False, return a copy. Otherwise, do operation inplace and return None.

- **errors**{‘ignore’, ‘raise’}, default ‘raise’

	If ‘ignore’, suppress error and only existing labels are dropped.

Returns

- DataFrame or None

	DataFrame without the removed index or column labels or None if `inplace=True`.

Raises

- KeyError

	If any of the labels is not found in the selected axis.

```python
df.drop([16, 17])
```

### 3.3 Rank

**函数原型**

> sort_values(by,  ascending)

**参数说明**

> by：列名，依旧该列进行排序
>
> ascending：确定排序方式，默认为True（降序）



## 4. Name

> 修改行或列的标题。

### 4.1 Reindex

更新index或者columns，不更新原frame，返回一个新的DataFrame，如果需要在原frame上修改，令参数`inplace="True"`，基本语法如下：

> DataFrame.**reindex**(*labels=None*, *index=None*, *columns=None*, *axis=None*, *method=None*, *copy=True*, *level=None*, *fill_value=nan*, *limit=None*, *tolerance=None*)

```python
# 返回一个新的DataFrame，更新index，原来的index会被替代消失
# 如果dataframe中某个索引值不存在，会自动补上NaN
df2 = df1.reindex(['a', 'b', 'c', 'd', 'e'])

# fill_valuse为原先不存在的索引补上默认值，不再是NaN
df2 = df1.reindex(['a', 'b', 'c', 'd', 'e'],   fill_value=0)

# inplace=Ture，在DataFrame上修改数据，而不是返回一个新的DataFrame
df1.reindex(['a', 'b', 'c', 'd', 'e'],   inplace=Ture)

# reindex不仅可以修改 索引(行)，也可以修改列
states = ["columns_a", "columns_b", "columns_c"]
df2 = df1.reindex( columns=states )
```



Conform Series/DataFrame to new index with optional filling logic.

Places NA/NaN in locations having no value in the previous index. A new object is produced unless the new index is equivalent to the current one and `copy=False`.

#### Parameters

**keywords for axes**	array-like, optionalNew labels / index to conform to, should be specified using keywords. Preferably an Index object to avoid duplicating data.

**method**	{None, 'backfill’/’bfill’, 'pad’/’ffill’, 'nearest’}Method to use for filling holes in reindexed DataFrame. Please note: this is only applicable to DataFrames/Series with a monotonically increasing/decreasing index.None (default): don’t fill gapspad / ffill: Propagate last valid observation forward to next valid.backfill / bfill: Use next valid observation to fill gap.nearest: Use nearest valid observations to fill gap.

**copy**	bool, default TrueReturn a new object, even if the passed indexes are the same.

**level**	int or nameBroadcast across a level, matching Index values on the passed MultiIndex level.

**fill_value**	scalar, default np.NaNValue to use for missing values. Defaults to NaN, but can be any “compatible” value.

**limit	**int, default NoneMaximum number of consecutive elements to forward or backward fill.

**tolerance**	optionalMaximum distance between original and new labels for inexact matches. The values of the index at the matching locations most satisfy the equation `abs(index[indexer] - target) <= tolerance`.Tolerance may be a scalar value, which applies the same tolerance to all values, or list-like, which applies variable tolerance per element. List-like includes list, tuple, array, Series, and must be the same size as the index and its dtype must exactly match the index’s type.

#### Returns

Series/DataFrame with changed index.

### 4.2 Rename

> DataFrame.**rename**(*mapper=None*, *index=None*, *columns=None*, *axis=None*, *copy=True*, *inplace=False*, *level=None*, *errors='ignore'*)

Alter axes labels.

Function / dict values must be unique (1-to-1). Labels not contained in a dict / Series will be left as-is. Extra labels listed don’t throw an error.

#### Parameters

|  参数   |                             含义                             |
| :-----: | :----------------------------------------------------------: |
| mapper  | 映射结构，修改columns或index要传入一个映射体，可以是字典、函数。修改列标签跟columns参数一起；修改行标签跟index参数一起。 |
|  index  |        行标签参数，mapper, axis=0 等价于 index=mapper        |
| columns |       列标签参数，mapper, axis=1 等价于 columns=mapper       |
|  axis   |       轴标签格式，0代表index，1代表columns，默认index        |
|  copy   |               默认为True，赋值轴标签后面的数据               |
| inplace |     默认为False，不在原处修改数据，返回一个新的DataFrame     |
|  level  | 默认为None，处理单个轴标签（有的数据会有2个或多个index或columns） |
| errors  | 默认ignore，如果映射体里面包含DataFrame没有的轴标签，忽略不报错 |

#### Returns

DataFrame or NoneDataFrame with the renamed axis labels or None if `inplace=True`.

#### Raises

KeyErrorIf any of the labels is not found in the selected axis and “errors=’raise’”.

---

### 4.3 Set_index

将DataFrame中的列columns设置成索引index，打造层次化索引的方法。

```python
# 将columns中的其中两列：race和sex的值设置索引，race为一级，sex为二级
# inplace=True 在原数据集上修改的
adult.set_index(['race', 'sex'],  inplace = True) 

# 默认情况下，设置成索引的列会从DataFrame中移除
# drop=False将其保留下来
adult.set_index(['race', 'sex'],  drop=False) 
```

### 4.3 Reset_index

reset_index()：将使用set_index()打造的层次化逆向操作。

既是取消层次化索引，将索引变回列，并补上最常规的数字索引。

```python
df.reset_index()
```

## 5 重复项

### 5.1 查看是否存在重复项

DataFrame的duplicated方法返回一个布尔型Series, 表示各行是否重复行。

```python
a = df.duplicated()
```

### 5.2 删除

而 drop_duplicates方法，它用于返回一个移除了重复行的DataFrame

```python
df = df.drop_duplicates()
```

## 6 元素

### 6.1 查找

通过标签或行号获取某个数值的具体位置（DataFrame数据类型中）

```python
#DataFrame数据
	a	b	c
d	0	1	2
e	3	4	5
f	6	7	8
g	9	10	11
#获取第2行，第3列位置的数据
df.iloc[1, 2]
Out[205]: 5

#获取f行，a列位置的数据
df.loc['f', 'a']
Out[206]: 6
'''
iat：依据行号定位
at：依旧标签定位
'''
```

### 6.2 修改

修改DataFrame中的某一元素

```python
df['列名'][行序号（index）] = "新数据"
```

## 7.排序

```python
df.sort_values(by="sales" ,  ascending=False)
```

函数原型：

> DataFrame.sort_values(by,  axis=0,  ascending=True,  inplace=False,  kind='quicksort’,  na_position='last’)

列举常用的参数用法：

> - by：函数的操作对象是DataFrame
> - axis：进行操作的列名，多个列名用列表表示
> - ascending：默认为升序True
>

```python
df
'''
输出：
    col1 col2 col3
0   A    2    0
1   A    1    1
2   B    9    9
3   NaN  8    4
4   D    7    2
5   C    4    3
'''
df = df.sort_values(by=['col1'])
'''
输出：
   col1 col2 col3
0   A    2    0
1   A    1    1
2   B    9    9
5   C    4    3
4   D    7    2
3   NaN  8    4
'''
```

## 8. 处理缺损数据

### 8.1 dropna

> 该方法用于检查是否存在缺损数据，若存在则删除相关列与行。

**函数：**

```python
pd.dropna(axis=0,  how='any’,  thresh=None,  subset=None,  inplace=False)
```

**参数说明：**

- `axis`: 该参数确定是删除包含缺失值的行或列， `axis=0`或`axis='index’`删除含有缺失值的行，`axis=1`或`axis='columns’`删除含有缺失值的列。
- `how`：`any`存在即nan即丢弃，`all`全部为nan才丢弃。
- `thresh`：默认值 None值，`thresh=n`则表明每行至少n的非NaN值，否则则删除该行。
- `subset`：定义要在哪些列中查找缺失值。
- `inplace`：默认值 False，是否直接在原DataFrame进行修改。

### 8.2 isnan

### 8.3 fillna

## 9. 其他用法

### 9.1 连续时间序列

```python
pd.date_range(startdate, enddate，periods, freq)
```

下面是python可使用的时间序列的基础频率表：

| 别名               | 偏移量类型         | 说明                                 |
| :----------------- | :----------------- | :----------------------------------- |
| D                  | Day                | 每日历日                             |
| B                  | BusinessDay        | 每工作日                             |
| H                  | Hour               | 每小时                               |
| T或min             | Minute             | 每分钟                               |
| S                  | Second             | 每秒                                 |
| L或ms              | Milli              | 每毫秒                               |
| U                  | Micro              | 每微秒                               |
| M                  | MonthEnd           | 每月最后一个日历日                   |
| BM                 | BusinessMonthEnd   | 每月最后一个工作日                   |
| MS                 | MonthBegin         | 每月第一个日历日                     |
| BMS                | BusinessMonthBegin | 每月第一个工作日                     |
| W-MON、W-TUE       | Week               | 每周的星期几                         |
| WOM-1MON、WOM-2MON | WeekofMonth        | 每月第几周的星期几                   |
| Q-JAN、Q-FEB       | QuarterEnd         | 每个季度对应的该月份的最后一个日历日 |
| BQ-JAN、BQ-FEB     | BusinessQuarterEnd | 每个季度对应的该月份的最后一个工作日 |
| QS-JAN、QS-FEB     | QuarterBegin       | 每个季度对应的该月份的第一个日历日   |
| BQS-JAN、BQS-FEB   | QuarterBegin       | 每个季度对应的该月份的第一个工作日   |
| A-JAN、B-FEB       | YearEnd            | 每年指定月份的最后一个日历日         |
| BA-JAN、BA-FEB     | BusinessYearEnd    | 每年指定月份的最后一个工作日         |
| AS-JAN、AS-FEB     | YearBegin          | 每年指定月份的第一个日历日           |
| BAS-JAN、BAS-FEB   | BusinessYearBegin  | 每年指定月份的第一个工作日           |



### 9.2 clip截取数据

```python
DataFrame.clip(lower=None, upper=None, axis=None, inplace=False, *args, **kwargs)
```

在输入阈值处修剪值。

将边界外的值指定给边界值。阈值可以是奇异值或数组，并且在后一种情况下，剪切在指定轴中以元素方式执行。

| 参数        | 参数说明                                                     |
| ----------- | ------------------------------------------------------------ |
| **lower**   | float或array_like，默认为None最小阈值。低于此阈值的所有值都将设置为它。 |
| **upper**   | float或array_like，默认为None最大阈值。高于此阈值的所有值都将设置为它。 |
| **axis**    | int或string轴名称，可选沿给定轴将对象与下部和上部对齐。      |
| **inplace** | 布尔值，默认为False是否对数据执行操作。版本0.21.0中的新功能。 |

**返回值**：  Series或DataFrame与调用对象相同的类型，替换了剪辑边界之外的值

## 10.数据处理

### 1. 数据偏移

#### pandas.DataFrame.shift

`DataFrame.shift`(*periods=1*, *freq=None*, *axis=0*, *fill_value=<object object>*)

> Shift index by desired number of periods with an optional time freq.When freq is not passed, shift the index without realigning the data. If freq is passed (in this case, the index must be date or datetime, or it will raise a NotImplementedError), the index will be increased using the periods and the freq. freq can be inferred when specified as “infer” as long as either freq or inferred_freq attribute is set in the index.

#### Parameters

> - **periods**	int
>
>   Number of periods to shift. Can be positive or negative.
>
> - **freq**     DateOffset, tseries.offsets, timedelta, or str, optional
>
>   Offset to use from the tseries module or time rule (e.g. 'EOM’). If freq is specified then the index values are shifted but the data is not realigned. That is, use freq if you would like to extend the index when shifting and preserve the original data. If freq is specified as “infer” then it will be inferred from the freq or inferred_freq attributes of the index. If neither of those attributes exist, a ValueError is thrown.
>
> - **axis**    {0 or 'index’, 1 or 'columns’, None}, default None
>
>   Shift direction.
>
> - **fill_value**    object, optional
>
>   The scalar value to use for newly introduced missing values. the default depends on the dtype of self. For numeric data, `np.nan` is used. For datetime, timedelta, or period data, etc. `NaT` is used. For extension dtypes, `self.dtype.na_value` is used.*Changed in version 1.1.0.*

#### Returns

> **DataFrame**,	Copy of input object, shifted.

### 2. 列变索引

DataFrame.`set_index`(*keys*, *drop=True*, *append=False*, *inplace=False*, *verify_integrity=False*)

> Set the DataFrame index using existing columns.Set the DataFrame index (row labels) using one or more existing columns or arrays (of the correct length). The index can replace the existing index or expand on it.

### Parameters

> **keys**	label or array-like or list of labels/arrays
>
> This parameter can be either a single column key, a single array of the same length as the calling DataFrame, or a list containing an arbitrary combination of column keys and arrays. Here, “array” encompasses [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series), [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index), `np.ndarray`, and instances of [`Iterator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator).
>
> **drop**	bool, default True
>
> Delete columns to be used as the new index.
>
> **append**	bool, default False
>
> Whether to append columns to existing index.
>
> **inplace	**bool, default False
>
> If True, modifies the DataFrame in place (do not create a new object).
>
> **verify_integrity**	bool, default False
>
> Check the new index for duplicates. Otherwise defer the check until necessary. Setting to False will improve the performance of this method.

### Returns

> DataFrame or NoneChanged row labels or None if `inplace=True`.



---

# Excel处理

## 1. 读取

**函数：**

```python
pandas.read_excel（io，sheet_name = 0，header = 0，names = None，
index_col = None，
usecols = None，squeeze = False,dtype = None, ...）
```

**参数：**

> `io`：字符串，文件的路径对象。
>
> `sheet_name`：None、string、int、字符串列表或整数列表，默认为0。字符串用于工作表名称,整数用于零索引工作表位置,字符串列表或整数列表用于请求多个工作表，为None时获取所有工作表。
>
> | 值                        | 对应操作                                  |
> | ------------------------- | :---------------------------------------- |
> | sheet_name=0              | 第一张作为DataFrame                       |
> | sheet_name=1              | 第二张作为DataFrame                       |
> | sheet_name=[0,1,'Sheet5'] | 第1页，第2页和第5页作为DataFrames的字典。 |
>
> `header`：指定作为列名的行，默认0，即取第一行的值为列名。数据为列名行以下的数据；若数据不含列名，则设定 header = None。
>
> `names`：默认为None，要使用的列名列表，如不包含标题行，应显示传递`header=None`。
>
> `index_col`：指定列为索引列，默认None列（0索引）用作DataFrame的行标签（若只使用列切片，则此处的列索引号为相对切片的索引号）。
>
> `usecols`：int或list，默认为None，<u>cols顺序不影响结果</u>。
>
> - 如果为None则解析所有列
> - 如果为int列表则表示要解析的列号列表
> - 如果为字符串则表示以逗号分隔的Excel列字母和列范围列表（例如“A：E”或“A，C，E：F”），<u>包括两端那两列</u>。
>
> `squeeze`：boolean，默认为False,如果解析的数据只包含一列，则返回一个Series。
>
>
> `dtype`：列的类型名称或字典，默认为None。数据或列的数据类型。例如{'a'：np.float64，'b'：np.int32}使用对象保存存储在Excel中的数据而不解释dtype。如果指定了转换器，则它们将应用于dtype转换的INSTEAD。
>
> `skiprows`：省略指定行数的数据,从第一行开始。
>
> `skipfooter`：省略指定行数的数据，从尾部数的行开始。
>
> `dtype`:字典类型{'列名1':数据类型，'列名’:数据类型}，设定指定列的数据类型。


```python
xls = pd.read_excel("1.xls")
type(xls)	# pandas.core.frame.DataFrame
```

由此可见，文档读取后得到的数据类型是pandas常用的数据类型DataFrame，大多数操作可以共通。



## 2. 保存与写入

要将单个对象写入excel文件, 我们必须指定目标文件名。如果要写入多个工作表, 则需要使用目标文件名创建一个ExcelWriter对象, 并且还需要在必须写入的文件中指定工作表。亦即，新文件的写入可通过相同操作实现。

也可以通过指定唯一的sheet_name来写入多张纸。必须保存所有写入文件的数据的更改。

注意：如果我们创建的ExcelWriter对象的文件名已经存在, 它将删除现有文件的内容。

**句法**

```python
writer = pd.ExcelWriter(path + filename)
DataFrame.to_excel(writer, sheet_name='Sheet1', na_rep='', float_format=None, 
                   columns=None, header=True, index=True, index_label=None, 
                   startrow=0, startcol=0, engine=None, merge_cells=True, 
                   encoding=None, inf_rep='inf',verbose=True, freeze_panes=None)
```

**参数**

> **excel_writer：文件路径或现有的ExcelWriter。**
>
> **sheet_name：它是指包含DataFrame的工作表的名称。**
>
> na_repr：缺少数据表示形式。
>
> **float_format：这是一个可选参数, 用于格式化浮点数字符串。**
>
> **columns：指要写入的列。**
>
> **header：写出列名。如果给出了字符串列表, 则假定它是列名的别名。**
>
> **index：布尔值，是否保留原行头写入索引。**
>
> index_label：引用索引列的列标签。如果未指定, 并且标头和索引为True, 则使用索引名称。如果DataFrame使用MultiIndex, 则应给出一个序列。
>
> **startrow：默认值0，在它的下一列开始写入数据。它指向转储DataFrame的左上单元格行。**
>
> **startcol：默认值0。它指向转储DataFrame的左上方单元格列。**
>
> engine：这是一个可选参数, 用于写入要使用的引擎, openpyxl或xlsxwriter。
>
> merge_cells：返回布尔值, 其默认值为True。它将MultiIndex和Hierarchical行写为合并的单元格。
>
> encoding：这是一个可选参数, 可对生成的excel文件进行编码。仅对于xlwt是必需的。
>
> inf_rep：它也是一个可选参数, 默认值为inf。它通常表示无穷大。
>
> verbose：返回一个布尔值。它的默认值为True。
> 它用于在错误日志中显示更多信息。
>
> frozen_panes：它也是一个可选参数, 用于指定要冻结的最底部一行和最右边一列。

通过sheet_name，startrow与startcol，可以实现定向excel写入。



## 3. 数据操作

1. excel文件读取后，columns为目标第一行信息内容，第0行为文件第二行，同时也作为第一行存在，行头默认为索引序号（不指定的情况下），如需跳过特定行，可以通过传参`skipfooter`实现；

2. 读取后的DataFrame不支持`DataFrame.index`或`DataFrame[columns]`的索引形式，但仍可以通过`iloc`进行行列条件索引，如需使用上述方式，需获取`DataFrame.values`对应的array对象，再执行上述操作；

3. 原数组组的修改，通过元素的直接访问与修改即可完成，其他大体操作，与DataFrame操作一致，需要注意的是，**pd行索引号与excel行序号相差2**，即excel表格中的第二行对应pd中第0行；

4. 具体实例可参见 **Excel Operation.ipynb** ；

5. 自定义格式输出；借助`XlsxWriter Excel object`，感觉反而不大方便；

   ```python
   df = pd.DataFrame(np.arange(16).reshape(4,4), columns=list('ABCD'))
   BASEINPUT=os.path.dirname(__file__)
   OUTPUTH=os.path.join(BASEINPUT,'result.xlsx')
   writer = pd.ExcelWriter(OUTPUTH, engine='xlsxwriter')
   # Convert the dataframe to an XlsxWriter Excel object. 
   df.to_excel(writer, sheet_name='Sheet1', startrow=1, header=0,
               index=False)
   # Get the xlsxwriter workbook and worksheet objects.
   workbook  = writer.book
   worksheet = writer.sheets['Sheet1']
   # Add a header format.
   header_format = workbook.add_format({
       'bold': True, # 字体加粗
       'text_wrap': True, # 是否自动换行
       'valign': 'top',  #垂直对齐方式
       'align': 'right', # 水平对齐方式
       'fg_color': '#D7E4BC', # 单元格背景颜色
       'border': 2}) # 单元格边框宽度
   yellow = workbook.add_format({'fg_color': '#FFEE99'})
   red=workbook.add_format({'fg_color': '#2dB054'})
   # Write the column headers with the defined format.
   for col_num, value in enumerate(df.columns.values):
       if col_num%2==0:
           worksheet.write(0, col_num, value, header_format)
       else:
           worksheet.write(0, col_num, value, yellow)
   # Write the row with the defined format.
   for index, value in df.iterrows():
       print(index," -- > ",value.values)
       if index % 2 == 0:
           worksheet.write(index+1, 0, value[0], header_format)
       else:
           worksheet.write(index+1, 0, value[0], yellow)
   worksheet.set_column("A:C", 16)
   format2 = workbook.add_format({'bold':  True, 'align': 'vcenter', 
                                  'valign': 'top', 'text_wrap': True})
   worksheet.set_row(0, cell_format=format2)
   writer.save()
   ```

   

## 4. 其他库

可用于处理Excel的库性能对比，此处推荐xlwings。

![图片](E:/工具/Typora/Temp/640.webp)

