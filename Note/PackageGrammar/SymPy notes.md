# SymPy库

## 简介

SymPy是一个符号计算的Python库。它的目标是成为一个全功能的计算机代数系统，同时保持代码简洁、易于理解和扩展。它完全由Python写成，不依赖于外部库。SymPy支持符号计算、高精度计算、模式匹配、绘图、解方程、微积分、组合数学、离散 数学、几何学、概率与统计、物理学等方面的功能。

## 基本常识

### 实数，有理数和整数

SymPy有三个内建的数值类型：实数，有理数和整数。有理数类用两个整数来表示一个有理数。分子与分母，所以Rational(1,2)代表1/2，Rational(5,2)代表5/2，等等。

```python
>>>from sympy import *
>>>a = Rational(1,2)
>>>a
1/2
>>>a*2
1
>>>Rational(2)**50/Rational(10)**50
1/88817841970012523233890533447265625
```

当利用Python的整数计算时要注意一下，Python只会截取除法的整数部分：

```python
>>>1/2
0
>>>1.0/2
0.5
```

然而你可以：

```python
>>>from __future__ import division
>>>1/2 #doctest: +SKIP
0.5
```

正确的除法在python3k和sympy中这样做，是标准的。

### 特殊的常数

我们也可以有一些特殊的常数，像e和pi，它们会被当作符号去对待。（1+pi不会求得值，反而它会保持为1+pi），例如：

```python
>>>pi**2
pi**2
>>>pi.evalf()
3.14159265358979
>>>(pi+exp(1)).evalf()
5.85987448204884
```

### 求表达式的浮点数-evalf()函数

正如你看到的，evalf()函数可以用求出表达式的浮点数。
有一个无穷大的类型，被成为oo：

```python
>>>oo > 99999
True
>>>oo + 1
oo
If the substitution will be followed by numerical evaluation, it is better to pass the substitution to evalf as
>>> (1/x).evalf(subs={x: 3.0}, n=21)
0.333333333333333333333
rather than
>>> (1/x).subs({x: 3.0}).evalf(21)
0.333333333333333314830
```

### 虚数单位i



```python
In [13]: import sympy

In [14]: sympy.I
Out[14]: I

In [15]: sympy.I ** 2
Out[15]: -1

# 求-1的平方根
In [16]: sympy.sqrt(-1)
Out[16]: I
```

注：本文后面的示例都省略导包语句：`import sympy`

### 自然对数的底e



```python
In [18]: sympy.E
Out[18]: E

# 求对数
In [20]: sympy.log(sympy.E)
Out[20]: 1
```

### 无穷大oo



```python
In [26]: 1/sympy.oo
Out[26]: 0

In [27]: 1 + sympy.oo
Out[27]: oo
```

### 圆周率pi



```cpp
In [60]: sympy.pi
Out[60]: pi

In [61]: sympy.sin(sympy.pi/2)
Out[61]: 1
```



## 定义变量-Symbols函数

对比与其他的计算机代数系统，在SymPy中要明确声明符号变量：

```python
>>> x = symbols('x')
>>> x + 1
x + 1
>>>x,y,z=symbols('x y z')
>>> crazy = symbols('unrelated')
>>> crazy + 1
unrelated + 1
>>> x = symbols('x')
>>> expr = x + 1
>>> x = 2
>>> print(expr)
x + 1
Changing x to 2 had no effect on expr. This is because x = 2 changes the Python variable x to 2, but has no effect on the SymPy Symbol x, which was what we used in creating expr.
```

## 变量替换-subs函数

```python
>>> x = symbols('x')
>>> expr = x + 1
>>> expr.subs(x, 2)
3
>>> from sympy import pi, exp, limit, oo
>>> from sympy.abc import x, y
>>> (1 + x*y).subs(x, pi)
pi*y + 1
>>> (1 + x*y).subs({x:pi, y:2})
1 + 2*pi
>>> (1 + x*y).subs([(x, pi), (y, 2)])
1 + 2*pi
>>> reps = [(y, x**2), (x, 2)]
>>> (x + y).subs(reps)
6
>>> (x + y).subs(reversed(reps))
x**2 + 2
>>> (x**2 + x**4).subs(x**2, y)
y**2 + y
>>> (x**2 + x**4).xreplace({x**2: y})
x**4 + y
>>> (x/y).subs([(x, 0), (y, 0)])
0
>>> (x/y).subs([(x, 0), (y, 0)], simultaneous=True)
nan
>>> ((x + y)/y).subs({x + y: y, y: x + y})
1
>>> ((x + y)/y).subs({x + y: y, y: x + y}, simultaneous=True)
y/(x + y)
>>> limit(x**3 - 3*x, x, oo)
oo
```

调用方式：[subs(*args, **kwargs)]

## 代数

局部的代数式展开，使用apart(expr, x):

```python
In [1]: 1/( (x+2)*(x+1) )
Out[1]:
       1
───────────────
(2 + x)*(1 + x)
In [2]: apart(1/( (x+2)*(x+1) ), x)
Out[2]:
  1       1
───── - ─────
1 + x   2 + x
In [3]: (x+1)/(x-1)
Out[3]:
-(1 + x)
────────
  1 - x
In [4]: apart((x+1)/(x-1), x)
Out[4]:
      2
1 - ─────
    1 - x
```

## 代数式的合并

(相当于展开的逆运算)，使用together(expr, x)：

```python
In [7]: together(1/x + 1/y + 1/z)
Out[7]:
x*y + x*z + y*z
───────────────
    x*y*z
In [8]: together(apart((x+1)/(x-1), x), x)
Out[8]:
-1 - x
──────
1 - x
In [9]: together(apart(1/( (x+2)*(x+1) ), x), x)
Out[9]:
      1
───────────────
(2 + x)*(1 + x)
```

## 微积分

### 极限

在sympy中极限容易求出，它们遵循极限语法 limit(function, variable, point) ，所以计算x->0时f(x)的极限，即limit(f, x, 0)：

```python
>>>from sympy import *
>>>x=Symbol("x")
>>>limit(sin(x)/x, x, 0)
1
>>>limit(x, x, oo)
oo
>>>limit(1/x, x, oo)
0
>>>limit(x**x, x, 0)
1
```

有一些特殊的极限的例子，可以阅读文件[test_demidovich.py](http://git.sympy.org/?p=sympy.git;a=blob;f=sympy/series/tests/test_demidovich.py)

### 微分

可以对任意SymPy表达式微分，如：diff(func, var)或者func.diff(var,n),n表示微分阶级，亦可func.diff(var1,var2)求偏微分。

例如：

```python
>>>from sympy import *
>>>x = Symbol('x')
>>>diff(sin(x), x)
cos(x)
>>>diff(sin(2*x), x)
2*cos(2*x)
>>>diff(tan(x), x)
1 + tan(x)**2
```

可以通过以下验证:

```python
>>>limit((tan(x+y)-tan(x))/y, y, 0)
1 + tan(x)**2
```

计算高阶微分 diff(func, var, n) :

```python
>>>diff(sin(2*x), x, 1)
2*cos(2*x)
>>>diff(sin(2*x), x, 2)
-4*sin(2*x)
>>>diff(sin(2*x), x, 3)
-8*cos(2*x)
```

### 级数展开

函数 series(var, point, order)：

```python
>>>from sympy import *
>>>x = Symbol('x')
>>>cos(x).series(x, 0, 10)
1 - x**2/2 + x**4/24 - x**6/720 + x**8/40320 + O(x**10)
>>>(1/cos(x)).series(x, 0, 10)
1 + x**2/2 + 5*x**4/24 + 61*x**6/720 + 277*x**8/8064 + O(x**10)
```

### 积分

SymPy支持不定积分，超越函数与特殊函数的定积分。SymPy有力的扩展Risch-Norman 算法和模型匹配算法。

```python
>>>from sympy import *
>>>x, y = symbols('xy')
```

初等函数：

```python
>>>integrate(6*x**5, x)
x**6
>>>integrate(sin(x), x)
-cos(x)
>>>integrate(log(x), x)
-x + x*log(x)
>>>integrate(2*x + sinh(x), x)
cosh(x) + x**2
```

特殊函数：

```python
>>>integrate(exp(-x**2)*erf(x), x)
pi**(1/2)*erf(x)**2/4
```

定积分：

```python
>>>integrate(x**3, (x, -1, 1))
0
>>integrate(sin(x), (x, 0, pi/2))
1
>>>integrate(cos(x), (x, -pi/2, pi/2))
2
```

一些广义积分也可以被支持：

```python
>>>integrate(exp(-x), (x, 0, oo))
1
>>>integrate(log(x), (x, 0, 1))
-1
```

### 复数

```python
>>>from sympy import Symbol, exp, I
>>>x = Symbol("x")
>>>exp(I*x).expand()
exp(I*x)
>>>exp(I*x).expand(complex=True)
I*exp(-im(x))*sin(re(x)) + cos(re(x))*exp(-im(x))
>>>x = Symbol("x", real=True)
>>>exp(I*x).expand(complex=True)
I*sin(x) + cos(x)
```

### 函数

三角函数：:

```python
In [1]: sin(x+y).expand(trig=True)
Out[1]: cos(x)*sin(y) + cos(y)*sin(x)
In [2]: cos(x+y).expand(trig=True)
Out[2]: cos(x)*cos(y) - sin(x)*sin(y)
In [3]: sin(I*x)
Out[3]: I*sinh(x)
In [4]: sinh(I*x)
Out[4]: I*sin(x)
In [5]: asinh(I)
Out[5]:
π*I
───
 2
In [6]: asinh(I*x)
Out[6]: I*asin(x)
In [15]: sin(x).series(x, 0, 10)
Out[15]:
     3     5     7       9
    x     x     x       x
x - ── + ─── - ──── + ────── + O(x**10)
    6    120   5040   362880
In [16]: sinh(x).series(x, 0, 10)
Out[16]:
     3     5     7       9
    x     x     x       x
x + ── + ─── + ──── + ────── + O(x**10)
    6    120   5040   362880
In [17]: asin(x).series(x, 0, 10)
Out[17]:
     3      5      7       9
    x    3*x    5*x    35*x
x + ── + ──── + ──── + ───── + O(x**10)
    6     40    112     1152
In [18]: asinh(x).series(x, 0, 10)
Out[18]:
     3      5      7       9
    x    3*x    5*x    35*x
x - ── + ──── - ──── + ───── + O(x**10)
    6     40    112     1152
```

球谐函数：

```python
In [1]: from sympy.abc import theta, phi
In [2]: Ylm(1, 0, theta, phi)
Out[2]:
     ————
╲╱ 3 *cos(θ)
────────────
        ——
  2*╲╱ π
In [3]: Ylm(1, 1, theta, phi)
Out[3]:
    ——            I*φ
-╲╱ 6   *│sin(θ)│*ℯ
────────────────────
           ——
      4*╲╱ π
In [4]: Ylm(2, 1, theta, phi)
Out[4]:
   ———                  I*φ
-╲╱ 30  *│sin(θ)│*cos(θ)*ℯ
────────────────────────────
                ——
          4*╲╱ π
```

阶乘和伽玛函数：

```python
In [1]: x = Symbol("x")
In [2]: y = Symbol("y", integer=True)
In [3]: factorial(x)
Out[3]: Γ(1 + x)
In [4]: factorial(y)
Out[4]: y!
In [5]: factorial(x).series(x, 0, 3)
Out[5]:
                    2           2    2  2
                   x *EulerGamma    π *x
1 - x*EulerGamma + ────────────── + ───── + O(x**3)
                         2            12
```

Zeta函数:

```python
In [18]: zeta(4, x)
Out[18]: ζ(4, x)
In [19]: zeta(4, 1)
Out[19]:
  4
π
──
90
In [20]: zeta(4, 2)
Out[20]:
       4
     π
-1 + ──
     90
In [21]: zeta(4, 3)
Out[21]:
         4
  17   π
- ── + ──
  16   90
```

### 多项式

```python
In [1]: chebyshevt(2, x)
Out[1]:
        2
-1 + 2*x
In [2]: chebyshevt(4, x)
Out[2]:
       2      4
1 - 8*x  + 8*x
In [3]: legendre(2, x)
Out[3]:
          2
       3*x
-1/2 + ────
       2
In [4]: legendre(8, x)
Out[4]:
          2         4         6         8
35   315*x    3465*x    3003*x    6435*x
─── - ────── + ─────── - ─────── + ───────
128     32        64        32       128
In [5]: assoc_legendre(2, 1, x)
Out[5]:
            —————
         ╱     2
-3*x*╲╱  1 - x
In [6]: assoc_legendre(2, 2, x)
Out[6]:
      2
3 - 3*x
In [7]: hermite(3, x)
Out[7]:
           3
-12*x + 8*x
```

### 微分方程

在sympy中：

```python
In [4]: f(x).diff(x, x) + f(x)     #注意在使用输入该命令之前，一定要声明f=Function('f')
Out[4]:
  2
 d
─────(f(x)) + f(x)
dx dx
In [5]: dsolve(f(x).diff(x, x) + f(x), f(x))
Out[5]: C₁*sin(x) + C₂*cos(x)
```

### 代数方程

在sympy中：

```python
In [7]: solve(x**4 - 1, x)
Out[7]: [i, 1, -1, -i]
In [8]: solve([x + 5*y - 2, -3*x + 6*y - 15], [x, y])
Out[8]: {y: 1, x: -3}
```

## 线性代数

### 矩阵

矩阵由矩阵类创立建:

```python
>>>from sympy import Matrix
>>>Matrix([[1,0], [0,1]])
[1, 0]
[0, 1]
```

不只是数值矩阵，亦可为代数矩阵，即矩阵中存在符号：

```python
>>>x = Symbol('x')
>>>y = Symbol('y')
>>>A = Matrix([[1,x], [y,1]])
>>>A
[1, x]
[y, 1]
>>>A**2
[1 + x*y,     2*x]
[    2*y, 1 + x*y]
```

关于矩阵更多的例子，请看线性代数教程。

## 系数匹配

使用 .match()方法，引用Wild类，来执行表达式的匹配。该方法会返回一个字典。

```python
>>>from sympy import *
>>>x = Symbol('x')
>>>p = Wild('p')
>>>(5*x**2).match(p*x**2)
{p_: 5}
>>>q = Wild('q')
>>>(x**2).match(p*x**q)
{p_: 1, q_: 2}
```

如果匹配不成功，则返回None：

```python
>>>print (x+1).match(p**x)
None
```

可以使用Wild类的‘exclude’参数（排除参数），排除不需要和无意义的匹配结果,来保证结论中的显示是唯一的：

```python
>>>x = Symbol('x')
>>>p = Wild('p', exclude=[1,x])
>>>print (x+1).match(x+p) # 1 is excluded
None
>>>print (x+1).match(p+1) # x is excluded
None
>>>print (x+1).match(x+2+p) # -1 is not excluded
{p_: -1}
```

## 打印输出

### 标准

str(expression)返回如下：

```python
>>>from sympy import Integral
>>>from sympy.abc import x
>>>print x**2
x**2
>>>print 1/x
1/x
>>>print Integral(x**2, x)
Integral(x**2, x)
```

### Pretty Printing

用pprint函数可以输出不错的ascii艺术：

```python
>>>from sympy import Integral, pprint
>>>from sympy.abc import x
>>>pprint(x**2) #doctest: +NORMALIZE_WHITESPACE
2
x
>>>pprint(1/x)
1
-
x
>>>pprint(Integral(x**2, x))
 /
|
|  2
| x  dx
|
/
```

[Pretty PrintingWiki]
提示：在python解释器中，为使pretty printing为默认输出，使用：

```python
python
Python 2.5.2 (r252:60911, Jun 25 2008, 17:58:32)
[GCC 4.3.1] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from sympy import *
>>> import sys
>>> sys.displayhook = pprint
>>> var("x")
x
>>> x**3/3
3
x
--
3
>>> Integral(x**2, x) #doctest: +NORMALIZE_WHITESPACE
/
|
|  2
| x  dx
|
/
```

Python printing

```python
>>>from sympy.printing.python import python
>>>from sympy import Integral
>>>from sympy.abc import x
>>>print python(x**2)
x = Symbol('x')
e = x**2
>>>print python(1/x)
x = Symbol('x')
e = 1/x
>>>print python(Integral(x**2, x))
x = Symbol('x')
e = Integral(x**2, x)
```

LaTeX printing

```python
>>>from sympy import Integral, latex
>>>from sympy.abc import x
>>>latex(x**2)
$x^{2}$
>>>latex(1/x)
$\frac{1}{x}$
>>>latex(Integral(x**2, x))
$\int x^{2}\,dx$
```

MathML

```python
>>>from sympy.printing.mathml import mathml
>>>from sympy import Integral, latex
>>>from sympy.abc import x
>>>print mathml(x**2)
<apply><power/><ci>x</ci><cn>2</cn></apply>
>>>print mathml(1/x)
<apply><power/><ci>x</ci><cn>-1</cn></apply>
```

Pyglet

```python
>>>from sympy import Integral, preview
>>>from sympy.abc import x
>>>preview(Integral(x**2, x)) #doctest:+SKIP
```

##### 注解

sympy默认调用pprint，所以这就是为什么看到pretty printing为默认的。

有一个打印的有效模块，sympy.printing。用这个模块实现其他的打印：

- pretty(expr), pretty_print(expr), pprint(expr): 分别返回或者输出，，表达式的漂亮描述。这是相同
- latex(expr), print_latex(expr):分别返回或者输出，LaTex描写的表达式
- mathml(expr), print_mathml(expr):分别返回或者输出，MathML描写的表达式
- print_gtk(expr): 表达式打印到Gtkmathview , 这是一个GTK小配件显示MathML代码。Gtkmathview程序是必须的。

 sympy是一个Python的科学计算库，用一套强大的符号计算体系完成诸如多项式求值、求极限、解方程、求积分、微分方程、级数展开、矩阵运算等等计算问题。虽然Matlab的类似科学计算能力也很强大，但是Python以其语法简单、易上手、异常丰富的三方库生态，个人认为可以更优雅地解决日常遇到的各种计算问题。

## 初等运算



### 求对数

```python
# 自然对数
In [10]: sympy.log(sympy.E)
Out[10]: 1

In [11]: sympy.log(sympy.E ** 3)
Out[11]: 3

# 以10为底1000的对数
In [12]: sympy.log(1000,10)
Out[12]: 3
```

### 求平方根

```python
In [13]: sympy.sqrt(4)
Out[13]: 2

In [14]: sympy.sqrt(-1)
Out[14]: I
```

### 求n次方根



```css
# 求8的3次方根
In [15]: sympy.root(8,3)
Out[15]: 2
```

### 求k次方



```undefined
In [21]: 2 ** 3
Out[21]: 8

In [22]: 16 ** (1/2)
Out[22]: 4.0
```

### 求阶乘



```css
In [35]:  sympy.factorial(4)
Out[35]: 24
```

### 求三角函数

以`sin`函数为例：



```cpp
In [86]: sympy.sin(sympy.pi)
Out[86]: 0

In [87]: sympy.sin(sympy.pi/2)
Out[87]: 1
```

# 表达式与表达式求值

sympy可以用一套符号系统来表示一个表达式，如函数、多项式等，并且可以进行求值，比如：



```bash
# 首先定义x为一个符号，表示一个变量
In [96]: x = sympy.Symbol('x')

In [97]: fx = 2*x + 1

# 可以看到fx是一个sympy.core.add.Add类型的对象，也就是一个表达式
In [98]: type(fx)
Out[98]: sympy.core.add.Add

# 用evalf函数，传入变量的值，对表达式进行求值
In [101]: fx.evalf(subs={x:2})
Out[101]: 5.00000000000000
```

还支持多元表达式：



```bash
In [102]: x,y = sympy.symbols('x y')

In [103]: f = 2 * x + y

# 以字典的形式传入多个变量的值
In [104]: f.evalf(subs = {x:1,y:2})
Out[104]: 4.00000000000000

# 如果只传入一个变量的值，则原本输出原来的表达式
In [105]: f.evalf(subs = {x:1})
Out[105]: 2.0*x + y
```

# 用sympy解简单方程（组）

使用`sympy.solve`函数解方程，该函数通常传入两个参数，第1个参数是方程的表达式（把方程所有的项移到等号的同一边形成的式子），第2个参数是方程中的未知数。函数的返回值是一个列表，代表方程的所有根（可能为复数根）。

## 解最简单的方程

比如下面我们来求两个方程：



```python
# 首先定义 `x`为一个符号，代表一个未知数
In [24]: x = sympy.Symbol('x')

# 解方程：x - 1 = 0
In [25]: sympy.solve(x - 1,x)
Out[25]: [1]

# 解方程：x ^ 2 - 1 = 0
In [26]: sympy.solve(x ** 2 - 1,x)
Out[26]: [-1, 1]

# 解方程：x ^ 2 + 1 = 0
In [27]: sympy.solve(x ** 2 + 1,x)
Out[27]: [-I, I]
```

## 把函数式赋给一个变量

有时候为了书写起来简洁，可以把一个函数式起个名字，比如：



```dart
In [30]: x = sympy.Symbol('x')

In [31]: f = x + 1

In [32]: sympy.solve(f,x)
Out[32]: [-1]
```

## 解方程组

比如要解这么个二元一次方程组：



![img](https:////upload-images.jianshu.io/upload_images/8819542-72c7beb45226ccf9.png?imageMogr2/auto-orient/strip|imageView2/2/w/157/format/webp)

代码如下：



```python
# 一次性定义多个符号
In [28]: x,y = sympy.symbols('x y')

In [29]: sympy.solve([x + y - 1,x - y -3],[x,y])
Out[29]: {x: 2, y: -1}
```

## 计算求和式

计算求和式可以使用`sympy.summation`函数，其函数原型为：`sympy.summation(f, *symbols, **kwargs)`。

话不多少，举个栗子，比如求下面这个求和式子的值：

![img](https:////upload-images.jianshu.io/upload_images/8819542-e779aa77893798bd.png?imageMogr2/auto-orient/strip|imageView2/2/w/114/format/webp)


 我们用初中的知识可以知道，这个式子的结果为：`5050 * 2 = 10100`



下面用代码来求：



```dart
In [37]: n = sympy.Symbol('n')

In [38]: sympy.summation(2 * n,(n,1,100))
Out[38]: 10100
```

可见结果是正确的。

如果`sympy.summation`函数无法计算出具体的结果，那么会返回求和表达式。

## 解带有求和式的方程

比如求这么一个方程：



![img](https:////upload-images.jianshu.io/upload_images/8819542-b7b391f37657a927.png?imageMogr2/auto-orient/strip|imageView2/2/w/232/format/webp)

代码如下：



```dart
In [43]: x = sympy.Symbol('x')

In [44]: i = sympy.Symbol('i',integer = True)

In [46]: f =  sympy.summation(x,(i,1,5)) + 10 * x - 15

In [47]: sympy.solve(f,x)
Out[47]: [1]
```

## 求极限

求极限用`sympy.limit`函数，其函数文档如下：



```csharp
Signature: sympy.limit(e, z, z0, dir='+')
Docstring:
Compute the limit of e(z) at the point z0.

z0 can be any expression, including oo and -oo.

For dir="+" (default) it calculates the limit from the right
(z->z0+) and for dir="-" the limit from the left (z->z0-).  For infinite
z0 (oo or -oo), the dir argument is determined from the direction
of the infinity (i.e., dir="-" for oo).
```

函数文档中已经说得很清楚了，下面用代码示例来求几个极限。

如果学过微积分，就会知道微积分中有3个重要的极限：



![img](https:////upload-images.jianshu.io/upload_images/8819542-184b70faf3c1275b.png?imageMogr2/auto-orient/strip|imageView2/2/w/171/format/webp)



![img](https:////upload-images.jianshu.io/upload_images/8819542-ee5d3990a0dc59ae.png?imageMogr2/auto-orient/strip|imageView2/2/w/220/format/webp)



![img](https:////upload-images.jianshu.io/upload_images/8819542-feb0fef92aa4cd0b.png?imageMogr2/auto-orient/strip|imageView2/2/w/224/format/webp)

下面就用`sympy.limit`函数来分别求这3个极限：



```cpp
In [53]: x = sympy.Symbol('x')

In [54]: f1 = sympy.sin(x)/x

In [55]: sympy.limit(f1,x,0)
Out[55]: 1

In [56]: f2 = (1+x)**(1/x)

In [57]: sympy.limit(f2,x,0)
Out[57]: E

In [58]: f3 = (1+1/x)**x

In [59]: sympy.limit(f3,x,sympy.oo)
Out[59]: E
```

可见三个极限的计算结果都完全正确。

## 求导

求导使用`sympy.diff`函数，传入2个参数：函数表达式和变量名，举例如下：



```cpp
In [63]: x = sympy.Symbol('x')

In [64]: f = x ** 2 + 2 * x + 1

In [65]: sympy.diff(f,x)
Out[65]: 2*x + 2

In [66]: f2 = sympy.sin(x)

In [67]: sympy.diff(f2,x)
Out[67]: cos(x)

# 多元函数求偏导
In [68]: y = sympy.Symbol('y')

In [70]: f3 = x**2 + 2*x + y**3

In [71]: sympy.diff(f3,x)
Out[71]: 2*x + 2

In [72]: sympy.diff(f3,y)
Out[72]: 3*y**2
```

## 求定积分

使用`sympy.integrate`函数求定积分，其功能比较复杂，非常强大，下面仅仅举几个比较简单的例子。

先来求一个最简单的积分：

![img](https:////upload-images.jianshu.io/upload_images/8819542-aabc41f9bfe28f1d.png?imageMogr2/auto-orient/strip|imageView2/2/w/121/format/webp)


 用`牛顿-莱布尼兹公式`可以立马口算出上面这个式子的结果是1，用代码计算如下：





```bash
n [74]: x = sympy.Symbol('x')

n [75]: f = 2 * x

# 传入函数表达式和积分变量、积分下限、上限
n [76]: sympy.integrate(f,(x,0,1))
ut[76]: 1
```

下面来算一个复杂一点的多重积分：



![img](https:////upload-images.jianshu.io/upload_images/8819542-fed1bbd18cde1427.png?imageMogr2/auto-orient/strip|imageView2/2/w/138/format/webp)



其中：



![img](https:////upload-images.jianshu.io/upload_images/8819542-7de76f6e53c71ec7.png?imageMogr2/auto-orient/strip|imageView2/2/w/208/format/webp)

我们通过口算可以求出`f(x)`：

![img](https:////upload-images.jianshu.io/upload_images/8819542-95c54a9c5647a7ca.png?imageMogr2/auto-orient/strip|imageView2/2/w/280/format/webp)



所以：



![img](https:////upload-images.jianshu.io/upload_images/8819542-77ea58537b677f66.png?imageMogr2/auto-orient/strip|imageView2/2/w/460/format/webp)

下面用代码来计算上述过程：



```python
In [82]: t,x = sympy.symbols('t x')

In [83]: f = 2 * t

In [84]: g = sympy.integrate(f,(t,0,x))

In [85]: sympy.integrate(g,(x,0,3))
Out[85]: 9
```

## 求不定积分

同样也是使用`sympy.integrate`函数求不定积分，下面仅仅举几个比较简单的例子。

比如求下面这个不定积分：



![img](https:////upload-images.jianshu.io/upload_images/8819542-cd7eb2ff2d91a49e.png?imageMogr2/auto-orient/strip|imageView2/2/w/199/format/webp)

通过观察我们知道它的结果是：



![img](https:////upload-images.jianshu.io/upload_images/8819542-b1268da5b014caed.png?imageMogr2/auto-orient/strip|imageView2/2/w/109/format/webp)

下面用代码来计算这个不定积分的结果：



```cpp
In [79]: x = sympy.Symbol('x')

In [80]: f = sympy.E ** x + 2 * x

In [81]: sympy.integrate(f,x)
Out[81]: x**2 + exp(x)
```

## 使用 Python 解数学方程

#### 解二元一次方程功能实现

解方程的功能主要是使用Sympy中solve函数实现。

示例题目是：

#### 符号表示

方程中的符号

```text
from sympy import *
x = Symbol('x')
y = Symbol('y')
```

或者

```text
from sympy import *
x, y = symbols('x y')
```

第二个用空格隔开，下面代码中用x，y。括号里面的其实可以随意定义，因为是显示用。 比如：

```text
x = Symbol('x1')
```

但考虑到易读性还是相同比较好。

#### 方程表示

代码表示与手写还是有区别的，下面列出常用的：

- 加号 +
- 减号 -
- 除号 /
- 乘号 *
- 指数 **
- 对数 log()
- e的指数次幂 exp()

对于长的表达式，如果不确定，就加小括号

题目中表达式可表示为：

```text
2 * x - y - 3 = 0
3 * x + y - 7 = 0
```

由于需要将表达式都转化成右端等于0,这里把常数3和7移到等式左边。

#### 利用solve函数解方程

在解决例子之前，我们先解决一个一元一次的方程。

```text
x * 2 - 4 = 0
```

虽然很容易口算出来，我们还是要用solve函数

```text
print solve(x * 2 - 4, x)
#result
#[2]
```

solve：第一个参数为要解的方程，要求右端等于0，第二个参数为要解的未知数。还有一些 其他的参数，想了解的可以去看官方文档。

下面进行例题求解：

```text
solve([2 * x - y - 3, 3 * x + y - 7],[x, y])
```

完整代码为：

```text
from sympy import *
x = Symbol('x')
y = Symbol('y')
print solve([2 * x - y - 3, 3 * x + y - 7],[x, y])
```

结果如下：

![img](https://pic1.zhimg.com/80/v2-ccd114b008ce738c98520db933e60000_720w.png)

麻麻，我跟正确答案一样哦~

![img](https://pic1.zhimg.com/80/v2-f355cd22eda6ffac0e5ffe998518f4f8_720w.png)

# 解矩阵方程

**Ax=b
A为系数矩阵，b为解集矩阵**

令B为A的增广矩阵

1、Ax=b无解的充要条件：r(A)+1=r(B)

2、Ax=b唯一解的充要条件：r(A)=r(B)=n

3、Ax=b无穷多解的充要条件：r(A)=r(B)＜n

求解的逻辑：
x=A-1b

```python
from sympy import *

p1 = Matrix([[1,2],[3,4]])
y = Matrix([[5],[9]])
print(p1**(-1)*y)
p2 = Matrix([[1,3,4],[2,3,4]])
print(p1**(-1)*p2)
p3 = Matrix([[1,0,3],[2,5,4],[3,4,5]])
p4 = Matrix([[1,3,4],[2,7,4],[6,5,8]])
print(p3**(-1)*p4)
12345678910
```

结果：

```python
Matrix([[-1], [3]])
Matrix([[0, -3, -4], [1/2, 3, 4]])
Matrix([[19/4, -3, 3], [-1/2, 1, -2/3], [-5/4, 2, 1/3]])
123
```

如果A不是可逆矩阵，那么矩阵方程无法进行求解
将会报错：

```python
sympy.matrices.common.NonSquareMatrixError
```

# TIP：

**不能将sympy库创建的符号数学表达式与仅计算值的正常函数混合(如数学库中的那些.如果您要创建符号表达式,则应始终使用sympy函数(sympy.exp, sympy.cos,sympy.log等)**

