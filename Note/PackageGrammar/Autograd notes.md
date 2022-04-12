这篇文章主要介绍了python中几种自动微分库解析,文中通过示例代码介绍的非常详细，对大家的学习或者工作具有一定的参考学习价值,需要的朋友可以参考下

**前言**

简单介绍下python的几个自动求导工具，tangent、autograd、sympy；

在各种机器学习、深度学习框架中都包含了自动微分，微分主要有这么四种：手动微分法、数值微分法、符号微分法、自动微分法，这里分别简单走马观花（hello world式）的介绍下下面几种微分框架；

sympy 强大的科学计算库，使用的是符号微分，通过生成符号表达式进行求导；求得的导数不一定为最简的，当函数较为复杂时所生成的表达式树异常复杂；

autograd自动微分先将符号微分用于基本的算子，带入数值并保存中间结果，后应用于整个函数；自动微分本质上就是图计算，容易做很多优化所以广泛应用于各种机器学习深度学习框架中；

tangent 为源到源（source-to-source）的自动微分框架，在计算函数f微分时他通过生成新函数f_grad来计算该函数的微分，与目前所存在的所有自动微分框架都有所不同；由于它是通过生成全新的函数来计算微分所以具有非常搞的可读性、可调式性这也是官方所说的与当前自动微分框架的重大不同；

**sympy 求导**



```
def grad():# 定义表达式的变量名称x, y = symbols('x y')# 定义表达式z = x**2 +y**2# 计算z关于y对应的偏导数return diff(z, y)func = grad()
```

输出结果表达式z的导函数z‘=2*y

```
print(func)
```

把y 等于6 带入计算 结果 为12

```
print(func.evalf(subs ={'y':3}))
```

**Autograd求偏导**

```
import autograd.numpy as npfrom autograd import grad#表达式 f(x,y)=x^2+3xy+y^2#df/dx = 2x+3y#df/dy = 3x+2y#x=1,y=2#df/dx=8#df/dy=7def fun(x, y):z=x**2+3*x*y+y**2return zfun_grad = grad(fun)fun_grad(2.,1.)
```

输出：7.0

**tangent求导**

```
import tangentdef fun(x, y):z=x**2+3*x*y+y**2return z
```

默认为求z关于x的偏导数

```
dy_dx = tangent.grad(fun)
```

输出偏导数值为 8 ，z' = 2 * x，此处x传任何值都是一样的

```
df(4, y=1)
```

可通过使用wrt参数指定求关于某个参数的偏导数，下面为求z关于y的偏导数

```
df = tangent.grad(funs, wrt=([1]))
```

输出值为10 ,z' = 2 *y，此处x传任何值都是一样的

```
df(x=0, y=5)
```

上面说了那么多也没体现出tangent的核心：源到源（source-to-source）

在生成导函数的时候加入verbose=1参数，即可看到tangent为我们生成的用于计算导数的函数，默认情况下该值为0所以我们没感觉到tangent的求导与别的自动微分框架有什么区别；

```
def df(x):z = x**2return zdf = tangent.grad(df, verbose=1)df(x=2)
```

在执行完上述代码后，我们看到了tangent为我们所生成用于求导数的函数：

```
def ddfdx(x, bz=1.0):z = x ** 2assert tangent.shapes_match(z, bz), 'Shape mismatch between return value (%s) and seed derivative (%s)' % (numpy.shape(z), numpy.shape(bz))# Grad of: z = x ** 2_bx = 2 * x * bzbx = _bxreturn bx
```

ddfdx函数就是所生成的函数，从中我们也可以看到表达式z的导函数z'=2 * x，tangent就是通过执行该函数用于求得导数的；

sympy 中的自动微分只是它强大的功能之一，autograd 从名字也可知它就是为了自动微分而生的，tangent初出茅庐2017年底Google才发布的自动微分方法也比较新颖，从17年发v0.1.8版本后也没见发版，源码更新也不够活跃；sympy、autograd比较成熟，tangent还有待观察；