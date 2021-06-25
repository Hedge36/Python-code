# 前言：读者注

> 书出版于2018年，因而其涉及的一些算法相对落后一些，其次，本书仅涉及简单的实践案例，并且在多种监督学习算法中，主要介绍了SVM算法，涉及面较窄。



# 第一章 概论

## 分类

### 学习方式

> （1）**监督学习**（有导师学习）：输入数据中有导师信号，以概率函数、代数函数或人工神经网络为基函数模型，采用迭代计算方法，学习结果为函数。
>
> （2）**无监督学习**（无导师学习）：输入数据中无导师信号，采用聚类方法，学习结果为类别。典型的无导师学习有发现学习、聚类、竞争学习等。
>
> （3）**强化学习**（增强学习）：以环境反惯（奖/惩信号）作为输入，以统计和动态规划技术为指导的一种学习方法。



### 基本步骤

> 1. 定义问题
> 2. 数据理解
> 3. 数据准备
> 4. 评估算法
> 5. 优化模型
> 6. 结果部署
>



### 常用算法

> - 线性回归（LR）
> - 线性判别分析（LDA）
> - K邻近（KNN）
> - 分类与回归树（CART）
> - 贝叶斯分类器（NB）
> - 支持向量机（SVM）
>

# 第二章 数据处理

## 1. 数据导入

> There are 3 ways to load data which are usually deposited in `.csv` , by **csv**, **numpy** and **pandas**, with pandas commended. 
>



## 2. 数据理解

对数据的简单审视，是加强对数据理解最有效的方式之一。

维度：shape属性

类型：dtypes属性

描述性统级：describe方法

分组分布：groupby('colname').size方法

相关性：corr方法

分布分析：skew方法（高斯偏离）



## 3. 数据可视化

> 为了生成最优化的算法模型，必须对数据进行理解。最快、最有效的方式就是通过数据的可视化来加强对数据的理解。

### 3.1单一图表

常用的单一图表包括直方图、密度图、箱线图

#### 3.1.1直方图

> 直方图又称质量分布图，是一种统计图表，由一系列高度不等的纵向条纹或线段表示数据的分布情况。一般用横轴表示数据类型，纵轴表示分布情况。直方图可以非常直观地**展示每个属性的分布情况**。通过图表可以直观地看到数据是高斯分布、指数分布还是偏态分布。

```python
names = ['preg', 'plas', 'pres', 'skin',
 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv('pima_data.csv', names=names)
data.hist()
plt.tight_layout()
plt.show()
```

输出结果：

![Hist](E:\工具\Typora\Temp\Hist.png)

---

#### 3.1.2 密度图

> 密度图是一种**表现与数据值对应的边界或域对象**的图形表示方法，一般用于呈现连续变量。密度图类似于对直方图进行抽象，用平滑的线来描述数据的分布。

```python
names = ['preg', 'plas', 'pres', 'skin',
 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv('pima_data.csv', names=names)
data.plot(kind='density', subplots=True, layout=(3, 3), sharex=False)
plt.tight_layout()
plt.show()
```

输出：

![Dens](E:\工具\Typora\Temp\Dens.png)

---

#### 3.1.3 箱线图

> 箱线图又称盒须图、盒式图或箱形图，是一种用于**显示数据分散情况**的统计图。因形状如盒子而得名，在各种领域都被经常使用。箱线图也是一种非常好的用于显示数据分布情况的手段。首先画一条中位数线，然后以下四分位数和上四分位数画一个盒子，上下各有一条横线，表示上下边缘，通过横线来显示数据的伸展情况，游离在边缘之外的点为异常值。

```python
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin',
 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
data.plot(kind='box', subplots=True, layout=(3, 3), sharex=False)
plt.tight_layout()
plt.show()
```

输出结果：

![Box](E:\工具\Typora\Temp\Box.png)



### 3.2 多重图表

> 相关矩阵图与散点矩阵图用来显示不同属性之间的关联。

#### 3.2.1 相关矩阵图

> 相关矩阵图主要用来展示两个不同属性相互影响的程度。如果两个属性按照相同的方向变化，说明是正向影响。如果两个属性朝相反方向变化，说明是反向影响。把所有的属性两两影响的关系展示出来的图表就叫相关矩阵图。矩阵图法就是从多为问题的事件中找出成对的因素，排列成矩阵图，然后根据矩阵图来分析问题，确定关键点。

```python
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin',
 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
correlations = data.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0, 9, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
plt.tight_layout()
plt.show()
```

输出：![Correlation Matrix](E:\工具\Typora\Temp\Correlation Matrix.png)



#### 3.2.2. 散点矩阵图

> 散点矩阵图表示因变量随自变量变化的趋势，据此可以选择合适的函数对数据点进行拟合。散点矩阵图由两组数据构成多个坐标点，考察坐标点的分布，可以判断两个变量之间是否存在某种管理或者总结坐标点的分布模式。散点矩阵图将序列显示为一组点，值由点在图表中的位置表示，类别由图表中的不同标记表示。散点矩阵图通常用比较跨类别的聚合数据，利用散点矩阵图来绘制各个变量之间的散点图可以快速发现多个变量间的主要相关性，这在多元线性回归中显得十分重要。

```python
from pandas.plotting import scatter_matrix
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin',
 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
scatter_matrix(data, figsize=(9, 6))
plt.tight_layout()
plt.show()
```

![Scartter Matrix](E:\工具\Typora\Temp\Scartter Matrix.png)



## 4. 数据预处理

> 数据预处理需要根据数据本身的特征进行，有不同的格式和不同的要求，有缺失值的要填，有无效数据的要剔，有冗余维的要选，这些步骤都和数据本身的特性紧密相关。数据预处理大致分为三个步骤：**数据的准备、数据的转换、数据的输出**。数据处理是系统工程的基本环节，也是提高算法精确度的有效方式。因此本章将介绍以下几种数据转换方法：
>
> - **调整数据尺度(Rescale Data)**
> - **正态化数据(Standardize Data)**
> - **标准化数据(Normalize Data)**
> - **二值数据(Binarize Data)**

### 数据处理流程

> - 导入数据
> - 按照算法的输入和输出整理数据
> - 格式化输入数据
> - 总结显示数据的变化

其中，关于格式化数据，sklearn提供了两种方法：

- **适合和多重变换**
- 适合和变换组合

---

### 4.1 调整数据尺度(Rescale Data)

> 如果数据的各个属性按照不同的方式度量数据，那么通过调整数据的尺度让所有的属性按照相同的尺度来度量数据，就会给机器学习的算法模型训练带来极大的方便。这个方法通常会将数据的所有属性标准化，并将**数据转换成0和1之间的值**，这对梯度下降等算法是非常有用的。

方法代码如下：

```python
# 调整数据尺度（0..）
from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 
 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
scaler = MinMaxScaler(feature_range=(0, 1))
# 数据转换
rescaledX = scaler.fit_transform(X)
# 设定数据的打印格式
set_printoptions(precision=3)
print(rescaledX)
```

输出结果如下：

```python
[[0.353 0.744 0.59  ... 0.501 0.234 0.483]
 [0.059 0.427 0.541 ... 0.396 0.117 0.167]
 [0.471 0.92  0.525 ... 0.347 0.254 0.183]
 ...
 [0.294 0.608 0.59  ... 0.39  0.071 0.15 ]
 [0.059 0.633 0.492 ... 0.449 0.116 0.433]
 [0.059 0.467 0.574 ... 0.453 0.101 0.033]]
```



### 4.2 正态化数据(Standardize Data)

正态化数据是有效的处理符合高斯分布的数据的手段，**输出结果以0为中位数，1为方差，**并作为假定数据符合高斯分布的算法输入。这些算法有线性回归、逻辑回归和线性判别分析等。这里介绍StardarfScaler类来进行正态化数据处理，代码如下：

```python
# 正态化数据
from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import StandardScaler
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi',
 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
scaler = StandardScaler().fit(X)
# 数据转换
rescaledX = scaler.transform(X)
# 设定数据的打印格式
set_printoptions(precision=3)
print(rescaledX)
```

输出结果：

```python
[[ 0.64   0.848  0.15  ...  0.204  0.468  1.426]
 [-0.845 -1.123 -0.161 ... -0.684 -0.365 -0.191]
 [ 1.234  1.944 -0.264 ... -1.103  0.604 -0.106]
 ...
 [ 0.343  0.003  0.15  ... -0.735 -0.685 -0.276]
 [-0.845  0.16  -0.471 ... -0.24  -0.371  1.171]
 [-0.845 -0.873  0.046 ... -0.202 -0.474 -0.871]]
```



### 4.3 标准化数据(Normalize Data)

> 标准化数据处理是将每一行的数据的处理处理成1（在线性代数中矢量距离为1）的数据又叫做“归一元”处理，适合处理稀疏数据（具有很多为0的数），归一化处理的数据对使用权重输入的神经网络和使用距离的K邻近算法的准确度的提升有显著作用，此处使用NormalizeScaler实现，代码如下：

```python
# 标准化数据
from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import Normalizer
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi',
 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
scaler = Normalizer().fit(X)
# 数据转换
rescaledX = scaler.transform(X)
# 设定数据的打印格式
set_printoptions(precision=3)
print(rescaledX)
```

输出结果如下：

```python
[[0.034 0.828 0.403 ... 0.188 0.004 0.28 ]
 [0.008 0.716 0.556 ... 0.224 0.003 0.261]
 [0.04  0.924 0.323 ... 0.118 0.003 0.162]
 ...
 [0.027 0.651 0.388 ... 0.141 0.001 0.161]
 [0.007 0.838 0.399 ... 0.2   0.002 0.313]
 [0.008 0.736 0.554 ... 0.241 0.002 0.182]]
```



### 4.4 二值数据(Binarize Data)

> 二值数据是使用值将数据转化为二值，大于阈值设置为1，小于阈值设置为0.这个过程被称为二分数据或者阈值转换。在生成明确值或者特征工程增加属性的时候使用，下面通过Binarizer来实现这个功能，代码如下：

```PYTHON
# 二值数据
from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import Binarizer
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi',
 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
transform = Binarizer(threshold=0.0).fit(X)
# 数据转换
newX = transform.transform(X)
# 设定数据的打印格式
set_printoptions(precision=3)
print(newX)
```

输出结果：

```PYTHON
# 二值数据...
[[1. 1. 1. ... 1. 1. 1.]
 [1. 1. 1. ... 1. 1. 1.]
 [1. 1. 1. ... 1. 1. 1.]
 ...
 [1. 1. 1. ... 1. 1. 1.]
 [1. 1. 1. ... 1. 1. 1.]
 [1. 1. 1. ... 1. 1. 1.]]
```



## 5. 数据特征选定

正如业界内一句话所言，数据和特征决定了机器学习的上限，而模型和算法只是逼近这个上限而已。因此，特征过程的本质就是一项工程活动，目的是最大限度地从原始数据中提取合适的特征，以供算法和模型使用。特征处理时特征工程的核心部分，sklearn提供了较为完整的特征处理方法，包括数据预处理、特征选择、降维等。

本章节介绍以下四个数据特征提取办法：

- 单变量特征选定
- 递归特征消除
- 主要成分分析
- 特征的重要性

特征选定有助于降低数据的拟合度、提高算法的精度、减少训练时间。



### 5.1 单变量特征选定

统计分析可以用来分析选择对结果影响最大的数据特征。在sklearn中提供了SelectKBest类，可以使用一系列统计方法来选定数据特征，是对卡方检验的实现。

卡方检验就是统计样本的实际观测值与理论推断值之间的偏离程度，实际观测值与理论推断值之间的偏离程度就决定卡方值的大小，如果卡方值越大，二者偏差程度越大；反之，二者偏差越小；若两个值完全相等时，卡方值就为0，表明理论值完全符合。

```PYTHON
# 通过卡方检验选定数据特征
from pandas import read_csv
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi',
 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
# 特征选定
test = SelectKBest(score_func=chi2, k=4)
fit = test.fit(X, Y)
set_printoptions(precision=3)
print(fit.scores_)
features = fit.transform(X)
print(features)
```



### 5.2 递归特征消除(RFE)

递归特征消除(Recursive feature elimination)的主要思想是反复构建模型，然后选出最好的（或者最差的）特征（根据系数来选），把选出来的特征放到一边，然后在剩余的特征上重复这个过程，直到遍历了所有的特征。在这个过程中被消除的次序就是特征的排序。

RFE的稳定性很大程度上取决于迭代时，底层用的哪种模型。比如RFE采用的是普通的回归（LR），没有经过正则化的回归是不稳定的，那么RFE就是不稳定的。假如采用的是Lasso/ Ridge，正则化的回归是稳定的，那么RFE就是稳定的。代码如下：

```PYTHON
# 通过递归消除来选定特征
from pandas import read_csv
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi',
 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
# 特征选定
model = LogisticRegression()
rfe = RFE(model, 3)
fit = rfe.fit(X, Y)
print("特征个数：")
print(fit.n_features_)
print("被选定的特征：")
print(fit.support_)
print("特征排名：")
print(fit.ranking_)
```

输出结果：

```PYTHON
特征个数：
3
被选定的特征：
[ True False False False False  True  True False]
特征排名：
[1 2 4 5 6 1 1 3]
```

从输出结果中我们可以看出RFE选定了preg、mass和pedi三个数据特征，他们在support\_中被标记为True，在ranking\_中被标记为1.



### 5.3 主要成分分析(PCA)

主要成分分析(PCA)是指使用线性代数来转换压缩数据，通常称为数据降维。常见的降维方法除此外还有线性判别分析(LDA)，它本身也是一个分类器。详细内容参考文档，使用代码如下：

```PYTHON
# 通过主要成分分析选定数据特征
from pandas import read_csv
from sklearn.decomposition import PCA
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi',
 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
# 特征选定
pca = PCA(n_components=3)
fit = pca.fit(X)
print("解释方差：%s" % fit.explained_variance_ratio_)
print(fit.components_)
```

输出结果：

```PYTHON
解释方差：
[0.88854663 0.06159078 0.02579012]
[[-2.02176587e-03  9.78115765e-02  1.60930503e-02  6.07566861e-02
   9.93110844e-01  1.40108085e-02  5.37167919e-04 -3.56474430e-03]
 [-2.26488861e-02 -9.72210040e-01 -1.41909330e-01  5.78614699e-02
   9.46266913e-02 -4.69729766e-02 -8.16804621e-04 -1.40168181e-01]
 [-2.24649003e-02  1.43428710e-01 -9.22467192e-01 -3.07013055e-01
   2.09773019e-02 -1.32444542e-01 -6.39983017e-04 -1.25454310e-01]]
```



### 5.4 特征重要性

袋装决策树算法(Bagged Decision Tress)、随机森林算法和极端随机树算法都可以用来计算数据特征的重要性。这三个集成算法中的袋装算法，在后面的集成算法章节会有详细介绍，此处给出一个例子，代码如下：

```PYTHON
# 通过决策树计算特征的重要性
from pandas import read_csv
from sklearn.ensemble import ExtraTreesClassifier
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi',
 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
# 特征选定
model = ExtraTreesClassifier()
fit = model.fit(X, Y)
print(fit.feature_importances_)
```

输出结果：

```PYTHON
[0.10748569 0.2309971  0.10288295 0.08090733 0.07410529 0.1434772
 0.11832026 0.14182416]
```





# 第三章 算法评估

## 1. 算法评估

> 要知道算法模型对未知的数据表现如何，最好的评估办法是利用已经明确知道结果的数据运行生成的算法模型进行验证。此外，还可以采用重新采样评估的方法，使用新的数据来评估算法模型。

### 1.1 评估算法的方法

> 评估就是评估算法在预测新数据的时候能达到什么程度，但这不是对算法准确度的保证。当评估完算法模型之后，可以用整个数据集重新训练算法，生成最终的算法模型，下面提供四种方法：
>
> - 分离训练数据集和评估数据集
> - K折交叉验证分离
> - 弃一交叉验证分离
> - 重复随机评估、训练数据集分离

### 1.2 分离训练数据集和评估数据集

最简单的方法就是将评估数据集和训练数据集完全开，采用评估数据来评估算法模型。可以简单地把数据分为两部分，67%的数据用作训练集，33%的数据集作为评估数据集，下面提供一种算法进行2：1数据分离。

```PYTHON
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi',
 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
test_size = 0.33
seed = 4
X_train, X_test, Y_traing, Y_test = 
train_test_split(X, Y,test_size=test_size, random_state=seed)
model = LogisticRegression()
model.fit(X_train, Y_traing)
result = model.score(X_test, Y_test)
print("算法评估结果：%.3f%%" % (result * 100))
```

输出结果：

```PYTHON
算法评估结果：80.315%
```

**Tip：若出现如下警告，修改代码如下：**

```PYTHON
ConvergenceWarning: lbfgs failed to converge (status=1):
STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.
Increase the number of iterations (max_iter) or scale the data as shown in:
https://scikit-learn.org/stable/modules/preprocessing.html
Please also refer to the documentation for alternative solver options:
https://scikit-learn.org/stable/modules/linear_model.html
#logistic-regression
```

```PYTHON
model = LogisticRegression() 
# 改为如下代码，增加迭代次数上限--> 
model = LogisticRegression(max_iter=3000)
```



### 1.3 K折交叉验证分离

> 所谓K折交叉验证，就是将数据集划分成K份（一般是均分），将每个子集数据分别做一次验证集，其他的K-1份数据作为训练集，这样会得到K个模型，再用这K个模型最终的验证集的分类准确度的平均数，作为K折验证下分类器的性能指标。K一般大于或等于2，实际操作时往往从3开始取，只有数据集和数据量较小时才会取2。K折交叉验证可以有效避免过学习和欠学习状态的发生，最后得到的结果也比较有说服力。通常情况下，K的取值为3、5、10，执行结果中输出了评估的得分以及标准方差。

代码如下：

```PYTHON
from pandas import read_csv
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi',
 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
n_splits = 10
test_size = 0.33
seed = 7
kfold = ShuffleSplit(n_splits=n_splits, test_size=test_size,
 random_state=seed)
model = LogisticRegression(max_iter=3000)	
result = cross_val_score(model, X, Y, cv=kfold)
print("算法评估结果：%.3f%% (%.3f%%)" % (result.mean() * 100,
  result.std() * 100))
```

输出结果：

```PYTHON
算法评估结果：77.047% (2.784%)
```



### 1.4 弃一法交叉验证

> 又称留一法交叉验证，假设样本数据集中有N个样本数据。将每个样本单独作为测试集，其余N-1个样本作为训练集，这样得到了N个分类器或模型，用这N个分类器或模型的分类准确率的平均数作为此分类器的性能指标。相比于K折交叉验证，弃一法交叉验证有如下特点：
>
> 优点：
>
> 1. 每一个分类器或模型都是用几乎所有的样本来训练模型，最接近样本，这样评估所得的结果比较可靠。
> 2. 实验没有随机因素，整个过程是可重复的。
>
> 缺点：
>
> 计算成本高，当N非常大时，计算耗时。

代码如下：

```PYTHON
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin',
 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True)
model = LogisticRegression()
result = cross_val_score(model, X, Y, cv=kfold)
print("算法评估结果：%.3f%% (%.3f%%)" % (result.mean() * 100, 
  result.std() * 100))
```

输出结果如下：

```PYTHON
算法评估结果：77.734% (4.605%)
```



### 1.5 重复随机分离

重复随机分离评估，训练数据集分离。随机分离数据为训练数据集和评估数据集，重复这个过程多次，如同交叉验证分离。

代码如下：

```PYTHON
from pandas import read_csv
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin',
 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
n_splits = 10
test_size = 0.33
seed = 7
kfold = ShuffleSplit(n_splits=n_splits, test_size=test_size, 
 random_state=seed)
model = LogisticRegression(max_iter=3000)
result = cross_val_score(model, X, Y, cv=kfold)
print("算法评估结果：%.3f%% (%.3f%%)" % (result.mean() * 100,
  result.std() * 100))
```

输出结果：

```PYTHON
算法评估结果：76.535% (2.235%)
```



## 2. 算法评估矩阵

> 如何来评估机器学习的算法模型时非常重要的。选择能够展示机器学习算法模型的准确度的评估矩阵，是计算和比较算法模型最好的方式。并且在评估算法时，计算并比较这些评估矩阵，可以快速地选择合适的算法。
>
> 在这里，分类算法矩阵以逻辑回归为例，回归算法矩阵以线性回归为例，使用实际应用中最常采用的10折交叉验证来分类数据，并计算展示算法的评估矩阵。

### 2.1 分类算法矩阵

> 分类问题或许是最常见的机器学习问题，并且有多种评估矩阵来评估分类算法。如以下几种：
>    1. 分类准确度
>    2. 对数损失函数
>    3. AUC图
>    4. 混淆矩阵
>    5. 分类报告

#### 2.1.1 分类准确度

> 分类准确度就是算法自动分类正确的样本数除以所有的样本数得出的结果。通常，准确度越高，分类器越好。这是分类算法中最常见的，也最易被误用的评估参数。准确度确实是一个很好，很直观的评价指标，但是有时候准确度高并不代表算法一定好，比如因为数据分布不均衡，类别1的数据太少，完全错分类别1依然可以达到很高的准确度，却忽视了需要关注的事实和现象。

```PYTHON
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin',
 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True)
model = LogisticRegression()
result = cross_val_score(model, X, Y, cv=kfold)
print("算法评估结果准确度：%.3f (%.3f%%)" % (result.mean(), result.std()))
```

输出结果：

```PYTHON
算法评估结果准确度：0.777(0.046%)
```



#### 2.1.2 对数损失函数

> 在逻辑回归的推导中，它假设样本服从伯努利分布（0~1分布），然后求得满足该分布的似然函数，再取对数，求极值等。而逻辑回归并没有求似然函数的极值，而是把极大化当作一种思想，进而推导出它的经验风险函数为：最小化负的似然函数。从损失函数的视角来看，它就成了对数损失函数了。对数损失函数越小，模型就越好，而且使损失函数尽量是一个凸函数，便于收敛计算。代码如下：

```PYTHON
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi',
 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True)
model = LogisticRegression()
scoring = 'neg_log_loss'
result = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print('Logloss %.3f (%.3f)' % (result.mean(), result.std()))
```

输出结果：

```PYTHON
Logloss -0.495 (0.060)
```



#### 2.1.3 AUC图

> ROC和AUC是评价分类器的指标。ROC是受试者工作特征曲线的简写，又称为感受性曲线。得此名在于曲线上各点反映相同的感受性，它们都是对同一信号刺激的反应，只不过是在几种不同的判定标准下所得的结果而已。ROC纵轴是“真正例率”，横轴是“假正例率”。AUC是处于ROC下方的那部分面积大小。通常，AUC的值介于0.5和1之间，AUC的值越大，诊断准确性越高。在ROC曲线上，靠近坐标图左上方的点为敏感性和特异性均较高的临界值。

```PYTHON
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin',
 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True)
model = LogisticRegression()
scoring = 'roc_auc'
result = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print('AUC %.3f (%.3f)' % (result.mean(), result.std()))
```

输出结果：

```PYTHON
AUC 0.824 (0.052)
```



#### 2.1.4 混淆矩阵

> 混淆矩阵主要用于比较分类结果和实际测得值，可以把分类结果的精度显示在一个混淆矩阵里面。混淆矩阵是可视化工具，特别适用于监督学习，在无监督学习时一般叫做匹配矩阵。混淆矩阵的每列代表预测类别，每列的总数表示预测为该类别的数据的数目；每行代表数据的真实归属类别，每行的数据总数表示该类别的数据的数目。每列中的数值表示真实数据被预测为该类的数目。

```PYTHON
from pandas import read_csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi',
 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
test_size = 0.33
seed = 4
X_train, X_test, Y_traing, Y_test = train_test_split(X, Y, 
  											test_size=test_size, random_state=seed)
model = LogisticRegression()
model.fit(X_train, Y_traing)
predicted = model.predict(X_test)
matrix = confusion_matrix(Y_test, predicted)
classes = ['0', '1']
dataframe = pd.DataFrame(data=matrix,
 index=classes,
 columns=classes)
print(dataframe)
```

输出结果：

```PYTHON
 		01		
0  150  21	
1   29  54
```

意为原始数据分为两类，类0和类1，类0共有171个数据，150个类0数据被预测为类0，21被预测为类1。

#### 2.1.5 分类报告

> Classification_report()方法能够给出精确率，召回率，F1值和样本数目。

代码如下：

```PYTHON
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi',
 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
test_size = 0.33
seed = 4
X_train, X_test, Y_traing, Y_test = train_test_split(X, Y,
  test_size=test_size, random_state=seed)
model = LogisticRegression()
model.fit(X_train, Y_traing)
predicted = model.predict(X_test)
report = classification_report(Y_test, predicted)
print(report)
```

输出结果如下：

```
  precisionrecall  f1-score   support
 0.0   0.84  0.88  0.86   171
 1.0   0.72  0.65  0.6883
accuracy   0.80   254
   macro avg   0.78  0.76  0.77   254
weighted avg   0.80  0.80  0.80   254
```



### 2.2 回归算法矩阵

> 三种评估机器学习的回归算法的评估矩阵：
>
> 1. 平方绝对误差（MAE） 
> 2. 均方误差（MSE）
> 3. 决定系数（R2）



#### 2.2.1 平方绝对误差（MAE)

> 平方绝对误差是所有单个观测值与算术平均值的偏差的绝对值的平均值。与平均误差相比，平均绝对误差由于离差被绝对值化，不会出现正负相抵消的情况，因而，平均绝对误差能更好地反映预测值误差的实际情况。

代码如下：

```PYTHON
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
# 导入数据
filename = 'housing.csv'
names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
 'RAD', 'TAX', 'PRTATIO', 'B', 'LSTAT', 'MEDV']
data = read_csv(filename, names=names, delim_whitespace=True)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:13]
Y = array[:, 13]
n_splits = 10
seed = 7
kfold = KFold(n_splits=n_splits, random_state=seed, shuffle=True)
model = LinearRegression()
scoring = 'neg_mean_absolute_error'
result = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print('MAE: %.3f (%.3f)' % (result.mean(), result.std()))
```

输出结果如下：

```PYTHON
MAE: -3.387 (0.667)
```



#### 2.2.2 均方误差(MSE)

均方误差是衡量平均误差的方法，可以评价数据的变化程度。均方根误差是均方误差的算数平方根。均方误差的值越小，说明用该预测模型描述实验数据的准确度越高。

代码如下：

```PYTHON
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
# 导入数据
filename = 'housing.csv'
names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
 'RAD', 'TAX', 'PRTATIO', 'B', 'LSTAT', 'MEDV']
data = read_csv(filename, names=names, delim_whitespace=True)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:13]
Y = array[:, 13]
n_splits = 10
seed = 7
kfold = KFold(n_splits=n_splits, random_state=seed, shuffle=True)
model = LinearRegression()
scoring = 'neg_mean_squared_error'
result = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print('MSE: %.3f (%.3f)' % (result.mean(), result.std()))
```

输出结果如下：

```PYTHON
MSE: -23.747 (11.143)
```



#### 2.2.3 决定系数(R^2^)

> 决定系数，反映因变量的全部变异能通过回归关系被自变量解释的比例。拟合优度越大，自变量对因变量的解释程度越高，自变量引起的变动占总变动的百分比越高，观察点在回归直线附近越密集。如决定系数为0.8，则表示回归关系可以解释因变量80%的变异。换句话说，如果我们能控制自变量不变，则因变量的变异程度会减少80%。

决定系数的特点：

  1. 决定系数是非负的统计量；
          2. 决定系数的取值范围为0~1之间
                  3. 决定系数是样本观测值的函数，是因随机抽样而变动的随机变量。为此，对决定系数的统计的可靠性也应该进行检验。
          4. R2的数值范围从0至1，表示目标变量的预测值和实际值之间的相关程度平方的百分比。一个模型的R2 值为0说明它完全无法预测目标变量；而一个R2 值为1的模型则可以对目标变量进行完美的预测。从0至1之间的数值，则表示该模型中目标变量中有百分之多少能够用特征来解释。_模型也可能出现负值的R2，这种情况下模型所做预测还不如直接计算目标变量的平均值。

代码如下：

```PYTHON
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
# 导入数据
filename = 'housing.csv'
names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
 'RAD', 'TAX', 'PRTATIO', 'B', 'LSTAT', 'MEDV']
data = read_csv(filename, names=names, delim_whitespace=True)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:13]
Y = array[:, 13]
n_splits = 10
seed = 7
kfold = KFold(n_splits=n_splits, random_state=seed, shuffle=True)
model = LinearRegression()
scoring = 'r2'
result = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print('R2: %.3f (%.3f)' % (result.mean(), result.std()))
```

输出结果如下：

```PYTHON
R2: 0.718 (0.099)
```



# 第四章 算法审查

> 算法审查是选择合适的机器学习的主要方法之一。审查算法前并不知道哪个算法对问题最有效，必须设计一定的实验进行验证，以找到对问题最有效的算法，这个过程被叫做算法审查。

## 1. 审查分类算法

> 在选择算法时，应该换一种思路，不是针对数据应该采用哪种算法，而是应该用数据来审查哪些算法。应该先猜测一下，什么算法会具有最好的效果。这是训练数据敏感性的好方法。建议对同一个数据集运用不同的方法，来审查算法的有效性，然后找到最有效的算法。下面时审查算法的几点注意：

1. 尝试多种代表性算法
2. 尝试多种机器学习的算法
3. 尝试多种模型

### 1.1 算法概述

> 在分类算法中，目前存在很多类型的分类器：线性分类器，贝叶斯分类器，基于距离的分类器等。



### 1.2 线性算法

逻辑回归和线性判别分析都是假定输入的数据符合高斯分布。

#### 1.2.1 逻辑回归

> 回归是一种极易理解的模型，表明自变量x与因变量的关系。逻辑回归实际上是一个分类算法而不是回归算法，通常是利用已知的自变量来预测一个离散型因变量的值。简单来说，它就是通过拟合一个逻辑函数来预测一个事件发生的概率。所以它预测的是一个概率值，它的输出值应该为0~1，因此非常适合处理二分类问题。

代码如下：

```PYTHON
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin',
 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True)
model = LogisticRegression()
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean())
```

输出结果：

```PYTHON
0.777341079972659
```



#### 1.2.2 线性判别分析

> 线性判别分析的基本思想是将高维的模式样本投影到最佳鉴别矢量空间，以达到抽取分类信息和压缩特征空间维数的效果，投影后保证模式样本在新的子空间有最大的类间距离和最小的类内距离，即模式在该空间有最佳的可分离性。因此，它是一种有效的特征抽取方法。使用这种方法能够使投影后模式样本的类间散布矩阵最大，并且类内散步矩阵最小。就是说，它能保证投影后模式样本在新的空间中有最小的类内距离和最大的类间距离，即模式在该空间有最佳的可分离性。线性判别分析与主要成分分析一样，被广泛应用在数据降维中。

代码如下：

```PYTHON
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin',
 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True)
model = LinearDiscriminantAnalysis()
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean())
```

输出结果：

```PYTHON
0.7669685577580315
```



### 1.3 非线性算法

#### 1.3.1K近邻算法

> K近邻算法是一种理论上比较成熟的方法，也是最简单的机器学习方法之一。该方法的思路是：如果一个样本在特征空间中的K个最相似（特征空间中最邻近）的样本中的大多数属于某一个类别，则该样本也属于这个类别。在KNN中，通过计算对象间距离来做为各个对象之间的非相似性指标，避免了对象之间的匹配问题，距离一般使用欧式距离或者曼哈顿距离；同时，KNN通过依据k个对象中占优的类别进行决策，而不是通过单一的对象类别决策。这就是KNN算法的优势。

代码如下：

```PYTHON
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin',
 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True)
model = KNeighborsClassifier()
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean())
```

输出结果：

```PYTHON
0.7109876965140123
```



#### 1.3.2贝叶斯分类器

贝叶斯分类器的分类原理是通过某对象的先验概率，利用贝叶斯公式计算出其在所有类别上的后验概率，即该对象属于某一类的概率，选择具有最大后验概率的类作为该对象所属的类。也就是说，贝叶斯分类器是最小错误率意义上的优化。对于给出的待分类项，求解在此项出现的条件下各个类别出现的概率，哪个最大就认为待分类项属于哪个类别。贝叶斯分类器的特点如下：
1.贝叶斯分类器是一种基于统计的分类器，它根据给定样本属于某一个具体类的概率来对其进行分类
2.贝叶斯分类器的理论基础是贝叶斯理论
3.贝叶斯分类器的一种简单形式是朴素贝叶斯分类器，与随机森林，神经网络等分类器都具有可比的性能
4.贝叶斯分类器是一种增量型的分类器
在贝叶斯分类器中，对输入数据同样做了符合高斯分布的假设。

代码如下：

```PYTHON
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin',
 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True)
model = GaussianNB()
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean())
```

输出结果：

```PYTHON
0.7591421736158578
```



#### 1.3.3分类与回归树

分类与回归树CART回归树，树的构建基于基尼指数。CART假设决策树是二叉树，内部结点特征的取值为“是”和“否”，左分支是取值为“是”的分支，右分支是取值为”否“的分支。这样的决策树等价与递归二分每个特征，将输入空间（特征空间）划分为有限个单元，并在这些单元上确定预测的概率分布，也就是在输入给定的条件下输出的条件概率分布。CART算法由以下两步组成：
1.树的生成：基于训练数据集生成决策树，生成的决策树要尽量大
2.树的剪枝：用验证数据集对已生成的树进行剪枝，并选择最优子树，这时以损失函数最小作为剪枝的标准
决策树的生成就是通过递归构建二叉决策树的过程，对回归树用平方误差最小化准则，或对分类树用基尼指数最小化准则，进行特征选择，生成二叉树。

代码如下：

```PYTHON
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin',
 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True)
model = DecisionTreeClassifier()
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean())
```

输出结果：

```PYTHON
0.6889268626110732
```



#### 1.3.4支持向量机

支持向量机在解决小样本，非线性及高维模式识别中表现出了许多特有的优势，并能够推广应用到函数拟合等其他机器学习问题中。在机器学习中，支持向量机是与相关的学习算法有关的监督学习模型，可以分析数据，识别模式，用于分类和回归分析。

代码如下：

```PYTHON
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin',
 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True)
model = SVC()
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean())
```

输出结果：

```PYTHON
0.760457963089542
```



## 2. 审查回归算法

### 2.1算法概述

> 将审查七种回归算法
>
> a. 线性回归算法(线性)
>
> b. 岭回归算法(线性)
>
> c. Lasso回归算法(线性）
>
> d. 弹性网络回归算法（线性）
>
> e. K近邻算法（KNN）（非线性）
>
> f. CART（非线性）
>
> g. 支持向量机(SVM)

### 2.2 线性算法

#### 2.2.1 线性回归算法

> 线性回归算法是利用数理统计中的回归分析，来确定两种或两种以上变量之间相互依赖的定量关系的一种统计分析方法，运用十分广泛。在回归分析中，只包括一个自变量和一个因变量，且两者的关系可用一条直线近似表示，这种回归分析称为一元线性回归分析。如果回归分析中包括两个或两个以上的自变量，且因变量和自变量之间是线性关系。则称为多元线性回归分析。

代码如下：

```PYTHON
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
# 导入数据
filename = 'housing.csv'
names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
 'RAD', 'TAX', 'PRTATIO', 'B', 'LSTAT', 'MEDV']
data = read_csv(filename, names=names, delim_whitespace=True)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:13]
Y = array[:, 13]
n_splits = 10
seed = 7
kfold = KFold(n_splits=n_splits, random_state=seed, shuffle=True)
model = LinearRegression()
scoring = 'neg_mean_squared_error'
result = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print('Linear Regression: %.3f' % result.mean())
```

输出结果：

```PYTHON
Linear Regression: -23.747
```



#### 2.2.2 岭回归算法

岭回归算法是一种专门用于共线性数据分析的有偏估计回归方法，实际上是一种改良的最小二乘估计法，通过放弃最小二乘法的无偏性，以损失部分信息，降低精度为代价，获得回归系数更符合实际，更可靠的回归方法，对病态数据的拟合要强于最小二乘法。L2正则化回归

代码如下：

```PYTHON
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Ridge
# 导入数据
filename = 'housing.csv'
names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
 'RAD', 'TAX', 'PRTATIO', 'B', 'LSTAT', 'MEDV']
data = read_csv(filename, names=names, delim_whitespace=True)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:13]
Y = array[:, 13]
n_splits = 10
seed = 7
kfold = KFold(n_splits=n_splits, random_state=seed, shuffle=True)
model = Ridge()
scoring = 'neg_mean_squared_error'
result = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print('Ridge Regression: %.3f' % result.mean())
```

输出结果：

```PYTHON
Ridge Regression: -23.890
```



#### 2.2.3 LASSO回归算法

LASSO回归算法和岭回归算法类似，LASSO回归算法也会惩罚回归系数，在LASSO回归中会惩罚回归系数的绝对值大小。此外，它能够减少变化程度并提高线性回归模型的精度。LASSO回归算法和岭回归算法有一点不同，它使用的惩罚函数是绝对值，而不是平方。这导致惩罚值使一些参数估计结果等于零。使用惩罚值越大，进一步估计会使缩小值越趋近于零。这将导致我们要从给定的n个变量中选择变量。如果预测的一组变量高度相似，LASSO回归算法会选择其中的一个变量，并将其他的变量收缩为零。

代码如下：

```PYTHON
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Lasso
# 导入数据
filename = 'housing.csv'
names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
 'RAD', 'TAX', 'PRTATIO', 'B', 'LSTAT', 'MEDV']
data = read_csv(filename, names=names, delim_whitespace=True)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:13]
Y = array[:, 13]
n_splits = 10
seed = 7
kfold = KFold(n_splits=n_splits, random_state=seed, shuffle=True)
model = Lasso()
scoring = 'neg_mean_squared_error'
result = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print('Lasso Regression: %.3f' % result.mean())
```

输出结果：

```PYTHON
Lasso Regression: -28.746
```



#### 2.2.4 弹性网络回归算法

弹性网络回归算法是LASSO回归算法和岭回归算法的混合体，在模型训练时，弹性网络回归算法综合使用L1和L2两种正则化方法。当有多个相关的特征时，弹性网络回归算法时很有用的，LASSO回归算法会随机挑选算法中的一个，而弹性网络回归算法则会选择两个。与LASSO回归算法和岭回归算法相比，弹性回归算法的有点是，它允许弹性网络回归继承循环状态下岭回归的一些稳定性。另外，在高度相关变量的情况下，它会产生群体效应；选择变量的数目没有限制；可以承受双重收缩。

代码如下：

```PYTHON
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import ElasticNet
# 导入数据
filename = 'housing.csv'
names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
 'RAD', 'TAX', 'PRTATIO', 'B', 'LSTAT', 'MEDV']
data = read_csv(filename, names=names, delim_whitespace=True)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:13]
Y = array[:, 13]
n_splits = 10
seed = 7
kfold = KFold(n_splits=n_splits, random_state=seed, shuffle=True)
model = ElasticNet()
scoring = 'neg_mean_squared_error'
result = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print('ElasticNet Regression: %.3f' % result.mean())
```

输出结果：

```PYTHON
ElasticNet Regression: -27.908
```



### 2.3 非线性算法

#### 2.3.1 K近邻算法

K近邻算法是按照距离来预测结果。默认的距离参数为闵氏距离，可以指定曼哈顿距离作为距离的计算方式。

代码如下：

```PYTHON
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsRegressor
# 导入数据
filename = 'housing.csv'
names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
 'RAD', 'TAX', 'PRTATIO', 'B', 'LSTAT', 'MEDV']
data = read_csv(filename, names=names, delim_whitespace=True)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:13]
Y = array[:, 13]
n_splits = 10
seed = 7
kfold = KFold(n_splits=n_splits, random_state=seed, shuffle=True)
model = KNeighborsRegressor()
scoring = 'neg_mean_squared_error'
result = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print('KNeighbors Regression: %.3f' % result.mean())
```

输出结果：

```PYTHON
KNeighbors Regression: -38.852
```



#### 2.3.2 分类与回归树

上一章已经介绍过分类与回归树的算法，他同样适用于回归问题。

代码如下：

```PYTHON
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor
# 导入数据
filename = 'housing.csv'
names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
 'RAD', 'TAX', 'PRTATIO', 'B', 'LSTAT', 'MEDV']
data = read_csv(filename, names=names, delim_whitespace=True)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:13]
Y = array[:, 13]
n_splits = 10
seed = 7
kfold = KFold(n_splits=n_splits, random_state=seed, shuffle=True)
model = DecisionTreeRegressor()
scoring = 'neg_mean_squared_error'
result = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print('CART: %.3f' % result.mean())
```

输出结果：

```PYTHON
CART: -25.140
```



#### 2.3.3 支持向量机

上一章已经介绍过支持向量机的算法，他同样适用于回归问题。

代码如下：

```PYTHON
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVR
# 导入数据
filename = 'housing.csv'
names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
 'RAD', 'TAX', 'PRTATIO', 'B', 'LSTAT', 'MEDV']
data = read_csv(filename, names=names, delim_whitespace=True)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:13]
Y = array[:, 13]
n_splits = 10
seed = 7
kfold = KFold(n_splits=n_splits, random_state=seed, shuffle=True)
model = SVR()
scoring = 'neg_mean_squared_error'
result = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print('SVM: %.3f' % result.mean())
```

输出结果：

```PYTHON
SVM: -67.641
```



# 第五章 算法比较

> 机器学习算法太多了，分类、回归、聚类、推荐、图像识别领域等等，要想找到一个合适算法真的不容易，所以在实际应用中，我们一般都是采用启发式学习方式来实验。通常最开始我们都会选择大家普遍认同的算法，诸如SVM，GBDT，Adaboost，现在深度学习很火热，神经网络也是一个不错的选择。假如你在乎精度（accuracy）的话，最好的方法就是通过交叉验证（cross-validation）对各个算法一个个地进行测试，进行比较，然后调整参数确保每个算法达到最优解，最后选择最好的一个。但是如果你只是在寻找一个“足够好”的算法来解决你的问题，或者这里有些技巧可以参考，下面来分析下各个算法的优缺点，基于算法的优缺点，更易于我们去选择它。

**偏差&方差**

在统计学中，一个模型好坏，是根据偏差和方差来衡量的，所以我们先来普及一下偏差和方差：

- **偏差：**描述的是预测值（估计值）的期望E’与真实值Y之间的差距。偏差越大，越偏离真实数据。

- **方差：**描述的是预测值P的变化范围，离散程度，是预测值的方差，也就是离其期望值E的距离。方差越大，数据的分布越分散。

模型的真实误差是两者之和，

如果是小训练集，高偏差/低方差的分类器（例如，朴素贝叶斯NB）要比低偏差/高方差大分类的优势大（例如，KNN），因为后者会过拟合。但是，随着你训练集的增长，模型对于原数据的预测能力就越好，偏差就会降低，此时低偏差/高方差分类器就会渐渐的表现其优势（因为它们有较低的渐近误差），此时高偏差分类器此时已经不足以提供准确的模型了。

当然，你也可以认为这是生成模型（NB）与判别模型（KNN）的一个区别。

**为什么说朴素贝叶斯是高偏差低方差?**

以下内容引自知乎：

> 首先，假设你知道训练集和测试集的关系。简单来讲是我们要在训练集上学习一个模型，然后拿到测试集去用，效果好不好要根据测试集的错误率来衡量。但很多时候，我们只能假设测试集和训练集的是符合同一个数据分布的，但却拿不到真正的测试数据。这时候怎么在只看到训练错误率的情况下，去衡量测试错误率呢？ 由于训练样本很少（至少不足够多），所以通过训练集得到的模型，总不是真正正确的。（就算在训练集上正确率100%，也不能说明它刻画了真实的数据分布，要知道刻画真实的数据分布才是我们的目的，而不是只刻画训练集的有限的数据点）。而且，实际中，训练样本往往还有一定的噪音误差，所以如果太追求在训练集上的完美而采用一个很复杂的模型，会使得模型把训练集里面的误差都当成了真实的数据分布特征，从而得到错误的数据分布估计。这样的话，到了真正的测试集上就错的一塌糊涂了（这种现象叫过拟合）。但是也不能用太简单的模型，否则在数据分布比较复杂的时候，模型就不足以刻画数据分布了（体现为连在训练集上的错误率都很高，这种现象较欠拟合）。过拟合表明采用的模型比真实的数据分布更复杂，而欠拟合表示采用的模型比真实的数据分布要简单。 在统计学习框架下，大家刻画模型复杂度的时候，有这么个观点，认为Error = Bias + Variance。这里的Error大概可以理解为模型的预测错误率，是有两部分组成的，一部分是由于模型太简单而带来的估计不准确的部分（Bias），另一部分是由于模型太复杂而带来的更大的变化空间和不确定性（Variance）。 所以，这样就容易分析朴素贝叶斯了。它简单的假设了各个数据之间是无关的，是一个被**严重简化了的模型**。所以，对于这样一个简单模型，大部分场合都会Bias部分大于Variance部分，也就是说高偏差而低方差。 在实际中，为了让Error尽量小，我们在选择模型的时候需要平衡Bias和Variance所占的比例，也就是平衡over-fitting和under-fitting。

当模型复杂度上升的时候，偏差会逐渐变小，而方差会逐渐变大。

## 1. 常见算法优缺点

### 1.1 朴素贝叶斯

朴素贝叶斯属于生成式模型（关于生成模型和判别式模型，主要还是在于是否是要求联合分布），非常简单，你只是做了一堆计数。如果注有条件独立性假设（一个比较严格的条件），朴素贝叶斯分类器的收敛速度将快于判别模型，如逻辑回归，所以你只需要较少的训练数据即可。即使NB条件独立假设不成立，NB分类器在实践中仍然表现的很出色。它的主要缺点是它不能学习特征间的相互作用，用mRMR中R来讲，就是特征冗余。引用一个比较经典的例子，比如，虽然你喜欢Brad Pitt和Tom Cruise的电影，但是它不能学习出你不喜欢他们在一起演的电影。

**优点**：

- 朴素贝叶斯模型发源于古典数学理论，有着坚实的数学基础，以及稳定的分类效率。
- 对小规模的数据表现很好，能个处理多分类任务，适合增量式训练；
- 对缺失数据不太敏感，算法也比较简单，常用于文本分类。

**缺点**：

- 需要计算先验概率；
- 分类决策存在错误率；
- 对输入数据的表达形式很敏感。



### 1.2 Logistic Regression（逻辑回归）

属于判别式模型，有很多正则化模型的方法（L0， L1，L2，etc），而且你不必像在用朴素贝叶斯那样担心你的特征是否相关。与决策树与SVM机相比，你还会得到一个不错的概率解释，你甚至可以轻松地利用新数据来更新模型（使用在线梯度下降算法，online gradient descent）。如果你需要一个概率架构（比如，简单地调节分类阈值，指明不确定性，或者是要获得置信区间），或者你希望以后将更多的训练数据快速整合到模型中去，那么使用它吧。

**Sigmoid函数**：

**优点：**

- 实现简单，广泛的应用于工业问题上；
- 分类时计算量非常小，速度很快，存储资源低；
- 便利的观测样本概率分数；
- 对逻辑回归而言，多重共线性并不是问题，它可以结合L2正则化来解决该问题；

**缺点**：

- 当特征空间很大时，逻辑回归的性能不是很好；
- 容易**欠拟合**，一般准确度不太高
- 不能很好地处理大量多类特征或变量；
- 只能处理两分类问题（在此基础上衍生出来的softmax可以用于多分类），且必须**线性可分**；
- 对于非线性特征，需要进行转换；



### 1.3 线性回归

线性回归是用于回归的，而不像Logistic回归是用于分类，其基本思想是用**梯度下降法**对最小二乘法形式的误差函数进行优化，当然也可以用normal equation直接求得参数的解，结果为：

而在LWLR（局部加权线性回归）中，参数的计算表达式为:

由此可见LWLR与LR不同，LWLR是一个非参数模型，因为每次进行回归计算都要遍历训练样本至少一次。

**优点**： 实现简单，计算简单； **缺点**： 不能拟合非线性数据.

### 

### 

### 1.4 最近邻算法——KNN

KNN即最近邻算法，其主要过程为：

1. 计算训练样本和测试样本中每个样本点的距离（常见的距离度量有欧式距离，马氏距离等）； 2. 对上面所有的距离值进行排序；3. 选前k个最小距离的样本； 4. 根据这k个样本的标签进行投票，得到最后的分类类别。


如何选择一个最佳的K值，这取决于数据。一般情况下，在分类时较大的K值能够减小噪声的影响。但会使类别之间的界限变得模糊。一个较好的K值可通过各种启发式技术来获取，比如，交叉验证。另外噪声和非相关性特征向量的存在会使K近邻算法的准确性减小。

近邻算法具有较强的一致性结果。随着数据趋于无限，算法保证错误率不会超过贝叶斯算法错误率的两倍。对于一些好的K值，K近邻保证错误率不会超过贝叶斯理论误差率。

**KNN算法的优点**

- 理论成熟，思想简单，既可以用来做分类也可以用来做回归；
- 可用于非线性分类；
- 训练时间复杂度为O(n)；
- 对数据没有假设，准确度高，对outlier不敏感；

**缺点**

- 计算量大；
- 样本不平衡问题（即有些类别的样本数量很多，而其它样本的数量很少）；
- 需要大量的内存；



### 1.5 决策树

易于解释。它可以毫无压力地处理特征间的交互关系并且是非参数化的，因此你不必担心异常值或者数据是否线性可分（举个例子，决策树能轻松处理好类别A在某个特征维度x的末端，类别B在中间，然后类别A又出现在特征维度x前端的情况）。它的缺点之一就是不支持在线学习，于是在新样本到来后，决策树需要全部重建。另一个缺点就是容易出现过拟合，但这也就是诸如随机森林RF（或提升树boosted tree）之类的集成方法的切入点。另外，随机森林经常是很多分类问题的赢家（通常比支持向量机好上那么一丁点），它训练快速并且可调，同时你无须担心要像支持向量机那样调一大堆参数，所以在以前都一直很受欢迎。

决策树中很重要的一点就是选择一个属性进行分枝，因此要注意一下信息增益的计算公式，并深入理解它。

信息熵的计算公式如下:

其中的n代表有n个分类类别（比如假设是2类问题，那么n=2）。分别计算这2类样本在总样本中出现的概率p1和p2，这样就可以计算出未选中属性分枝前的信息熵。

现在选中一个属性$x_i$用来进行分枝，此时分枝规则是：如果$x_i=v$的话，将样本分到树的一个分支；如果不相等则进入另一个分支。很显然，分支中的样本很有可能包括2个类别，分别计算这2个分支的熵H1和H2,计算出分枝后的总信息熵H’ =p1 *H1+p2* H2,则此时的信息增益ΔH = H - H’。以信息增益为原则，把所有的属性都测试一边，选择一个使增益最大的属性作为本次分枝属性。

**决策树自身的优点**

- 计算简单，易于理解，可解释性强；
- 比较适合处理有缺失属性的样本；
- 能够处理不相关的特征；
- 在相对短的时间内能够对大型数据源做出可行且效果良好的结果。

**缺点**

- 容易发生过拟合（随机森林可以很大程度上减少过拟合）；
- 忽略了数据之间的相关性；
- 对于那些各类别样本数量不一致的数据，在决策树当中,信息增益的结果偏向于那些具有更多数值的特征（只要是使用了信息增益，都有这个缺点，如RF）。

### 1.7 Adaboosting

Adaboost是一种加和模型，每个模型都是基于上一次模型的错误率来建立的，过分关注分错的样本，而对正确分类的样本减少关注度，逐次迭代之后，可以得到一个相对较好的模型。是一种典型的boosting算法。下面是总结下它的优缺点。

**优点**

- adaboost是一种有很高精度的分类器。
- 可以使用各种方法构建子分类器，Adaboost算法提供的是框架。
- 当使用简单分类器时，计算出的结果是可以理解的，并且弱分类器的构造极其简单。
- 简单，不用做特征筛选。
- 不容易发生overfitting。

关于随机森林和GBDT等组合算法，参考这篇文章：机器学习-组合算法总结

**缺点：**对outlier比较敏感



### 1.8 SVM支持向量机

高准确率，为避免过拟合提供了很好的理论保证，而且就算数据在原特征空间线性不可分，只要给个合适的核函数，它就能运行得很好。在动辄超高维的文本分类问题中特别受欢迎。可惜内存消耗大，难以解释，运行和调参也有些烦人，而随机森林却刚好避开了这些缺点，比较实用。

**优点**

- 可以解决高维问题，即大型特征空间；
- 能够处理非线性特征的相互作用；
- 无需依赖整个数据；
- 可以提高泛化能力；

**缺点**

- 当观测样本很多时，效率并不是很高；
- 对非线性问题没有通用解决方案，有时候很难找到一个合适的核函数；
- 对缺失数据敏感；

对于核的选择也是有技巧的（libsvm中自带了四种核函数：线性核、多项式核、RBF以及sigmoid核）：

- 第一，如果样本数量小于特征数，那么就没必要选择非线性核，简单的使用线性核就可以了；
- 第二，如果样本数量大于特征数目，这时可以使用非线性核，将样本映射到更高维度，一般可以得到更好的结果；
- 第三，如果样本数目和特征数目相等，该情况可以使用非线性核，原理和第二种一样。

对于第一种情况，也可以先对数据进行降维，然后使用非线性核，这也是一种方法。

### 

### 1.9 人工神经网络的优缺点

**人工神经网络的优点：**

- 分类的准确度高；
- 并行分布处理能力强,分布存储及学习能力强，
- 对噪声神经有较强的鲁棒性和容错能力，能充分逼近复杂的非线性关系；
- 具备联想记忆的功能。

**人工神经网络的缺点：**

- 神经网络需要大量的参数，如网络拓扑结构、权值和阈值的初始值；
- 不能观察之间的学习过程，输出结果难以解释，会影响到结果的可信度和可接受程度；
- 学习时间过长,甚至可能达不到学习的目的。

### 

### 

### 1.10 K-Means聚类

关于K-Means聚类的文章，链接：机器学习算法-K-means聚类。关于K-Means的推导，里面有着很强大的EM思想。

**优点**

- 算法简单，容易实现 ；
- 对处理大数据集，该算法是相对可伸缩的和高效率的，因为它的复杂度大约是O(nkt)，其中n是所有对象的数目，k是簇的数目,t是迭代的次数。通常k<<n。这个算法通常局部收敛。
- 算法尝试找出使平方误差函数值最小的k个划分。当簇是密集的、球状或团状的，且簇与簇之间区别明显时，聚类效果较好。

**缺点**

- 对数据类型要求较高，适合数值型数据；
- 可能收敛到局部最小值，在大规模数据上收敛较慢
- K值比较难以选取；
- 对初值的簇心值敏感，对于不同的初始值，可能会导致不同的聚类结果；
- 不适合于发现非凸面形状的簇，或者大小差别很大的簇。
- 对于”噪声”和孤立点数据敏感，少量的该类数据能够对平均值产生极大影响。

## 2. 算法选择参考

之前翻译过一些国外的文章，有一篇文章中给出了一个简单的算法选择技巧：

1、首当其冲应该选择的就是逻辑回归，如果它的效果不怎么样，那么可以将它的结果作为基准来参考，在基础上与其他算法进行比较；

2、然后试试决策树（随机森林）看看是否可以大幅度提升你的模型性能。即便最后你并没有把它当做为最终模型，你也可以使用随机森林来移除噪声变量，做特征选择；

3、如果特征的数量和观测样本特别多，那么当资源和时间充足时（这个前提很重要），使用SVM不失为一种选择。

通常情况下：【GBDT>=SVM>=RF>=Adaboost>=Other…】，现在深度学习很热门，很多领域都用到，它是以神经网络为基础的，目前我自己也在学习，只是理论知识不是很厚实，理解的不够深，这里就不做介绍了。

算法固然重要，**但好的数据却要优于好的算法**，设计优良特征是大有裨益的。假如你有一个超大数据集，那么无论你使用哪种算法可能对分类性能都没太大影响（此时就可以根据速度和易用性来进行抉择）。



# 第六章 集成算法

集成算法有3个流派：Bagging（代表随机森林）、Boosting（代表AdaBoost，Xgboost）、Stacking模型

Bagging：训练多个分类器取平均（并行）

Boosting：从弱学习器开始加强，通过加权来进行训练（串行）

Stacking：聚合多个分类或回归模型（分阶段）

## 1. Bagging模型：随机森林

### 1.1 Bagging的原理

![img](E:\工具\Typora\Temp\b058ffa9d3c4effa16748e75c5a1e9b5.png)

Bagging的弱学习器之间的确没有boosting那样的联系。它的特点在“随机采样”。

随机采样(bootsrap)就是从我们的训练集里面采集固定个数的样本，但是每采集一个样本后，都将样本放回。也就是说，之前采集到的样本在放回后有可能继续被采集到。

bagging对于弱学习器没有限制，这和Adaboost一样。但是最常用的一般也是决策树和神经网络。

bagging的集合策略也比较简单，对于分类问题，通常使用简单投票法，得到最多票数的类别或者类别之一为最终的模型输出。对于回归问题，通常使用简单平均法，对T个弱学习器得到的回归结果进行算术平均得到最终的模型输出。

由于Bagging算法每次都进行采样来训练模型，因此泛化能力很强，对于降低模型的方差很有作用。当然对于训练集的拟合程度就会差一些，也就是模型的偏倚会大一些。

-----

### 1.2 随机森林算法 Random Forest

用一句话总结就是：随机采样构建不同的树，结果取平均

随机森林的主要优点有：

> 1）训练可以高度并行化，对于大数据时代的大样本训练速度有优势。个人觉得这是的最主要的优点。
>
> 2）由于可以随机选择决策树节点划分特征，这样在样本特征维度很高的时候，仍然能高效的训练模型。
>
> 3）在训练后，可以给出各个特征对于输出的重要性
>
> 4）由于采用了随机采样，训练出的模型的方差小，泛化能力强。
>
> 5）相对于Boosting系列的Adaboost和GBDT， RF实现比较简单。
>
> 6）对部分特征缺失不敏感。

随机森林的主要缺点有：

> 1）在某些噪音比较大的样本集上，RF模型容易陷入过拟合。
>
> 2) 取值划分比较多的特征容易对RF的决策产生更大的影响，从而影响拟合的模型的效果。

树模型：

![img](E:\工具\Typora\Temp\ec4b321bd61dfa888562188db1859696.png)

理论上越多的树效果会越好，但实际上基本超过一定数量就差不多上下浮动了

 

### 1.3 极限随机树 Extra Trees

计算分割点方法中的随机性进一步增强。 在随机森林中，使用的特征是候选特征的随机子集；不同于寻找最具有区分度的阈值， 这里的阈值是针对每个候选特征随机生成的，并且选择这些随机生成的阈值中的最佳者作为分割规则。 这种做法通常能够减少一点模型的方差，代价则是略微地增大偏差。

extra trees是RF的一个变种, 原理几乎和RF一模一样，仅有区别有：

1）对于每个决策树的训练集，RF采用的是随机采样bootstrap来选择采样集作为每个决策树的训练集，而extra trees一般不采用随机采样，即每个决策树采用原始训练集。

2）在选定了划分特征后，RF的决策树会基于基尼系数，均方差之类的原则，选择一个最优的特征值划分点，这和传统的决策树相同。但是extra trees比较的激进，他会随机的选择一个特征值来划分决策树。

从第二点可以看出，由于随机选择了特征值的划分点位，而不是最优点位，这样会导致生成的决策树的规模一般会大于RF所生成的决策树。也就是说，模型的方差相对于RF进一步减少，但是偏倚相对于RF进一步增大。在某些时候，extra trees的泛化能力比RF更好。

 

## 2. Boosting模型：Adaboost、XGBoost

###  2.1 Boosting模型

  Boosting(提升)是一族可将弱学习器提升为强学习器的算法。提升算法基于这样一种思想：对于一个复杂的任务，将多个专家的判断总和得出的结果要比任何一个专家单独的判断好。这族算法的工作机制类似：先从初始训练集训练出一个基学习器，再根据基学习器表现对训练样本分布进行调整，是的先前基学习器做错的样本在后续收到更多关注（赋予做错的样本更大的权值），然后基于调整后的样本分布来训练下一个基学习器，一直反复进行，直到达到指定值。
 Boosting方法通过分步迭代（stage-wise）的方式来构建模型，在迭代的每一步构建的弱学习器都是为了弥补已有模型的不足。（**个体学习器之间存在强依赖关系。**）

 

### 2.2 AdaBoost算法

AdaBoost算法是提升算法中最具代表性的。其中AdaBoost是Adaptive Boosting的缩写， 正如上面所说的，在AdaBoost算法中会提高前一轮分类器分类错误的样本的权值，而降低那些被分类正确样本的权值。对于弱分类器的组合，AdaBoost算法采取加权多数表决的方法。具体的说就是加大分类误差率小的弱分类器的权值，使其在表决中起到较大的作用；减小分类误差率大的弱分类器的权值，使其在表决中起较小的作用。

感性认识AdaBoost算法： 

> 1.算法开始前，需要将每个样本的权重初始化为1/m,这样一开始每个样本都是等概率的分布，每个分类器都会公正对待。 
>
> 2.开始迭代后，需要计算每个弱分类器的分类错误的误差，误差等于各个分错样本的权重和，这里就体现了样本权重的作用。如果一个分类器正确分类了一个权重大的样本，那么这个分类器的误差就会小，否则就会大。这样就对分类错误的样本更大的关注。 
>
> 3.获取最优分类器后，需要计算这个分类器的权重，然后再更新各个样本的权重，然后再归一化。 
>
> 4.算法迭代的次数一般不超过弱分类器的个数，如果弱分类器的个数非常之多，那么可以权衡自己性价比来折中选择。 
>
> 5.迭代完成后，最后的分类器是由迭代过程中选择的弱分类器线性加权得到的。

理性认识AdaBoost算法：

![img](E:\工具\Typora\Temp\a698591b8986ea5776a83640d68da173.png)

 

 

## 3. Stacking模型

作为一个在kaggle比赛中高分选手常用的技术，SG在部分情况下，甚至可以让错误率相比当前最好的方法进一步降低30%之多。

以下图为例：

- ① 将训练集分为几个部分，分别用于让几个基分类器（Base-leaner）进行学习和拟合（也可以让基分类器所有训练集）
- ② 将3个基分类器预测得到的结果作为下一层分类器（Meta-learner）的输入
- ③ 将下一层分类器得到的结果作为最终的预测结果

![img](E:\工具\Typora\Temp\ed7b26731e06e5742772bedddb7451fa.JPEG)

这个模型的特点就是通过使用第一阶段（level 0）的预测作为下一层预测的特征，比起相互独立的预测模型能够有**更强的非线性表述能力，降低泛化误差**。

#### 特点：

堆叠：很暴力，拿来一堆直接上（各种分类器都来了）集成算法，可以堆叠各种各样的分类器（KNN,SVM,RF等等）

分阶段：第一阶段得出各自结果，第二阶段再用前一阶段结果训练。



# 第七章 算法调参

模型有很多参数，如何找到最佳的参数组合？

调整参数何时为止：应该遵循偏差和方差协调的原则。

本章将介绍：

- 调整参数对机器学习的重要性
- 如何使用网格搜索优化参数
- 如何使用随机搜索优化参数

------

机器学习算法调参

调整算法参数是采用机器学习解决问题的最后一个步骤，有时也被称为超参数优化。

参数可以分为两种：一种是影响模型在训练集上的准确度或防止过拟合能力的参数；另一种是不影响这两者的参数。

模型在样本总体上的准确度由其在训练集上的准确度及其防止过拟合的能力共同决定，所以在调参时主要针对第一种参数进行调整，最终达到的效果是：模型在训练集上的准确度和防止过拟合能力的完美共处。

下面将介绍两种自动寻找最优化参数的算法：

- 网格搜索优化参数
- 随机搜索优化参数

## 网格搜索优化参数

 网格搜索优化参数是通过遍历已定义参数列表，来评估算法的参数，从而找到最优参数。

在scikit-learn中使用GridSearchCV来实现对参数的跟踪，调整与评估，从而找到最优参数。

网格搜索优化参数适用于三四个（或更少）的超参数（当超参数的数量增加时，网格搜索的计算复杂度会呈现指数型增长，这时要换用随机搜索），由用户列出一个较小的超参数值域，这些超参数值域的笛卡尔集（排列组合）为一组组超参数。

网格搜索算法使用每组超参数训练模型，并挑选验证集误差最小的超参数组合。

下面的例子是展示如何使用GridSearchCV来调整脊回归（Ridge）的参数。GridSearchCV使用字典对象来指定需要调参的参数，可以同时对一个或多个参数进行参数调整。

```python
#网格搜索优化参数
from pandas import read_csv
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

filename='/home/aistudio/work/pima_data1.csv'
names=['preg','plas','pres','skin','test','mass','pedi','age','class']
data=read_csv(filename,names=names)
#将数据分为输入数据和输出数据
array=data.values
x=array[:,0:8]
y=array[:,8]
#算法实例化
model=Ridge()
#设置要遍历的参数
param_grid={'alpha':[1,0.1,0.01,0.001,0]}

#通过网格搜索查询最优参数
grid=GridSearchCV(estimator=model,param_grid=param_grid)
grid.fit(x,y)
#搜索结果
print('最高得分：%.3f' % grid.best_score_)
print('最优参数: %s' % grid.best_estimator_.alpha)
```

param_grid是一个字典对象，以算法的参数名为key，需要遍历的参数值列表为value。在验证算法最优参数的网格搜索算法中，可以设定多个key：value对，同时查询多个参数的最优参数值。

执行结果：

```python
最高得分：0.280
最优参数: 1
```

------

## 随机搜索优化参数

通过固定次数的迭代，采用随机采样分布的方式搜索合适的参数。

与网格搜索优化相比，随机搜索提供了一种更高效的解决方法（特别是在参数数量多的情况下），随机搜索优化参数为每个参数定义了一个分布函数，并在该空间中采样。

在scikit-learn中通过RandomizedSearchCV类实现。

下面例子是通过RandomizedSearchCV对脊回归算法的参数进行100次迭代，并从中选择最优的参数。

Scipy中的uniform是一个均匀随机采样函数，默认生成0与1之间的随机采样数值。在这里利用uniform对参数进行随机采样。

```python
#随机搜索优化参数
from pandas import read_csv
from sklearn.linear_model import Ridge
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import uniform

filename='/home/aistudio/work/pima_data1.csv'
names=['preg','plas','pres','skin','test','mass','pedi',
   'age','class']
data=read_csv(filename,names=names)
#将数据分为输入数据和输出数据
array=data.values
x=array[:,0:8]
y=array[:,8]
#算法实例化
model=Ridge()
#设置要遍历的参数
param_grid={'alpha':uniform()}

#通过网格搜索查询最优参数
grid=RandomizedSearchCV(estimator=model,
param_distributions=param_grid, 
n_iter=100,random_state=7)
grid.fit(x,y)
#搜索结果
print('最高得分：%.3f' % grid.best_score_)
print('最优参数: %s' % grid.best_estimator_.alpha)
```

```python
最高得分：0.280
最优参数: 0.9779895119966027
```

# 第八章 结果部署

结果部署是机器学习的最后一步。

选定算法之后，对算法训练生成模型，并部署到生产环境上，以便利用机器学习解决实际问题。

模型生成之后，也需要定期对模型进行更行，是模型处于最新，最有效的状态，通常建议3-6月更新一次模型。

生成的模型序列化之后，当有新的数据出现时，需要反序列化已保存的模型，然后用其预测新的数据。

接下来介绍在Python中如何序列化和反序列化scikit-learn的模型。包括：

- 通过pickle来序列化和反序列化机器学习模型
- 通过joblib来序列化和反序列化机器学习模型

------

## Pickle

pickle序列化和反序列化机器学习模型，pickle是标准的Python序列化方法，可以通过它来序列化机器学习算法生成的模型，并将其保存到文件中。

当需要对新数据进行预测时，将保存在文件中的模型反序列化，并用其来预测新的数据。

```python
#pickle的使用
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from pickle import dump
from pickle import load
filename='/home/aistudio/work/pima_data1.csv'
names=['preg','plas','pres','skin','test','mass','pedi',
   'age','class']
data=read_csv(filename,names=names)
#将数据分为输入数据和输出数据
array=data.values
x=array[:,0:8]
y=array[:,8]
test_size=0.33
seed=4
x_train,x_test,y_train,y_test=train_test_split(x,y,
 test_size=test_size, random_state=seed)
#训练模型
model=LogisticRegression()
model.fit(x_train,y_train)

#保存模型
model_file='finalzied_model.sav'
with open(model_file,'wb') as model_f:
#模型序列化
dump(model,model_f)

#加载模型
with open(model_file,'rb') as model_f:
#模型反序列化
loaded_model=load(model_f)
result=loaded_model.score(x_test,y_test)
print('算法评估结果：%.3f%%' % (result * 100))
```

算法评估结果：80.315%

------

## Joblib

通过Joblib序列化与反序列化。joblib是Scipy生态环境的一部分，提供了通用的工具来序列化python的对象和反序列化python的对象。

通过joblib序列化对象时会采用Numpy的格式保存数据，这对某些保存数据到模型的算法非常有效，如K近邻算法。

```python
#joblib的使用
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.externals.joblib import dump
from sklearn.externals.joblib import load

filename='/home/aistudio/work/pima_data1.csv'
names=['preg','plas','pres','skin','test','mass','pedi'
,'age','class']
data=read_csv(filename,names=names)
#将数据分为输入数据和输出数据
array=data.values
x=array[:,0:8]
y=array[:,8]
test_size=0.33
seed=4
x_train,x_test,y_train,y_test=train_test_split(x,y,
test_size=test_size,random_state=seed)
#训练模型
model=LogisticRegression()
model.fit(x_train,y_train)

#保存模型
model_file='finalzied_model_joblib.sav'
with open(model_file,'wb') as model_f:
#模型序列化
dump(model,model_f)

#加载模型
with open(model_file,'rb') as model_f:
#模型反序列化
loaded_model=load(model_f)
result=loaded_model.score(x_test,y_test)
print('算法评估结果：%.3f%%' % (result * 100))
```

算法评估结果：80.315%

------

## 生成模型的技巧

在生成机器学习模型时，需要考虑以下几个问题：

- python版本：要记录python的版本，大部分情况下，在序列化和反序列化模型时，需要使用相同的python版本。
- 类库版本：同样需要记录所有主要类库的版本，因为在序列化模型和反序列化模型时需要使用相同版本的类库，不仅需要scipy和scikit-learn版本一致，其他类库版本也需要一致。
- 手动序列化：有时需要手动序列化算法，这样可以直接在scikit-learn中或其它平台重现这个模型。我们通常会花费大量的时间在选择算法和参数调整上，将这个过程手动记录下来比仅序列化模型更有价值。

# 预测模型项目模板

本章将介绍：

- 端到端的预测（分类与回归）模型的项目结构
- 如何通过这个项目模板来得到一个高准确度的模板。

机器学习是针对数据进行自动挖掘，找出数据的内在规律，并应用这个规律来预测新的数据。

![img](E:\工具\Typora\Temp\286275-20200525084908055-2130787356.png)

------

在项目中实践机器学习

一个很好的实践机器学习项目的方法是，使用从UCI机器学习仓库获取的数据集开启一个机器学习项目。

如果从一个数据集开始实践机器学习，应该如何将学到的所有技巧和方法整合到一起来处理机器学习的问题？

分类与回归模型的机器学习项目可以分成以下6个步骤：

> （1）定义问题
>
> （2）理解数据
>
> （3）数据准备
>
> （4）评估算法
>
> （5）优化模型
>
> （6）结果部署

------

机器学习项目的Python模版

> **（1）定义问题**
>
> - 导入类库
> - 导入数据
>
> **（2）理解数据**
>
> - 描叙性统计
> - 数据可视化
>
> **（3）数据准备**
>
> - 数据清洗
> - 特征选择
> - 数据转换
>
> **（4）评估算法**
>
> - 分离数据集
> - 定义模型评估标准
> - 算法审查
> - 算法比较
>
> **（5）优化模型**
>
> - 算法调参
> - 集成算法
>
> **（6）结果部署**
>
> - 预测评估数据集
> - 利用整个数据集生成模型
> - 序列化模型

当有新的机器学习项目时，新建一个python文件，并将这个模版粘贴进去，再按照前面章节介绍的方法将其填充到每一个步骤中。

------

## 1. 定义问题

> 主要是导入在机器学习项目中所需要的类库和数据集等，包括导入python类库、类、方法，以及导入数据。
>
> 同时这也是所有配置参数的配置模块。当数据集过大时，可以在这里对数据集进行廋身处理。

------

## 2. 理解数据

包括通过描叙性统计来分析数据和通过可视化来观察数据；设定假设条件并调查分析，这对模型的建立会有很大的帮助。

------

## 3. 数据准备

预处理数据，以便让数据可以很好的展示问题，以及熟悉输入和输出结果的关系。包括：

- 通过删除重复数据、标记错误数值，甚至标记错误的输入数据来清洗数据
- 特征选择，包括移除多余的特征属性和增加新的特征属性。
- 数据转化，对数据尺度进行调整，或者调整数据的分布，以便更好的展示问题

需要不断的重复这一步和下一步，直到找到足够准确的算法生成模型。

------

## 4. 评估算法

主要是为了寻找最佳算法子集，包括：

- 分离出评估数据集，以便于验证模型
- 定义模型评估标准，用来评估算法模型
- 抽样审查线性算法和非线性算法
- 比较算法的准确度

在面对一个机器学习的问题时候，需要花费大量的时间在评估算法和准备数据上，直到找到3-5种准确度足够的算法为止。

------

## 5. 优化模型

当得到一个准确度足够的算法列表后，要从中找出最合适的算法，通常有两种方法可以提高算法的准确度：

- 对每一种算法调参，得到最佳结果
- 使用集合算法来提高算法模型的准确度

------

## 6. 结果部署

一旦认为模型的准确度足够高，就可以将这个模型序列化，以便有新数据时使用该模型来预测数据。

通过验证数据集来验证被优化过的模型

通过整个数据集来生成模型

将模型序列化，以便于预测新的数据

做到这一步时，就可以将模型展示并发布给相关人员。当有新数据产生时，就可以采用这个模型来预测新数据。

------



 使用模版的小技巧

- 快速执行一遍：首先要快速的在项目中将模版中的每一个步骤执行一遍，这样会加强对项目每一部分的理解
- 循环：整个流程不是线性的，而是循环的，尤其是步骤3-5步骤，直到找到一个准确度足够的模型，或者达到预定周期
- 尝试每一个步骤：跳过某一步骤，坚持在模型中的每一步中最这些工作
- 定向准确度：要确保每次改变都会给结果带来正向影响，或者对其他步骤带来正向影响
- 按需适用：每一次改进都以提高算法模型的准确度为前提



# 回归项目实例 波士顿房价

## 定义问题

波士顿房价数据集收集于1978年，包括14个特征和506条数据（每条特征的中文解释暂时忽略）。

分析数据，发现输入的特征属性的度量单位是不统一的，也许需要对数据度量单位进行调整。

------

## 导入数据

首先导入项目中需要的类库。

```python
#导入类库
import numpy as np
from numpy import arange
from matplotlib import pyplot
from pandas import read_csv
from pandas import set_option
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet

from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_squared_error
```

接下来导入数据集到Python中，在导入数据集时还设定了数据集属性特征的名字。

```python
1 #导入数据
2 filename='/home/aistudio/work/housing.csv'
3 names=['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS',
         'RAD','TAX','PRTATIO','B','LSTAT','MEDV']
4 data=read_csv(filename,names=names,delim_whitespace=True)
```

在这里对每一个特征属性设定了一个名称，便于后面的程序中使用它们。因为CSV文件是使用空格键做分隔符，因此读入CSV文件时指定分割符为空格键（delim_whitespace=True)。

------

## 理解数据

首先看下数据维度，如数据集中有多少条记录，有多少个数据特征。

```python
1 #数据维度
2 print(data.shape)
(506, 14)
得到506条记录和14个特征属性。
再查看各个特征属性的字段类型：
1 print(data.dtypes)
CRIM       float64
ZN         float64
INDUS      float64
CHAS         int64
NOX        float64
RM         float64
AGE        float64
DIS        float64
RAD          int64
TAX        float64
PRTATIO    float64
B          float64
LSTAT      float64
MEDV       float64
dtype: object接下来对数据进行一次简单查看，如前30条记录：
1 set_option('display.width',200)
2 print(data.head(30))
CRIM    ZN  INDUS  CHAS    NOX  ...     TAX  PRTATIO       B  LSTAT  MEDV
0   0.006  18.0   2.31     0  0.538  ...   296.0     15.3  396.90   4.98  24.0
1   0.027   0.0   7.07     0  0.469  ...   242.0     17.8  396.90   9.14  21.6
2   0.027   0.0   7.07     0  0.469  ...   242.0     17.8  392.83   4.03  34.7
3   0.032   0.0   2.18     0  0.458  ...   222.0     18.7  394.63   2.94  33.4
4   0.069   0.0   2.18     0  0.458  ...   222.0     18.7  396.90   5.33  36.2
5   0.030   0.0   2.18     0  0.458  ...   222.0     18.7  394.12   5.21  28.7
6   0.088  12.5   7.87     0  0.524  ...   311.0     15.2  395.60  12.43  22.9
7   0.145  12.5   7.87     0  0.524  ...   311.0     15.2  396.90  19.15  27.1
8   0.211  12.5   7.87     0  0.524  ...   311.0     15.2  386.63  29.93  16.5
9   0.170  12.5   7.87     0  0.524  ...   311.0     15.2  386.71  17.10  18.9
10  0.225  12.5   7.87     0  0.524  ...   311.0     15.2  392.52  20.45  15.0
11  0.117  12.5   7.87     0  0.524  ...   311.0     15.2  396.90  13.27  18.9
12  0.094  12.5   7.87     0  0.524  ...   311.0     15.2  390.50  15.71  21.7
13  0.630   0.0   8.14     0  0.538  ...   307.0     21.0  396.90   8.26  20.4
14  0.638   0.0   8.14     0  0.538  ...   307.0     21.0  380.02  10.26  18.2
15  0.627   0.0   8.14     0  0.538  ...   307.0     21.0  395.62   8.47  19.9
16  1.054   0.0   8.14     0  0.538  ...   307.0     21.0  386.85   6.58  23.1
17  0.784   0.0   8.14     0  0.538  ...   307.0     21.0  386.75  14.67  17.5
18  0.803   0.0   8.14     0  0.538  ...   307.0     21.0  288.99  11.69  20.2
19  0.726   0.0   8.14     0  0.538  ...   307.0     21.0  390.95  11.28  18.2
20  1.252   0.0   8.14     0  0.538  ...   307.0     21.0  376.57  21.02  13.6
21  0.852   0.0   8.14     0  0.538  ...   307.0     21.0  392.53  13.83  19.6
22  1.232   0.0   8.14     0  0.538  ...   307.0     21.0  396.90  18.72  15.2
23  0.988   0.0   8.14     0  0.538  ...   307.0     21.0  394.54  19.88  14.5
24  0.750   0.0   8.14     0  0.538  ...   307.0     21.0  394.33  16.30  15.6
25  0.841   0.0   8.14     0  0.538  ...   307.0     21.0  303.42  16.51  13.9
26  0.672   0.0   8.14     0  0.538  ...   307.0     21.0  376.88  14.81  16.6
27  0.956   0.0   8.14     0  0.538  ...   307.0     21.0  306.38  17.28  14.8
28  0.773   0.0   8.14     0  0.538  ...   307.0     21.0  387.94  12.80  18.4
29  1.002   0.0   8.14     0  0.538  ...   307.0     21.0  380.23  11.98  21.0
[30 rows x 14 columns]
```

（测试发现，改变显示宽度200到400，显示界面没有变化，暂时不知什么原因？）

数据的描叙性统计信息，如数量，均值，方差等。

```python
1 set_option('precision',3)
2 print(data.describe())
        CRIM       ZN    INDUS   ...           B    LSTAT     MEDV
count  506.000  506.000  506.000   ...     506.000  506.000  506.000
mean     3.614   11.364   11.137   ...     356.674   12.653   22.533
std      8.602   23.322    6.860   ...      91.295    7.141    9.197
min      0.006    0.000    0.460   ...       0.320    1.730    5.000
25%      0.082    0.000    5.190   ...     375.377    6.950   17.025
50%      0.257    0.000    9.690   ...     391.440   11.360   21.200
75%      3.677   12.500   18.100   ...     396.225   16.955   25.000
max     88.976  100.000   27.740   ...     396.900   37.970   50.000

[8 rows x 14 columns]查看数据特征之间两两关联关系，这里查看数据的皮尔荪相关系数。
1 print(data.corr(method='pearson'))
CRIM     ZN  INDUS   CHAS  ...    PRTATIO      B  LSTAT   MEDV
CRIM     1.000 -0.200  0.407 -0.056  ...      0.290 -0.385  0.456 -0.388
ZN      -0.200  1.000 -0.534 -0.043  ...     -0.392  0.176 -0.413  0.360
INDUS    0.407 -0.534  1.000  0.063  ...      0.383 -0.357  0.604 -0.484
CHAS    -0.056 -0.043  0.063  1.000  ...     -0.122  0.049 -0.054  0.175
NOX      0.421 -0.517  0.764  0.091  ...      0.189 -0.380  0.591 -0.427
RM      -0.219  0.312 -0.392  0.091  ...     -0.356  0.128 -0.614  0.695
AGE      0.353 -0.570  0.645  0.087  ...      0.262 -0.274  0.602 -0.377
DIS     -0.380  0.664 -0.708 -0.099  ...     -0.232  0.292 -0.497  0.250
RAD      0.626 -0.312  0.595 -0.007  ...      0.465 -0.444  0.489 -0.382
TAX      0.583 -0.315  0.721 -0.036  ...      0.461 -0.442  0.544 -0.469
PRTATIO  0.290 -0.392  0.383 -0.122  ...      1.000 -0.177  0.374 -0.508
B       -0.385  0.176 -0.357  0.049  ...     -0.177  1.000 -0.366  0.333
LSTAT    0.456 -0.413  0.604 -0.054  ...      0.374 -0.366  1.000 -0.738
MEDV    -0.388  0.360 -0.484  0.175  ...     -0.508  0.333 -0.738  1.000
```
[14 rows x 14 columns]通过上面的结果可以看到，有些特征属性之间具有很强关联关系（>0.7或<-0.7):NOX与INDUS之间皮尔荪相关系数是0.76；DIS与INDUS之间的皮尔荪相关系数是-0.71.


------

## 数据可视化

单一特征图
查看每一个数据特征的单独分布图，多查看几种不同的图表有助于发现更好的方法。
```python
#直方图
data.hist(sharex=False,sharey=False,xlabelsize=1,ylabelsize=1)
pyplot.show()
```

![img](E:\工具\Typora\Temp\286275-20200529075552044-2100947239.png)

从上图可以看出有些数据呈指数分布，如CRIM，ZN，AGE，B；有些数据呈双峰分布，如RAD和TAX。

通过密度图可以展示这些数据的特征属性，密度图比直方图更加平滑的展示了这些数据特征。

```python
#密度图
data.plot(kind='density',subplots=True,layout=(4,4),
          sharex=False,fontsize=1)
pyplot.show()
```

![img](E:\工具\Typora\Temp\286275-20200529080117443-1698245439.png)

通过箱线图可以查看每一个数据特征的状况，也可以很方便地看出数据分布的偏态程度。

```python
#箱线图
data.plot(kind='box',subplots=True,layout=(4,4),
          sharex=False,sharey=False,fontsize=8)
pyplot.show()
```

![img](E:\工具\Typora\Temp\286275-20200529080640771-1311096917.png)

多重数据图表

可用多重数据图表来查看不同数据之间的相互影响关系。

```python
#散点矩阵图
scatter_matrix(data)
pyplot.show()
```

![img](E:\工具\Typora\Temp\286275-20200529081114136-1946044831.png)

再看下数据相互影响的相关矩阵图。

```python
#相关矩阵图
fig=pyplot.figure()
ax=fig.add_subplot(111)
cax=ax.matshow(data.corr(),vmin=-1,vmax=1,interpolation='none')
fig.colorbar(cax)
ticks=np.arange(0,14,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
pyplot.show()
```

![img](E:\工具\Typora\Temp\286275-20200529081635419-2066011157.png)

(越接近黄色表示相关性越强)

通过数据的相关性和数据的分布等发现，数据集中的数据结构比较复杂，需要考虑对数据进行转换，以提高模型的准确度。可以尝试：

- 通过特征选择来减少大部分相关性高的特征
- 通过标准化数据来降低不同数据度量单位带来的影响
- 通过正太化数据来降低不同的数据分布，以提高算法的准确度

可以进一步查看数据的可能性分级（离散化），它可以帮助提高决策树的准确度。

------

## 分离评估数据集 

分离出一个评估数据集需要确保与训练模型的数据集完全隔离，有助于最终判断和报告模型的准确度。这里是2/8开。

```python
#分离数据集
array=data.values
x=array[:,0:13]
y=array[:,13]
validation_size=0.2
seed=7
x_train,x_validation,y_train,y_validation=train_test_split(
  x,y,test_size=validation_size,random_state=seed)
```

------

## 评估算法--原始数据

分析完数据不能立刻选择出哪个算法对需要解决的问题最有效。

直观上认为，由于部分数据的线性分布，线性回归算法和弹性网络回归算法对解决问题可能比较有效。另外，由于数据的离散化，通过决策树算法或支持向量机算法也许可以生成高准确度的模型。

下面采用10折交叉验证来分离数据，通过均方误差来比较算法的准确度。均方误差越趋近于0，算法准确度越高。

```python
#评估算法--评估标准
num_folds=10
seed=7
scoring='neg_mean_squared_error'
```

对原始数据不做任何处理，对算法进行一个评估，形成一个算法的评估基准。这个基准值是对后续算法改善优劣比较的基准值。选择三个线性算法和三个非线性算法来进行比较。

线性算法：线性回归（LR），套索回归（LASSO）和弹性网络回归（EN）

非线性：分类与回归树（CART），支持向量机（SVM）和K近邻（KNN）。

```python
models={}
models['LR']=LinearRegression()
models['LASSO']=Lasso()
models["EN"]=ElasticNet()
models['KNN']=KNeighborsRegressor()
models['CART']=DecisionTreeRegressor()
models['SVM']=SVR()
```

对所有的算法使用默认参数，并比较算法的准确度，此处比较的是均方误差的均值和标准方差。

```python
result=[]
for key in models:
    kfold=KFold(n_splits=num_folds,random_state=seed)
    cv_result=cross_val_score(models[key],x_train,y_train,
                              cv=kfold,scoring=scoring)
    result.append(cv_result)
    print('%s: %f (%f)' % (key,cv_result.mean(),cv_result.std()))
```

从执行的结果来看，线性回归（LR)具有最优的MSE，接下来是分类与回归树算法（CART）。

```python
LR: -21.379856 (9.414264)
LASSO: -26.423561 (11.651110)
EN: -27.502259 (12.305022)
KNN: -41.896488 (13.901688)
CART: -25.118465 (13.596293)
SVM: -85.518342 (31.994798)
```

再查看所有的10折交叉分离验证的结果。

```python
#评估算法----箱线图
fig=pyplot.figure()
fig.suptitle('Algorithm Comparison')
ax=fig.add_subplot(111)
pyplot.boxplot(result)
ax.set_xticklabels(models.keys())
pyplot.show()
```

执行结果如下图，从图中可以看到，线性算法的分布比较类似，并且K近邻算法的结果分布非常紧凑。

![img](E:\工具\Typora\Temp\286275-20200529161509056-1795390026.png)

不同的数据度量单位，也许是K近邻算法和支持向量机算法表现不佳的主要原因。

下面将对数据进行正太化处理，再次比较算法的结果。

------

##  评估算法----正太化数据

对训练数据集进行数据转换处理，将所有的数据特征值转化成0为中位值，标准差为1的数据。

对数据正太化时，为了防止数据泄漏，采用Pipeline来正太化数据。

为了与前面的结果进行比较，此处采用相同的评估框架来评估算法模型。

```python
#评估算法----正太化数据
pipelines={}
pipelines['ScalerLR']=Pipeline([('Scaler',StandardScaler()),
                                ('LR',LinearRegression())])
pipelines['ScalerLASSO']=Pipeline([('Scaler',StandardScaler()),
                                   ('LASSO',Lasso())])
pipelines['ScalerEN']=Pipeline([('Scaler',StandardScaler()),
                                ('EN',ElasticNet())])
pipelines['ScalerKNN']=Pipeline([('Scaler',StandardScaler()),
                                 ('KNN',KNeighborsRegressor())])
pipelines['ScalerCART']=Pipeline([('Scaler',StandardScaler()),
                                  ('CART',DecisionTreeRegressor())])
pipelines['ScalerSVM']=Pipeline([('Scaler',StandardScaler()),
                                 ('SVM',SVR())])

results=[]
for key in pipelines:
    kfold=KFold(n_splits=num_folds,random_state=seed)
    cv_result=cross_val_score(pipelines[key],x_train,y_train,
                              cv=kfold,scoring=scoring)
    results.append(cv_result)
    print('%s: %f (%f)' % (key,cv_result.mean(),cv_result.std()))
```

执行后，发现K近邻算法具有最优的MES。

```python
ScalerLR: -21.379856 (9.414264)
ScalerLASSO: -26.607314 (8.978761)
ScalerEN: -27.932372 (10.587490)
ScalerKNN: -20.107620 (12.376949)
ScalerCART: -27.487674 (12.436629)
ScalerSVM: -29.633086 (17.009186)接下来看一下所有10折交叉分离验证的结果：
```

```python
#评估算法----箱线图
fig=pyplot.figure()
fig.suptitle('Algorithm Comparison')
ax=fig.add_subplot(111)
pyplot.boxplot(results)
ax.set_xticklabels(models.keys())
pyplot.show()
```

从生成箱线图中可以看到K近邻算法具有最优的MSE和最紧凑的数据分布。

![img](E:\工具\Typora\Temp\286275-20200529174518118-1607093379.png)

------

## 调参改善算法

K近邻算法的默认参数近邻个数（n_neighbors)是5，下面通过网格搜索算法来优化参数。

```python
#调参改善算法----KNN
scaler=StandardScaler().fit(x_train)
rescaledX=scaler.transform(x_train)
param_grid={'n_neighbors':[1,3,5,7,9,11,13,15,17,19,21]}
model=KNeighborsRegressor()
kfold=KFold(n_splits=num_folds,random_state=seed)
grid=GridSearchCV(estimator=model,param_grid=param_grid,
                  scoring=scoring,cv=kfold)
grid_result=grid.fit(X=rescaledX,y=y_train)

print('最优：%s 使用 %s' % (grid_result.best_score_, 
                       grid_result.best_params_))
cv_results=zip(grid_result.cv_results_['mean_test_score'],
               grid_result.cv_results_['std_test_score'],
               grid_result.cv_results_['params'])
for mean,std,param in cv_results:
    print('%f (%f) with %r' % (mean,std,param))
```

最优结果----K近邻算法的默认参数近邻个数（n_neighbors)是3.

```python
最优：-18.172136963696367 使用 {'n_neighbors': 3}
-20.208663 (15.029652) with {'n_neighbors': 1}
-18.172137 (12.950570) with {'n_neighbors': 3}
-20.131163 (12.203697) with {'n_neighbors': 5}
-20.575845 (12.345886) with {'n_neighbors': 7}
-20.368264 (11.621738) with {'n_neighbors': 9}
-21.009204 (11.610012) with {'n_neighbors': 11}
-21.151809 (11.943318) with {'n_neighbors': 13}
-21.557400 (11.536339) with {'n_neighbors': 15}
-22.789938 (11.566861) with {'n_neighbors': 17}
-23.871873 (11.340389) with {'n_neighbors': 19}
-24.361362 (11.914786) with {'n_neighbors': 21}
```

------

## 集成算法

除了调参之外，提高模型准确度的方法是使用集成算法。
下面会对表现比较好的线性回归、K近邻、分类与回归树进行集成，来看看算法能否提高。
装袋算法：随机森林（RF）和极端随机树（ET）
提升算法：AdaBoost（AB）和随机梯度上升（GBM）
依然采用和前面同样的评估框架和正太化之后的数据来分析相关的算法。

```python
#集成算法
ensembles={}
ensembles['ScaledAB']=Pipeline([('Scaler',StandardScaler()),
                                ('AB',AdaBoostRegressor())])
ensembles['ScaledAB-KNN']=Pipeline([('Scaler',StandardScaler()),
                                    ('ABKNN',AdaBoostRegressor(base_estimator=KNeighborsRegressor(n_neighbors=3)))])
ensembles['ScaledAB-LR']=Pipeline([('Scaler',StandardScaler()),
                                   ('ABLR',AdaBoostRegressor(LinearRegression()))])
ensembles['ScaledRFR']=Pipeline([('Scaler',StandardScaler()),
                                 ('RFR',RandomForestRegressor())])
ensembles['ScaledETR']=Pipeline([('Scaler',StandardScaler()),
                                 ('ETR',ExtraTreesRegressor())])
ensembles['ScaledGBR']=Pipeline([('Scaler',StandardScaler()),
                                 ('RBR',GradientBoostingRegressor())])

results=[]
for key in ensembles:
    kfold=KFold(n_splits=num_folds,random_state=seed)
    cv_result=cross_val_score(ensembles[key],x_train,y_train,
                              cv=kfold,scoring=scoring)
    results.append(cv_result)
    print('%s: %f (%f)' % (key,cv_result.mean(),cv_result.std()))
```

与前面的线性算法和非线性算法相比，这次准确度都有了较大的提高。

```python
ScaledAB: -15.396665 (6.887380)
ScaledAB-KNN: -15.897982 (9.477002)
ScaledAB-LR: -24.463893 (10.070492)
ScaledRFR: -13.172716 (5.511913)
ScaledETR: -10.210106 (5.516494)
ScaledGBR: -10.099802 (4.388978)
接下来通过箱线图看一下算法在10折交叉验证中均方误差的分布情况。
```

```python
#集成算法----箱线图
fig=pyplot.figure()
fig.suptitle('Algorithm Comparison')
ax=fig.add_subplot(111)
pyplot.boxplot(results)
ax.set_xticklabels(ensembles.keys())
pyplot.show()
```

执行结果如下图，随机梯度上升算法和极端随机树算法具有较高的中位值和分布状况。

![img](E:\工具\Typora\Temp\286275-20200529184808707-1835151403.png)

------

## 集成算法调参

 集成算法都有一个参数n_estimators，这是一个很好的可以用来调整的参数，会带来更准确的结果。下面对随机梯度上升（GBM）和极端随机树（ET）进行调参。再次比较这两个算法的准确度，来确定最终的算法模型。

```python
#集成算法GBM--调参
caler=StandardScaler().fit(x_train)
rescaledX=scaler.transform(x_train)
param_grid={'n_estimators':[10,50,100,200,300,400,500,600,700,800,900]}
model=GradientBoostingRegressor()
kfold=KFold(n_splits=num_folds,random_state=seed)
grid=GridSearchCV(estimator=model,param_grid=param_grid,scoring=scoring,cv=kfold)
grid_result=grid.fit(X=rescaledX,y=y_train)
print('最优：%s 使用%s' % (grid_result.best_score_,grid_result.best_params_))

#集成算法ET--调参
caler=StandardScaler().fit(x_train)
rescaledX=scaler.transform(x_train)
param_grid={'n_estimators':[5,10,20,30,40,50,60,70,80,90,100]}
model=ExtraTreesRegressor()
kfold=KFold(n_splits=num_folds,random_state=seed)
grid=GridSearchCV(estimator=model,param_grid=param_grid,scoring=scoring,cv=kfold)
grid_result=grid.fit(X=rescaledX,y=y_train)
print('最优：%s 使用%s' % (grid_result.best_score_,grid_result.best_params_))
```

对于随机梯度上升（GBM)算法来说，最优的n_estimators=400,而对于极端随机树（ET）来说，最优的n_estimators=90,且，ET稍优于GBM，因此采用极端随机树算法来训练最终模型。

```python
最优：-9.26198126367106 使用{'n_estimators': 400}
最优：-8.999967152548582 使用{'n_estimators': 90}
小技巧，当最优参数是param_grid的边界值时，有必要调整param_grid进行下一次调参。
```

------

## 确定最终模型

我们已经确定使用极端随机树（ET）算法来生成模型，下面就对该算法进行训练和生成模型，并计算模型的准确度。

```python
#训练模型
caler=StandardScaler().fit(x_train)
rescaledX=scaler.transform(x_train)
gbr=ExtraTreesRegressor(n_estimators=90)
gbr.fit(X=rescaledX,y=y_train)
```

再通过评估数据集来评估算法的准确度。

```python
#评估算法模型
rescaledX_validation=scaler.transform(x_validation)
predictions=gbr.predict(rescaledX_validation)
print(mean_squared_error(y_validation,predictions))
```

得到执行结果：

```python
13.974640426046953
```



# 二分类实例 矿物分类

分类问题项目流程：

- 如何端到端的完成一个分类问题的模型
- 如何通过数据转换提高模型的准确度
- 如何通过调参提高模型的准确度
- 如何通过算法集成提高模型的准确度

------

## 问题定义

在这个项目中采用声纳、矿山和岩石数据集。通过声纳返回的信息判断物质是金属还是岩石。这个数据集共有208条记录，每条记录了60中不同的声纳探测数据和一个分类结果，若是岩石则标记为R，若是金属则标记为M。

------

## 导入数据

 在导入之前，先需要导入所需的类库。

```python
#60中声纳探测预测
import numpy as np
from matplotlib import pyplot
from pandas import read_csv
from pandas import set_option
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier

#导入数据
filename='/home/aistudio/work/sonar.all-data.csv'
dataset=read_csv(filename,header=None)
```

因为每条记录都是60种不同的声纳探测结果，没有办法提供合适的名字，所以导入时没有指定特征属性名。

------

## 数据理解

先确认数据的维度，例如记录的条数和数据特征属性的个数：

```python
#数据维度
print(dataset.shape)
```

执行结果显示数据有208条记录和61个数据特征属性（包含60此声纳探测数据和一个分类结果）。

```python
(208, 61)
```
接下来看一下各个数据特征和数据类型。
```python
#查看数据类型
set_option('display.max_rows',500)
print(dataset.dtypes)
```

结果显示所有的特征属性的数据类型都是数字。

再查看最开始的20条记录：

```python
set_option('display.width',100)
print(dataset.head(20))
```

数据的描述性统计信息：

```python
set_option('precision',3)
print(dataset.describe())
```

可以看到，数据具有相同的范围，但是中位值不同，这也许对数据正太化的结果有正面的影响。

最后看一下数据的分类分布：

```python
print(dataset.groupby(60).size())
60
M    111
R     97
dtype: int64
```

------

## 数据可视化

```python
#直方图
dataset.hist(sharex=False,sharey=False,xlabelsize=1,ylabelsize=1)
pyplot.show()
```

下图中显示，大部分数据呈高斯分布或指数分布

![img](E:\工具\Typora\Temp\286275-20200601085126634-2112415065.png)

接下来看下密度分布图：

```python
#密度图
dataset.plot(kind='density',subplots=True,layout=(8,8),
             sharex=False,legend=False, fontsize=1)
pyplot.show()
```

可以看到大部分数据呈现一定程度的偏态分布，也许通过Box-Cox转换可以提高模型的准确度。

Box-Cox转换是统计中常用的一种数据变化方式，用于连续响应变量不满足正太分布的情况。Box-Cox转换后，可以在一定程度上减少不可观测的误差，也可以预测变量的相关性，将数据转换成正太分布。

![img](E:\工具\Typora\Temp\286275-20200601090118601-1520401196.png)

接下来看一下数据特征的两两相关性:

```python
#关系矩阵图
fig=pyplot.figure()
ax=fig.add_subplot(111)
cax=ax.matshow(dataset.corr(),vmin=-1,vmax=1,interpolation='none')
fig.colorbar(cax)
pyplot.show()
```

可以看到数据有一定的负先关性：

![img](E:\工具\Typora\Temp\286275-20200601090448163-1479959138.png)

------

##  分离评估数据集

按照常规，2：8分：

```python
#分离评估数据集
array=dataset.values
x=array[:,0:60].astype(float)
y=array[:,60]
validation_size=0.2
seed=7
x_train,x_validation,y_train,y_validation=train_test_split(x,
								y,test_size=validation_size,random_state=seed)
```

------

## 评估算法

采用10折交叉验证来分离数据，并通过准确度来比较算法，这样可以很快的找到最优算法：

```python
#评估算法--评估标准
num_folds=10
seed=7
scoring='accuracy'
```

同上一节一样，首先利用原始数据对算法进行审查，下面会选择六种不同的算法进行审查。

线性算法：罗辑回归（LR）和线性判别分析（LDA）

非线性算法：分类与回归树算法（CART），支持向量机（SVM），贝叶斯分类器（NB）和K近邻（KNN）

算法模型初始化代码如下：

```python
models={}
models['LR']=LogisticRegression()
models['LDA']=LinearDiscriminantAnalysis()
models['KNN']=KNeighborsClassifier()
models['CART']=DecisionTreeClassifier()
models['NB']=GaussianNB()
models['SVM']=SVC()
```

对所有的算法都不进行调参，使用默认的参数来比较算法。通过比较准确度的平均值和标准方差来比较算法：

```python
results=[]
for key in models:
    kfold=KFold(n_splits=num_folds,random_state=seed)
    cv_results=cross_val_score(models[key],x_train,y_train,cv=kfold,
                               scoring=scoring)
    results.append(cv_results)
    print('%s: %f (%f)' % (key,cv_results.mean(),cv_results.std()))
```

执行结果显示，逻辑回归算法（LR）和K近邻（KNN)值得我们进一步分析。

```python
LR: 0.782721 (0.093796)
LDA: 0.746324 (0.117854)
KNN: 0.808088 (0.067507)
CART: 0.727941 (0.102731)
NB: 0.648897 (0.141868)
SVM: 0.608824 (0.118656)
```
  这只是K折交叉验证给出的平均统计结果，通常还要看每次得出的结果分布状况。在这里使用箱线图来显示数据分布。

```python
#评估算法----箱线图
fig=pyplot.figure()
fig.suptitle('Algorithm Comparison')
ax=fig.add_subplot(111)
pyplot.boxplot(results)
ax.set_xticklabels(models.keys())
pyplot.show()
```

如下图所示，K近邻算法的执行结果分布比较紧凑，说明算法对数据的处理比较准确，但是，支持向量机(svm)的结果较差。

![img](E:\工具\Typora\Temp\286275-20200602081724865-908191952.png)

可能是数据分布的多样性导致SVM算法不够准确，接下来会对数据进行正太化，然后重新评估算法。

下面采用Pipeline来流程化处理：

```python
#评估算法----正太化数据
pipelines={}
pipelines['ScalerLR']=Pipeline([('Scaler',StandardScaler()),('LR',LogisticRegression())])
pipelines['ScalerLDA']=Pipeline([('Scaler',StandardScaler()),('LDA',LinearDiscriminantAnalysis())])
pipelines['ScalerKNN']=Pipeline([('Scaler',StandardScaler()),('KNN',KNeighborsClassifier())])
pipelines['ScalerCART']=Pipeline([('Scaler',StandardScaler()),('CART',DecisionTreeClassifier())])
pipelines['ScalerNB']=Pipeline([('Scaler',StandardScaler()),('NB',GaussianNB())])
pipelines['ScalerSVM']=Pipeline([('Scaler',StandardScaler()),('SVM',SVC())])

results=[]
for key in pipelines:
    kfold=KFold(n_splits=num_folds,random_state=seed)
    cv_results=cross_val_score(pipelines[key],x_train,y_train,cv=kfold,scoring=scoring)
    results.append(cv_results)
    print('%s: %f (%f)' % (key,cv_results.mean(),cv_results.std()))
```

从执行结果来看，K近邻依然具有最好的结果，甚至还有所提高，同时SVM也得到了极大的提高。

```python
ScalerLR: 0.734191 (0.095885)
ScalerLDA: 0.746324 (0.117854)
ScalerKNN: 0.825735 (0.054511)
ScalerCART: 0.717647 (0.095103)
ScalerNB: 0.648897 (0.141868)
ScalerSVM: 0.836397 (0.088697)再通过箱线图看看：
```

![img](E:\工具\Typora\Temp\286275-20200602082519284-54666539.png)

同样可以看到KNN和SVM的数据分布也是最紧凑的。

------

## 算法调参

下面就对KNN和SVM这两个算法进行调参，以进一步提高算法的准确度。

K近邻默认n_neighbors=5，下面对这个参数多试几组，采用相同的10折交叉验证来测试：

```python
#调参改进算法--KNN
scaler=StandardScaler().fit(x_train)
rescaledX=scaler.transform(x_train)
param_grid={'n_neighbors':[1,3,5,7,9,11,13,15,17,19,21]}
model=KNeighborsClassifier()
kfold=KFold(n_splits=num_folds,random_state=seed)
grid=GridSearchCV(estimator=model,param_grid=param_grid,
                  scoring=scoring,cv=kfold)
grid_result=grid.fit(X=rescaledX,y=y_train)
print('最优：%s 使用%s' % (grid_result.best_score_,
                      grid_result.best_params_))
cv_results = zip(grid_result.cv_results_['mean_test_score'],
                 grid_result.cv_results_['std_test_score'],
                 grid_result.cv_results_['params'])
for mean,std,param in cv_results:
    print('%f (%f) with %r' % (mean, std, param))
```

执行结果如下：

```python
最优：0.8493975903614458 使用{'n_neighbors': 1}
0.849398 (0.059881) with {'n_neighbors': 1}
0.837349 (0.066303) with {'n_neighbors': 3}
0.837349 (0.037500) with {'n_neighbors': 5}
0.765060 (0.089510) with {'n_neighbors': 7}
0.753012 (0.086979) with {'n_neighbors': 9}
0.734940 (0.104890) with {'n_neighbors': 11}
0.734940 (0.105836) with {'n_neighbors': 13}
0.728916 (0.075873) with {'n_neighbors': 15}
0.710843 (0.078716) with {'n_neighbors': 17}
0.722892 (0.084555) with {'n_neighbors': 19}
0.710843 (0.108829) with {'n_neighbors': 21}
```
得到最优的n_neighbors=1.

支持向量机有两个重要的参数，C（惩罚系数）和kernel（径向基函数），默认的C参数是1.0，kernal=rbf，下面将对这两个参数进行调参。

```python
#SVM--调参
scaler=StandardScaler().fit(x_train)
rescaledX=scaler.transform(x_train).astype(float)
param_grid={}
param_grid['C']=[0.1,0.3,0.5,0.7,0.9,1.0,1.3,1.5,1.7,2.0]
param_grid['kernel']=['linear','poly','rbf','sigmoid','precomputed']
model=SVC()
kfold=KFold(n_splits=num_folds,random_state=seed)
grid=GridSearchCV(estimator=model,param_grid=param_grid,
                  scoring=scoring,cv=kfold)
grid_result=grid.fit(X=rescaledX, y=y_train)
print('最优：%s 使用%s' % (grid_result.best_score_,
                      grid_result.best_params_))
cv_results=zip(grid_result.cv_results_['mean_test_score'],
               grid_result.cv_results_['std_test_score'],
               grid_result.cv_results_['param'])
for mean, std, param in cv_results:
    print('%f (%f) with %r' % (mean, std, param))
```

上面的代码调试过程中有误，但我找不出原因（Line 10： ValueError: X should be a square kernel matrix），为了这本书的完整性，我还是贴出错误的代码。

书中给出的测试结果：

最好的支持向量机SVM的参数是C=1.5，kernel=RBF。准确度达到0.8675，这也比K近邻算法的结果要好一些。

------

## 集成算法

下面会对四种集成算法进行比较，以便进一步提高算法的准确度。

装袋算法：随机森林（RF）和极端随机树（ET）

提升算法：AdaBoost（AB）和随机梯度上升（GBM）

依然采用10折交叉验证集成算法的准确度，以便选择最优的算法模型。

```python
#集成算法
num_folds=10
scoring='accuracy'

ensembles={}
ensembles['ScaledAB']=Pipeline([('Scaler',StandardScaler()),
                                ('AB',AdaBoostClassifier())])
ensembles['ScaledGBM']=Pipeline([('Scaler',StandardScaler()),
                                 ('GBM',GradientBoostingClassifier())])
ensembles['ScaledRF']=Pipeline([('Scaler',StandardScaler()),
                                ('RFR',RandomForestClassifier())])
ensembles['ScaledET']=Pipeline([('Scaler',StandardScaler()),
                                ('ETR',ExtraTreesClassifier())])

results=[]
for key in ensembles:
    kfold=KFold(n_splits=num_folds,random_state=seed)
    cv_result=cross_val_score(ensembles[key],x_train,y_train,
                              cv=kfold,scoring=scoring)
    results.append(cv_result)
    print('%s: %f (%f)' % (key,cv_result.mean(),cv_result.std()))
```

执行结果如下：

```python
ScaledAB: 0.813971 (0.066017)
ScaledGBM: 0.847794 (0.100189)
ScaledRF: 0.764338 (0.092898)
ScaledET: 0.771691 (0.097858)
```

 通过箱线图来看一下算法结果的离散状况。

```python
#集成算法----箱线图
fig=pyplot.figure()
fig.suptitle('Scaled Algorithm Comparison')
ax=fig.add_subplot(111)
pyplot.boxplot(results)
ax.set_xticklabels(ensembles.keys())
pyplot.show()
```

![img](E:\工具\Typora\Temp\286275-20200608080930066-1915815515.png)

随机梯度上升（GBM）值得进一步分析，因为它具有良好的准确度，并且数据比较紧凑，接下来对其进行调参。

```python
#集成算法GBM--调参
scaler=StandardScaler().fit(x_train)
rescaledX=scaler.transform(x_train)
param_grid={'n_estimators':[10,50,100,200,300,400,500,600,700,800,900]}
model=GradientBoostingClassifier()
kfold=KFold(n_splits=num_folds,random_state=seed)
grid=GridSearchCV(estimator=model,param_grid=param_grid,scoring=scoring,
                  cv=kfold)
grid_result=grid.fit(X=rescaledX,y=y_train)
print('最优：%s 使用%s' % (grid_result.best_score_,grid_result.best_params_))
```

```python
最优：0.8614457831325302 使用{'n_estimators': 200}
```

------

## 确定最终模型

依据上面的测试，采用支持向量机（SVM），通过训练集数据生成算法模型，并通过预留的评估数据来评估模型。
在算法评估过程中发现，支持向量机对正太化的数据具有较高的准确度，所以对训练集做正太化处理，对评估数据集也做相同的处理。

```python
#训练模型
scaler=StandardScaler().fit(x_train)
rescaledX=scaler.transform(x_train)
model=SVC(C=1.5,kernel='rbf')
model.fit(X=rescaledX,y=y_train)

#评估算法模型
rescaledX_validation=scaler.transform(x_validation)
predictions=model.predict(rescaledX_validation)
print(accuracy_score(y_validation,predictions))
print(confusion_matrix(y_validation,predictions))
print(classification_report(y_validation,predictions))
```

```python
最优：0.8674698795180723 使用{'n_estimators': 500}
0.8571428571428571
[[23  4]
 [ 2 13]]
              precision    recall  f1-score   support

           M       0.92      0.85      0.88        27
           R       0.76      0.87      0.81        15
 # micro avg       0.86      0.86      0.86        42
   macro avg       0.84      0.86      0.85        42
weighted avg       0.86      0.86      0.86        42
以上是只采用参数优化后的SVM得到的结果，看起来比集成算法效果还好。
```

