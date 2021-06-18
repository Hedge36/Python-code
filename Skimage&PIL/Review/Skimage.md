# Skimage

##   All Before  

**Docs url : https://scikit-image.org/**

If there are any problem on skimage, check here.

## 1. 图像处理常识

### 图像通道

在Photoshop中有一个很重要概念叫图像通道，在RGB色彩模式下就是指那单独的红色、绿色、蓝色部分。也就是说，一幅完整的图像，是由红色绿色蓝色三个通道组成的。他们共同作用产生了完整的图像。

表征为每一个像素点，亦即Array矩阵每一个点的长度。

------

### 图像通道类型

> #### 彩色图像RGB
>
> 有blue，green，red三个通道，取值范围均为0-255；
>
> #### 彩色图像RGBA
>
> 有blue，green，red，alpha 四个通道，前三个取值范围均为0-255，alpha表示透明的，取值范围为0-1；
>
> #### 灰度图GRAY
>
> 只有一个通道0-255，所以一共有256种颜色；
>
> #### 二值图像BW
>
> 只有两种颜色，黑色和白色，二值化就是把图像的像素转变为0或者255，只有这两个像素值。0白色 1黑色 。0是黑色，255是白色。

在skimage中，一张图片就是一个简单的numpy数组，数组的数据类型有很多种，相互之间也可以转换。这些数据类型及取值范围如下表所示：

| Data type | Range             |
| --------- | ----------------- |
| **uint8** | 0 to 255          |
| uint16    | 0 to 65535        |
| uint32    | 0 to 232          |
| float     | -1 to 1 or 0 to 1 |
| int8      | -128 to 127       |
| int16     | -32768 to 32767   |
| int32     | -231 to 231 - 1   |

数据类型之间可以自由转换，但**float转为unit8，有可能会造成数据的损失**，因此会有警告提醒。

| Function name | Description                       |
| ------------- | --------------------------------- |
| img_as_float  | Convert to 64-bit floating point. |
| img_as_ubyte  | Convert to 8-bit uint.            |
| img_as_uint   | Convert to 16-bit uint.           |
| img_as_int    | Convert to 16-bit int.            |

float64至uniti8处理办法：

```python
(img*255).astype(np.uint8)
```

-------

### 椒盐噪声

**椒盐噪声**也称为**脉冲噪声**，是图像中经常见到的一种噪声，它是一种随机出现的白点或者黑点，可能是亮的区域有黑色像素或是在暗的区域有白色像素(或是两者皆有）。椒盐噪声的成因可能是影像讯号受到突如其来的强烈干扰而产生、类比数位转换器或位元传输错误等。例如失效的感应器导致像素值为最小值，饱和的感应器导致像素值为最大值。

-------

### 图形滤波

图像滤波，即在尽量保留图像细节特征的条件下对目标图像的噪声进行抑制，是图像预处理中不可缺少的操作，其处理效果的好坏将直接影响到后续图像处理和分析的有效性和可靠性。

> **目的**
>
> 1、消除图像中混入的噪声；
> 　　2、为图像识别抽取出图像特征。
>
> **要求**
>
> 1、不能损坏图像轮廓及边缘；
> 　　2、图像视觉效果应当更好。

### 滤波器

### 非线性滤波器

一般说来，当信号频谱与噪声频谱混叠时或者当信号中含有非叠加性噪声时如由系统非线性引起的噪声或存在非高斯噪声等)，传统的线性滤波技术，如傅立变换，在滤除噪声的同时，总会以某种方式模糊图像细节(如边缘等)进而导致像线性特征的定位精度及特征的可抽取性降低。而非线性滤波器是基于对输入信号的一种非线性映射关系，常可以把某一特定的噪声近似地映射为零而保留信号的要特征，因而其在一定程度上能克服线性滤波器的不足之处。

### 中值滤波

中值滤波由Turky在1971年提出，最初用于时间序列分析，后来被用于图像处理，并在去噪复原中取得了较好的效果。中值滤波器是基于次序统计完成信号恢复的一种典型的非线性滤波器，其基本原理是把图像或序列中心点位置的值用该域的中值替代，具有运算简单、速度快、除噪效果好等优点，曾被认为是非线性滤波的代表。然而，一方面中值滤波因不具有平均作用，在滤除诸如高斯噪声时会严重损失信号的高频信息，使图像的边缘等细节模糊；另一方面中值滤波的滤波效果常受到噪声强度以及滤波窗口的大小和形状等因素的制约，为了使中值滤波器具有更好的细节保护特性及适应性，人们提出了许多中值滤波器的改进算法。

标准中值滤波算法的基本思想是将滤波窗口内的最大值和最小值均视为噪声，用滤波窗口内的中值代替窗口中心像素点的灰度，在一定程度上抑制了噪声。实际上在一定邻域范围内具有最大或最小灰度值这一特性的，除了噪声点，还包括图像中的边缘点、线性特征点等。中值滤波以此作为图像滤波依据，其滤波结果不可避免地会破坏图像的线段、锐角等信息。因此，要找到一种既能实现有效滤除噪声，又能完整保留图像细节的滤波机制，仅考虑噪声的灰度特性是难以实现的。

### 形态学滤波器

随着数学各分支在理论和应用上的逐步深入，以数学形态学为代表的非线性滤波在保护图像边缘和细节方面取得了显著进展。形态学滤波器是近年来出现的一类重要的非线性滤波器，它由早期的二值形滤波器发展为后来的多值(灰度)形态滤波器，在形状识别、边缘检测、纹理分析、图像恢复和增强等领域了广泛的应用。形态滤波方法充分利用形态学运算所具有的几何特征和良好的代数性质，主要采用态学开、闭运算进行滤波操作。从形态学基本原理可知，形态学的开运算会去掉图像上与结构元素的形态不相吻合的相对亮的分布结构，同时保留那些相吻合的部分;而闭运算则会填充那些图像上与结构元素不相吻合的相对暗的分布结构，同时保留那些相吻合的部分。因此他们都可以用来有效的提取特征和平滑像。值得注意地是，采用形态滤波器时，应根据不同的目的选择具有不同形状、大小和方向特性的结构元素。此外，形态学开、闭运算都具有幂等性，这意味着一次滤波就己将所有特定于结构元素的噪声滤除干净，再次重复不会产生新的结果。这是一个经典方法(如线性卷积滤波、中值滤波)所不具备的性质。由于形态学运算是从图像的几何形态观点来进行图像处理的，因此这种优良的非线性滤波器能在滤波的同时，保持图像结构不被钝化。

### 双边滤波

双边滤波是结合图像的空间邻近度和像素值相似度的一种折中处理，同时考虑空域信息和灰度相似性，达到保留边缘且去除噪声的目的。



## 2. 简介

学习参考网站：https://www.cnblogs.com/denny402/p/5121501.html

skimage包的全称是scikit-image SciKit (toolkit for SciPy) ，它对scipy.ndimage进行了扩展，提供了更多的图片处理功能。它是由python语言编写的，由scipy 社区开发和维护。skimage包由许多的子模块组成，各个子模块提供不同的功能。

### 2.1 主要子模块

| Submodule name | Main functions                                              |
| -------------- | ----------------------------------------------------------- |
| io             | 读取、保存和显示图片或视频                                  |
| data           | 提供一些测试图片和样本数据                                  |
| color          | 颜色空间变换                                                |
| filters        | 图像增强、边缘检测、排序滤波器、自动阈值等                  |
| draw           | 操作于numpy数组上的基本图形绘制，包括线条、矩形、圆和文本等 |
| transform      | 几何变换或其它变换，如旋转、拉伸和拉东变换等                |
| morphology     | 形态学操作，如开闭运算、骨架提取等                          |
| exposure       | 图片强度调整，如亮度调整、直方图均衡等                      |
| feature        | 特征检测与提取等                                            |
| measure        | 图像属性的测量，如相似性或等高线等                          |
| segmentation   | 图像分割                                                    |
| restoration    | 图像恢复                                                    |
| util           | 通用函数                                                    |

### 2.2 内置图片

skimage程序自带了一些示例图片，如果我们不想从外部读取图片，就可以直接使用这些示例图片：

| code         | object     | code                 | object       | code              | object |
| ------------ | ---------- | -------------------- | ------------ | ----------------- | ------ |
| astronaut    | 宇航员     | coffee               | 一杯咖啡     | lena              | 美女   |
| camera       | 拿相机的人 | coins                | 硬币         | moon              | 月亮   |
| checkerboard | 棋盘       | horse                | 马           | page              | 书页   |
| chelsea      | 小猫       | hubble_deep_field    | 星空         | text              | 文字   |
| clock        | 时钟       | immunohistochemistry | 结肠         | lily              | 不知道 |
| logo         | 商标       | rocket               | DSCOVR照片。 | stereo_motorcycle | 摩托车 |

> microaneurysms
>
> retina
>
> shepp_logan_phantom
>
> skin
>
> cell
>
> human_mitosis

引入方法：

```python
from skimage import io,data
img = data.lena()
io.imshow(img )
```



## 3. 基本属性

```python
print(type(img))  # 显示类型
print(img.shape)  # 显示尺寸
print(img.shape[0])  # 图片高度
print(img.shape[1])  # 图片宽度
print(img.shape[2])	 # 图片通道数
print(img.size)   # 显示总像素个数
print(img.max())  # 最大像素值
print(img.min())  # 最小像素值
print(img.mean())	# 像素平均值
print(img[0][0])	# 图像的像素值
```



## 4. 基本方法

方法很多，基本的IO操作以及图片展示此处不再赘述。

### 4.1 像素的访问与修改

图片读入程序中后，是以numpy数组存在的。因此对numpy数组的一切功能，对图片也适用。对数组元素的访问，实际上就是对图片像素点的访问。

彩色图片访问方式为： `img[i, j, c]`

其中 i 表示图片的行数，j 表示图片的列数，c 表示图片的通道数(RGB三通道分别对应0，1，2）。坐标是从左上角开始。

灰度图片访问方式为： `gray[i, j]`

除了对像素进行读取，也可以采用同样的方式修改像素值。

#### 实例4-1-1：对小猫图片随机添加噪音

```python
from skimage import io,data
import numpy as np
img=data.chelsea()

#随机生成5000个椒盐
rows,cols,dims=img.shape
for i in range(5000):
    x=np.random.randint(0,rows)
    y=np.random.randint(0,cols)
    img[x,y,:]=255
    
io.imshow(img)
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160111173926944-642626720.png)

#### 实例4-1-2：二值化

将lena图片进行二值化，像素值大于128的变为1，否则变为0

```python
from skimage import io,data,color
img=data.lena()
img_gray=color.rgb2gray(img)
rows,cols=img_gray.shape
for i in range(rows):
    for j in range(cols):
        if (img_gray[i,j]<=0.5):
            img_gray[i,j]=0
        else:
            img_gray[i,j]=1
io.imshow(img_gray)
```



![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160111180738413-1323030042.png)



### 4.2 像素的裁剪

通过对数组的裁剪，就可以实现对图片的裁剪。

对多个像素点进行操作，使用数组切片方式访问。切片方式返回的是以指定间隔下标访问 该数组的像素值。

**实例：对小猫图片进行裁剪**

```python
from skimage import io,data
img=data.chelsea()
roi=img[80:180,100:200,:]
io.imshow(roi)
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160111174855897-1556171298.png)

### 4.3 颜色空间及其转换

如前所述，除了直接转换可以改变数据类型外，还可以通过图像的颜色空间转换来改变数据类型。

常用的颜色空间有灰度空间、rgb空间、hsv空间和cmyk空间。颜色空间转换以后，图片类型都变成了float型。

所有的颜色空间转换函数，都放在skimage的color模块内。

#### 实例4-3-1：RGB转灰度图

```python
from skimage import io,data,color
img=data.lena()
gray=color.rgb2gray(img)
io.imshow(gray)
```

其它的转换，用法都是一样的，列举常用的如下：

> skimage.color.rgb2grey(rgb)
>
> skimage.color.rgb2hsv(rgb)
>
> skimage.color.rgb2lab(rgb)
>
> skimage.color.gray2rgb(image)
>
> skimage.color.hsv2rgb(hsv)
>
> skimage.color.lab2rgb(lab)

 实际上，上面的所有转换函数，都可以用一个函数来代替

```python
skimage.color.convert_colorspace(arr, fromspace, tospace)
```

表示将arr从fromspace颜色空间转换到tospace颜色空间。

#### 实例4-3-2：RGB转HSV

```PYTHON
from skimage import io,data,color
img=data.lena()
hsv=color.convert_colorspace(img,'RGB','HSV')
io.imshow(hsv)
```



### 4.4 Matplot图形绘制

#### 实例4-4-1：RGB分布展示

```python
import matplotlib.pyplot as plt
from skimage import data,color

img = data.immunohistochemistry()
hsv = color.rgb2hsv(img)

fig, axes = plt.subplots(2, 2, figsize=(7, 6))
ax0, ax1, ax2, ax3 = axes.ravel()

ax0.imshow(img)
ax0.set_title("Original image")

ax1.imshow(hsv[:, :, 0], cmap=plt.cm.gray)
ax1.set_title("H")

ax2.imshow(hsv[:, :, 1], cmap=plt.cm.gray)
ax2.set_title("S")

ax3.imshow(hsv[:, :, 2], cmap=plt.cm.gray)
ax3.set_title("V")

for ax in axes.ravel():
    ax.axis('off')

fig.tight_layout()  #自动调整subplot间的参数
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160111211022335-245009093.png)

直接用subplots()函数来创建并划分窗口。注意，比前面的subplot()函数多了一个s，该函数格式为：

```python
matplotlib.pyplot.subplots(nrows=1, ncols=1)
```

nrows: 所有子图行数，默认为1。

ncols: 所有子图列数，默认为1。

返回一个窗口figure, 和一个tuple型的ax对象，该对象包含所有的子图,可结合ravel()函数列出所有子图，如：

```python
fig, axes = plt.subplots(2, 2, figsize=(7, 6))
ax0, ax1, ax2, ax3 = axes.ravel()
```

创建了2行2列4个子图，分别取名为ax0,ax1,ax2和ax3, 每个子图的标题用set_title()函数来设置，如：

```python
ax0.imshow(img)
ax0.set_title("Original image")
```

如果有多个子图，我们还可以使用tight_layout()函数来调整显示的布局，该函数格式为：

```python
matplotlib.pyplot.tight_layout(pad=1.08, h_pad=None, w_pad=None, rect=None)
```

所有的参数都是可选的，调用该函数时可省略所有的参数。

pad : 主窗口边缘和子图边缘间的间距，默认为1.08

(h_pad, w_pad) : 子图边缘之间的间距，默认为 pad_inches

rect : 一个矩形区域，如果设置这个值，则将所有的子图调整到这个矩形区域内。

一般调用为：

```python
plt.tight_layout()  #自动调整subplot间的参数
```



除了使用matplotlib库来绘制图片，skimage还有另一个子模块viewer，也提供一个函数来显示图片。不同的是，它利用Qt工具来创建一块画布，从而在画布上绘制图像。

#### 实例4-4-2：viewer绘图

```python
from skimage import data
from skimage.viewer import ImageViewer

img = data.coins()
viewer = ImageViewer(img)
viewer.show()
```

 

#### All in all

| Function     | Function                         | Call format                              |
| ------------ | -------------------------------- | ---------------------------------------- |
| figure       | 创建一个显示窗口                 | plt.figure(num=1,figsize=(8,8)           |
| imshow       | 绘制图片                         | plt.imshow(image)                        |
| show         | 显示窗口                         | plt.show()                               |
| subplot      | 划分子图                         | plt.subplot(2,2,1)                       |
| title        | 设置子图标题(与subplot结合使用） | plt.title('origin image')                |
| axis         | 是否显示坐标尺                   | plt.axis('off')                          |
| subplots     | 创建带有多个子图的窗口           | fig,axes=plt.subplots(2,2,figsize=(8,8)) |
| ravel        | 为每个子图设置变量               | ax0,ax1,ax2,ax3=axes.ravel()             |
| set_title    | 设置子图标题（与axes结合使用）   | ax0.set_title('first window')            |
| tight_layout | 自动调整子图显示布局             | plt.tight_layout()                       |



### 4.5 Generate structuring elements

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from skimage.morphology import (square, rectangle, diamond, disk, cube,
                                octahedron, ball, octagon, star)

# Generate 2D and 3D structuring elements.
struc_2d = {
    "square(15)": square(15),
    "rectangle(15, 10)": rectangle(15, 10),
    "diamond(7)": diamond(7),
    "disk(7)": disk(7),
    "octagon(7, 4)": octagon(7, 4),
    "star(5)": star(5)
}

struc_3d = {
    "cube(11)": cube(11),
    "octahedron(5)": octahedron(5),
    "ball(5)": ball(5)
}

# Visualize the elements.
fig = plt.figure(figsize=(8, 8))

idx = 1
for title, struc in struc_2d.items():
    ax = fig.add_subplot(3, 3, idx)
    ax.imshow(struc, cmap="Paired", vmin=0, vmax=12)
    for i in range(struc.shape[0]):
        for j in range(struc.shape[1]):
            ax.text(j, i, struc[i, j], ha="center", va="center", color="w")
    ax.set_axis_off()
    ax.set_title(title)
    idx += 1

for title, struc in struc_3d.items():
    ax = fig.add_subplot(3, 3, idx, projection=Axes3D.name)
    ax.voxels(struc)
    ax.set_title(title)
    idx += 1

fig.tight_layout()
plt.show()
```

**result：**

![img](https://scikit-image.org/docs/stable/_images/sphx_glr_plot_structuring_elements_001.png)



### 4.6 图片批处理

> 有些时候，我们不仅要对一张图片进行处理，可能还会对一批图片处理。这时候，我们可以通过循环来执行处理，也可以调用程序自带的图片集合来处理。

图片集合函数为：

```python
skimage.io.ImageCollection(load_pattern,load_func=None)
```

这个函数是放在io模块内的，带两个参数，第一个参数 load_pattern ,  表示图片组的路径，可以是一个str字符串。第二个参数 load_func 是一个回调函数，我们对图片进行批量处理就可以通过这个回调函数实现。回调函数默认为 imread() ,即默认这个函数是批量读取图片。

#### 实例4-6-1：图片批处理应用

```python
import skimage.io as io
from skimage import data_dir
pathstr = data_dir + '/*.png'
coll = io.ImageCollection(pathstr)
print(len(coll))
```

显示结果为25, 说明系统自带了25张png的示例图片，这些图片都读取了出来，放在图片集合coll里。如果我们想显示其中一张图片，则可以在后加上一行代码：

```python
io.imshow(coll[10])
```

显示为：

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160112094108975-355009274.png)

如果一个文件夹里，我们既存放了一些jpg格式的图片，又存放了一些png格式的图片，现在想把它们全部读取出来，该怎么做呢?

```python
import skimage.io as io
from skimage import data_dir
str='d:/pic/*.jpg:d:/pic/*.png'
coll = io.ImageCollection(str)
print(len(coll))
```

> 注意这个地方'd:/pic/\*.jpg:d:/pic/\*.png' ，是两个字符串合在一起的，第一个是'd:/pic/\*.jpg', 第二个是'd:/pic/*.png' ，合在一起后，中间用冒号来隔开，这样就可以把d:/pic/文件夹下的jpg和png格式的图片都读取出来。如果还想读取存放在其它地方的图片，也可以一并加进去，只是中间同样用冒号来隔开。

io.ImageCollection()这个函数省略第二个参数，就是批量读取。如果我们不是想批量读取，而是其它批量操作，如批量转换为灰度图，那又该怎么做呢？

那就需要先定义一个函数，然后将这个函数作为第二个参数，如：

```python
from skimage import data_dir,io,color

def convert_gray(f):
    rgb=io.imread(f)
    return color.rgb2gray(rgb)
    
str=data_dir+'/*.png'
coll = io.ImageCollection(str,load_func=convert_gray)
io.imshow(coll[10])
```

![Gray Coffee](https://images2015.cnblogs.com/blog/140867/201601/140867-20160112100545241-256518000.png)

这种批量操作对视频处理是极其有用的，因为视频就是一系列的图片组合。

```python
from skimage import data_dir,io,color

class AVILoader:
    video_file = 'myvideo.avi'

    def __call__(self, frame):
        return video_read(self.video_file, frame)

avi_load = AVILoader()

frames = range(0, 1000, 10) # 0, 10, 20, ...
ic =io.ImageCollection(frames, load_func=avi_load)
```

这段代码的意思，就是将myvideo.avi这个视频中每隔10帧的图片读取出来，放在图片集合中。

得到图片集合以后，我们还可以将这些图片连接起来，构成一个维度更高的数组，连接图片的函数为：

```python
skimage.io.concatenate_images(ic)
```

带一个参数，就是以上的图片集合，如：

```python
from skimage import data_dir,io,color

coll = io.ImageCollection('d:/pic/*.jpg')
mat=io.concatenate_images(coll)
```

使用`concatenate_images(ic)`函数的前提是读取的这些图片尺寸必须一致，否则会出错。我们看看图片连接前后的维度变化：

```python
from skimage import data_dir,io,color

coll = io.ImageCollection('d:/pic/*.jpg')
print(len(coll))      # 连接的图片数量
print(coll[0].shape)   # 连接前的图片尺寸，所有的都一样
mat=io.concatenate_images(coll)
print(mat.shape)  # 连接后的数组尺寸
```

显示结果：

```python
2
(870, 580, 3)
(2, 870, 580, 3)
```

可以看到，将2个3维数组，连接成了一个4维数组

如果我们对图片进行批量操作后，想把操作后的结果保存起来，也是可以办到的。

```python
from skimage import data_dir,io,transform,color
import numpy as np

def convert_gray(f):
		rgb=io.imread(f)    # 依次读取rgb图片
		gray=color.rgb2gray(rgb)   # 将rgb图片转换成灰度图
		dst=transform.resize(gray,(256,256))  # 将灰度图片大小转换为256*256
		return dst
    
str=data_dir+'/*.png'
coll = io.ImageCollection(str,load_func=convert_gray)
for i in range(len(coll)):
    io.imsave('d:/data/'+np.str(i)+'.jpg',coll[i])  # 循环保存图片
```

 结果：

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160112112931163-1932386935.png)

-------

### 4.7 基本图像处理

图像的形变与缩放，使用的是skimage的transform模块，函数比较多，功能齐全。

#### 4.7.1 Resize

**函数格式为：**

```python
skimage.transform.resize(image, output_shape)
```

> image: 需要改变尺寸的图片
>
> output_shape: 新的图片尺寸

```PYTHON
from skimage import transform,data
import matplotlib.pyplot as plt
img = data.camera()
dst=transform.resize(img, (80, 60))
plt.figure('resize')

plt.subplot(121)
plt.title('before resize')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('before resize')
plt.imshow(dst,plt.cm.gray)

plt.show()
```

将camera图片由原来的512\*512大小，变成了80*60大小。从下图中的坐标尺，我们能够看出来：

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160112114807100-2075505818.png)

 

#### 4.7.2 Rescale

函数格式为：

```PYTHON
skimage.transform.rescale(image, scale)
```

scale 参数可以是单个float 数，表示缩放的倍数，也可以是一个float 型的tuple ，如 [0.2, 0.5] ,表示将行列数分开进行缩放

```PYTHON
from skimage import transform,data
img = data.camera()
print(img.shape)  #图片原始大小 
print(transform.rescale(img, 0.1).shape)  #缩小为原来图片大小的0.1倍
print(transform.rescale(img, [0.5,0.25]).shape)  #缩小为原来图片行数一半，列数四分之一
print(transform.rescale(img, 2).shape)   #放大为原来图片大小的2倍
```

结果为：

```PYTHON
(512, 512)
(51, 51)
(256, 128)
(1024, 1024)
```

**Tip：**

transform.rescale将数组视为形状为 shape 的3D图像，图片的颜色通道会与长与宽一起插值，导致降维或者升维，此时，如果不想导致颜色通道的改变，需要传递参数`multichannel=True`。

如果图像是灰色图像，没有通道尺寸，则不需要传递`multichannel=True`标志。这将导致最后一个轴被视为通道，并且会得到不希望的输出。



#### 4.7.3 Rotate

```PYTHON
skimage.transform.rotate(image, angle[, ...],resize=False)
```

angle 参数是个 float类型数，表示旋转的度数

resize 用于控制在旋转时，是否改变大小 ，默认为False

```PYTHON
from skimage import transform,data
import matplotlib.pyplot as plt
img = data.camera()
print(img.shape)  #图片原始大小
img1=transform.rotate(img, 60) #旋转90度，不改变大小 
print(img1.shape)
img2=transform.rotate(img, 30,resize=True)  #旋转30度，同时改变大小
print(img2.shape)   

plt.figure('resize')

plt.subplot(121)
plt.title('rotate 60')
plt.imshow(img1,plt.cm.gray)

plt.subplot(122)
plt.title('rotate  30')
plt.imshow(img2,plt.cm.gray)

plt.show()
```

显示结果:

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160112121554991-2029212755.png)



#### 4.7.4 Pyramid

以多分辨率来解释图像的一种有效但概念简单的结构就是图像金字塔。图像金字塔最初用于**机器视觉和图像压缩**，一幅图像的金字塔是一系列以金字塔形状排列的分辨率逐步降低的图像集合。金字塔的底部是待处理图像的高分辨率表示，而顶部是低分辨率的近似。当向金字塔的上层移动时，尺寸和分辨率就降低。

在此，我们举一个高斯金字塔的应用实例，函数原型为：

```PYTHON
skimage.transform.pyramid_gaussian(image, downscale=2)
```

downscale控制着金字塔的缩放比例，**只返回生成器**，同时，RGB图同样需要锁定颜色通道。

```PYTHON
import numpy as np
import matplotlib.pyplot as plt
from skimage import data,transform

image = data.astronaut()  #载入宇航员图片
rows, cols, dim = image.shape  #获取图片的行数，列数和通道数
pyramid = tuple(transform.pyramid_gaussian(image, downscale=2))  #产生高斯金字塔图像
#共生成了log(512)=9幅金字塔图像，加上原始图像共10幅，pyramid[0]-pyramid[1]

composite_image = np.ones((rows, cols + cols / 2, 3), dtype=np.double)  #生成背景

composite_image[:rows, :cols, :] = pyramid[0]  #融合原始图像

i_row = 0
for p in pyramid[1:]:
    n_rows, n_cols = p.shape[:2]
    composite_image[i_row:i_row + n_rows, cols:cols + n_cols] = p  #循环融合9幅金字塔图像
    i_row += n_rows

plt.imshow(composite_image)
plt.show()
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160112133003397-871722971.png)![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160112133052194-908221509.png)

上右图，就是10张金字塔图像，下标为0的表示原始图像，后面每层的图像行和列变为上一层的一半，直至变为1

除了高斯金字塔外，还有其它的金字塔，如：

```PYTHON
skimage.transform.pyramid_laplacian(image, downscale=2)：
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160112133851538-1964410161.png)



#### 4.7.5 Contrast ratio

##### gamma

原理：I=I^g^

对原图像的像素，进行幂运算，得到新的像素值。公式中的g就是gamma值。

如果gamma>1, 新图像比原图像暗

如果gamma<1,新图像比原图像亮

(0为白色，1为黑色，越大越接近黑色)

函数格式为：

```PYTHON
skimage.exposure.adjust_gamma(image, gamma=1)
```

gamma参数默认为1，原像不发生变化 。

```PYTHON
from skimage import data, exposure, img_as_float
import matplotlib.pyplot as plt
image = img_as_float(data.moon())
gam1= exposure.adjust_gamma(image, 2)   #调暗
gam2= exposure.adjust_gamma(image, 0.5)  #调亮
plt.figure('adjust_gamma',figsize=(8,8))

plt.subplot(131)
plt.title('origin image')
plt.imshow(image,plt.cm.gray)
plt.axis('off')

plt.subplot(132)
plt.title('gamma=2')
plt.imshow(gam1,plt.cm.gray)
plt.axis('off')

plt.subplot(133)
plt.title('gamma=0.5')
plt.imshow(gam2,plt.cm.gray)
plt.axis('off')

plt.show()
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160112142216491-904609334.png)

##### log对数调整

这个刚好和gamma相反

原理：I=log(I)

```PYTHON
from skimage import data, exposure, img_as_float
import matplotlib.pyplot as plt
image = img_as_float(data.moon())
gam1= exposure.adjust_log(image)   #对数调整
plt.figure('adjust_gamma',figsize=(8,8))

plt.subplot(121)
plt.title('origin image')
plt.imshow(image,plt.cm.gray)
plt.axis('off')

plt.subplot(122)
plt.title('log')
plt.imshow(gam1,plt.cm.gray)
plt.axis('off')

plt.show()
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160112142604522-1898975274.png)

##### 判断图像对比度是否偏低

函数：is_low_contrast(img)

返回一个bool值

```PYTHON
from skimage import data, exposure
image =data.moon()
result=exposure.is_low_contrast(image)
print(result)
```

输出为False

 

##### 调整强度

> 将个像素点值按照极差依据一定的数学关系进行重新排布并限制在一定的范围内，从而增大数据差，增大对比度。

函数格式：

```PYTHON
exposure.rescale_intensity(image, in_range='image', out_range='dtype')
```

> in_range 表示输入图片的强度范围，默认为'image', 表示用图像的最大/最小像素值作为范围
>
> out_range 表示输出图片的强度范围，默认为'dtype', 表示用图像的类型的最大/最小值作为范围
>
> 默认情况下，输入图片的[min,max]范围被拉伸到[dtype.min, dtype.max]，如果dtype = uint8,  那么 dtype.min = 0, dtype.max = 255



如果原始像素值不想被拉伸，只是**等比例缩小**，就使用in_range参数，如：

```PYTHON
import numpy as np
from skimage import exposure
image = np.array([51, 102, 153], dtype=np.uint8)
tmp=image*1.0
mat=exposure.rescale_intensity(tmp,in_range=(0,255))
print(mat)
```

输出为：[0.2  0.4  0.6]，即原像素值除以255



如果参数in_range的[main,max]范围要比原始像素值的范围[min,max] 大或者小，那就进行**裁剪**，如：

```PYTHON
mat=exposure.rescale_intensity(tmp,in_range=(0,102))
print(mat)
```

输出 [0.5  1.  1.]，即原像素值除以102，超出1的变为1

如果一个数组里面有**负数**，现在想**调整到正数**，就使用out_range参数。如：

```PYTHON
import numpy as np
from skimage import exposure
image = np.array([-10, 0, 10], dtype=np.int8)
mat=exposure.rescale_intensity(image, out_range=(0, 127))
print(mat)
```

输出 [0  63 127]



#### 4.7.6 Swirl

Image swirling is a non-linear image deformation that creates a whirlpool effect. This example describes the implementation of this transform in `skimage`, as well as the underlying warp mechanism.

##### Image warping

When applying a geometric transformation on an image, we typically make use of a reverse mapping, i.e., for each pixel in the output image, we compute its corresponding position in the input. The reason is that, if we were to do it the other way around (map each input pixel to its new output position), some pixels in the output may be left empty. On the other hand, each output coordinate has exactly one corresponding location in (or outside) the input image, and even if that position is non-integer, we may use interpolation to compute the corresponding image value.

##### Performing a reverse mapping

To perform a geometric warp in `skimage`, you simply need to provide the reverse mapping to the [`skimage.transform.warp()`](https://scikit-image.org/docs/stable/api/skimage.transform.html#skimage.transform.warp) function. E.g., consider the case where we would like to shift an image 50 pixels to the left. The reverse mapping for such a shift would be:

```python
def shift_left(xy):
    xy[:, 0] += 50
    return xy
```

The corresponding call to warp is:

```python
from skimage.transform import warp
warp(image, shift_left)
```

##### The swirl transformation

Consider the coordinate (*x*,*y*) in the output image. The reverse mapping for the swirl transformation first computes, relative to a center (*x*0,*y*0), its polar coordinates,

$\theta=arctan(y/x)\rho=\sqrt{(x−x_0)^2+(y−y_0)^2}$

where `strength` is a parameter for the amount of swirl, `radius` indicates the swirl extent in pixels, and `rotation` adds a rotation angle. The transformation of `radius` into *r* is to ensure that the transformation decays to $\\approx 1/1000^{\mathsf{th}}$ within the specified radius.

![plot swirl](https://scikit-image.org/docs/stable/_images/sphx_glr_plot_swirl_001.png)

```python
import matplotlib.pyplot as plt

from skimage import data
from skimage.transform import swirl


image = data.checkerboard()
swirled = swirl(image, rotation=0, strength=10, radius=120)

fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(8, 3),
                               sharex=True, sharey=True)

ax0.imshow(image, cmap=plt.cm.gray)
ax0.axis('off')
ax1.imshow(swirled, cmap=plt.cm.gray)
ax1.axis('off')

plt.show()
```



### 4.8 采样

按照一定的间隔对图片进行重新采样获取图片。

实例

```python
"""
  Sampling image by using the method of finding the mean
  ratio为采样间隔。采样间隔越大，所得图像的像素数越少，空间分辨率低，图像质量差；
  采样间隔越小，所得图像像素越多，空间分布率高，图像质量好，数据量大。
"""
# load test image
image = data.coffee()
# print(image)
# plt.imshow(image)
# plt.show()
# display the original shape of the image
print(image.shape)
# display the type of the image
print(*type*(image))
# set sampling rate
ratio = 20
# set the shape of the image after sampling
image1 = np.zeros((int(image.shape[0] / ratio), 
                   int(image.shape[1] / ratio),image.shape[2]), 
                  dtype="int32")
# lterate over the image
for i in range(image1.shape[0]):
	for j in range(image1.shape[1]):
		for k in range(image1.shape[2]):
# get the image block that needs to be sampled
			delta = image[i*ratio:(i+1)*ratio, j*ratio:(j+1)*ratio,k]
# calculate the mean and put it in the result image

			image1[i, j, k] = np.mean(delta)
			pass
  	pass
	pass
# print the image after sampling
plt.imshow(image1)
plt.show()
```







## 5. 数据处理

### 5.1  直方图与均衡化

在图像处理中，直方图是非常重要，也是非常有用的一个处理要素。

在skimage库中对直方图的处理，是放在exposure这个模块中。

**1、计算直方图**

函数格式：

```python
skimage.exposure.histogram(image, nbins=256)
```

参数：

> image对象
>
> nbins 分组组数，仅对**float类型**有效，转化可采用**原数组*1.0**的方式

在numpy包中，也提供了一个计算直方图的函数histogram() ,两者大同小义。

返回一个tuple(hist, bins_center), 前一个数组是直方图的统计量，后一个数组是每个bin的中间值

```python
import numpy as np
from skimage import exposure,data
image =data.camera()*1.0
hist1=np.histogram(image, bins=2)   #用numpy包计算直方图
hist2=exposure.histogram(image, nbins=2)  #用skimage计算直方图
print(hist1)
print(hist2)
```

输出：

```python
(array([107432, 154712], dtype=int64), array([ 0., 127.5, 255.]))
(array([107432, 154712], dtype=int64), array([ 63.75, 191.25]))
```

分成两个bin，每个bin的统计量是一样的，但numpy返回的是每个bin的两端的范围值，而skimage返回的是每个bin的中间值

**2、绘制直方图**

绘图都可以调用matplotlib.pyplot库来进行，其中的hist函数可以直接绘制直方图。

调用方式：

```python
n, bins, patches = plt.hist(arr, bins=None, range=None, density=False, 
                            weights=None, cumulative=False, bottom=None,
                            histtype='bar', align='mid', 
                            orientation='vertical', rwidth=None, 
                            log=False, color=None, label=None, 
                            stacked=False, *, data=None, **kwargs)
```

hist的参数非常多，但常用的就这六个，只有第一个是必须的，后面四个可选

> arr: 需要计算直方图的一维数组
>
> bins: 直方图的柱数，可选项，默认为10
>
> density: 是否将得到的直方图向量归一化。默认为0，原属性已废弃。
>
> color: 直方图颜色
>
> edgecolor: 直方图边框颜色
>
> histtype: 直方图类型，{'bar',  'barstacked',  'step',  'stepfilled'}, default: 'bar'}

返回值 ：

> n: 直方图向量，是否归一化由参数normed设定
>
> bins: 返回各个bin的区间范围
>
> patches: 返回每个bin里面包含的数据，是一个list

```python
from skimage import data
import matplotlib.pyplot as plt
img = data.camera()
plt.figure("hist")
arr = img.flatten()
n, bins, patches = plt.hist(arr, bins=256, normed=1, edgecolor='None', 
                            facecolor='red')  
plt.show()
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160112155611975-603549277.png)

其中的flatten()函数是numpy包里面的，用于将二维数组序列化成一维数组。

是按行序列，如：

mat=[[1 2 3

　　　  4 5 6]]

经过 mat.flatten()后，就变成了

mat=[1 2 3 4 5 6]

**3、彩色图片三通道直方图**

一般来说直方图都是征对灰度图的，如果要画rgb图像的三通道直方图，实际上就是三个直方图的叠加。

```python
from skimage import data
import matplotlib.pyplot as plt
img=data.lena()
ar=img[:,:,0].flatten()
plt.hist(ar, bins=256, normed=1,facecolor='r',edgecolor='r',hold=1)
ag=img[:,:,1].flatten()
plt.hist(ag, bins=256, normed=1, facecolor='g',edgecolor='g',hold=1)
ab=img[:,:,2].flatten()
plt.hist(ab, bins=256, normed=1, facecolor='b',edgecolor='b')
plt.show()
```

其中，加一个参数hold=1,表示可以叠加

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160112160410585-2097320572.png)

**4、直方图均衡化**

如果一副图像的像素占有很多的灰度级而且分布均匀，那么这样的图像往往有高对比度和多变的灰度色调。直方图均衡化就是一种能仅靠输入图像直方图信息自动达到这种效果的变换函数。它的基本思想是对图像中像素个数多的灰度级进行展宽，而对图像中像素个数少的灰度进行压缩，从而扩展取值的动态范围，提高了对比度和灰度色调的变化，使图像更加清晰。

```python
from skimage import data,exposure
import matplotlib.pyplot as plt
img=data.moon()
plt.figure("hist",figsize=(8,8))

arr=img.flatten()
plt.subplot(221)
plt.imshow(img,plt.cm.gray)  #原始图像
plt.subplot(222)
plt.hist(arr, bins=256, normed=1,edgecolor='None',facecolor='red') #原始图像直方图

img1=exposure.equalize_hist(img)
arr1=img1.flatten()
plt.subplot(223)
plt.imshow(img1,plt.cm.gray)  #均衡化图像
plt.subplot(224)
plt.hist(arr1, bins=256, normed=1,edgecolor='None',facecolor='red') #均衡化直方图

plt.show()
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160112163656460-1224206984.png)

#### Histogram matching

This example demonstrates the feature of histogram matching. It manipulates the pixels of an input image so that its histogram matches the histogram of the reference image. If the images have multiple channels, the matching is done independently for each channel, as long as the number of channels is equal in the input image and the reference.

Histogram matching can be used as a lightweight normalisation for image processing, such as feature matching, especially in circumstances where the images have been taken from different sources or in different conditions (i.e. lighting).

```python
import matplotlib.pyplot as plt

from skimage import data
from skimage import exposure
from skimage.exposure import match_histograms

reference = data.coffee()
image = data.chelsea()

matched = match_histograms(image, reference, multichannel=True)

fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3),
                                    sharex=True, sharey=True)
for aa in (ax1, ax2, ax3):
    aa.set_axis_off()

ax1.imshow(image)
ax1.set_title('Source')
ax2.imshow(reference)
ax2.set_title('Reference')
ax3.imshow(matched)
ax3.set_title('Matched')

plt.tight_layout()
plt.show()
```

![Source, Reference, Matched](https://scikit-image.org/docs/stable/_images/sphx_glr_plot_histogram_matching_001.png)

To illustrate the effect of the histogram matching, we plot for each RGB channel, the histogram and the cumulative histogram. Clearly, the matched image has the same cumulative histogram as the reference image for each channel.

```python
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(8, 8))


for i, img in enumerate((image, reference, matched)):
    for c, c_color in enumerate(('red', 'green', 'blue')):
        img_hist, bins = exposure.histogram(img[..., c], source_range='dtype')
        axes[c, i].plot(bins, img_hist / img_hist.max())
        img_cdf, bins = exposure.cumulative_distribution(img[..., c])
        axes[c, i].plot(bins, img_cdf)
        axes[c, 0].set_ylabel(c_color)

axes[0, 0].set_title('Source')
axes[0, 1].set_title('Reference')
axes[0, 2].set_title('Matched')

plt.tight_layout()
plt.show()
```

![Source, Reference, Matched](https://scikit-image.org/docs/stable/_images/sphx_glr_plot_histogram_matching_002.png)

### 5.2 图像简单滤波

对图像进行滤波，可以有两种效果：一种是平滑滤波，用来抑制噪声；另一种是微分算子，可以用来检测边缘和特征提取。

skimage库中通过filters模块进行滤波操作。

#### 5.2.1 sobel算子

sobel算子可用来检测边缘

函数格式为：

```python
skimage.filters.sobel(image, mask=None)
```

**实例**

```python
from skimage import data,filters
import matplotlib.pyplot as plt
img = data.camera()
edges = filters.sobel(img)
plt.imshow(edges,plt.cm.gray)
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160112172421585-579522669.png)



#### 5.2.2 roberts算子

roberts算子和sobel算子一样，用于检测边缘，但不同于其他方法：

> **`Image` must be a 2-dimensional array, that is gray image.**

调用格式也是一样的：

```python
edges = filters.roberts(img)
```



#### 5.2.3 scharr算子

功能同sobel，调用格式：

```python
edges = filters.scharr(img)
```



#### 5.2.4 prewitt算子

功能同sobel，调用格式：

```python
edges = filters.prewitt(img)
```



#### 5.2.5 canny算子

canny算子也是用于提取边缘特征，但它不是放在filters模块，而是放在feature模块。但不同于其他方法：

> **`Image` must be a 2-dimensional array, that is gray image.**

函数格式：

```python
skimage.feature.canny(image，sigma=1.0)
```

可以修改sigma的值来调整效果

```python
from skimage import data,filters,feature
import matplotlib.pyplot as plt
img = data.camera()
edges1 = feature.canny(img)   #sigma=1
edges2 = feature.canny(img,sigma=3)   #sigma=3

plt.figure('canny',figsize=(8,8))
plt.subplot(121)
plt.imshow(edges1,plt.cm.gray)  

plt.subplot(122)
plt.imshow(edges2,plt.cm.gray)

plt.show()
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160112174024569-770895433.png)

从结果可以看出，sigma越小，边缘线条越细小。



#### 5.2.6 gabor滤波

gabor滤波可用来进行边缘检测和纹理特征提取。

> **`skimage.filters.gabor_filter`has been removed.  Use`skimage.filters.gabor`instead.**

> **`Image` must be a 2-dimensional array, that is gray image.**

函数调用格式：

```python
skimage.filters.gabor(image, frequency)
```

通过修改frequency值来调整滤波效果，返回一对边缘结果，一个是用真实滤波核的滤波结果，一个是想象的滤波核的滤波结果。

```python
from skimage import data,filters
import matplotlib.pyplot as plt
img = data.camera()
filt_real, filt_imag = filters.gabor(img,frequency=0.6)   

plt.figure('gabor',figsize=(8,8))

plt.subplot(121)
plt.title('filt_real')
plt.imshow(filt_real,plt.cm.gray)  

plt.subplot(122)
plt.title('filt-imag')
plt.imshow(filt_imag,plt.cm.gray)

plt.show()
```

以上为frequency=0.6的结果图。

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160112175805100-1627760924.png)

以上为frequency=0.1的结果图



#### 5.2.7 gaussian滤波

> 图像大多数噪声均属于高斯噪声，因此高斯滤波器(Gauss filter)应用也较广泛。高斯滤波是一种线性平滑滤波，适用于消除高斯噪声，广泛应用于图像去噪。
>
> 高斯滤波后图像被平滑的程度取决于标准差。它的输出是领域像素的加权平均，同时离中心越近的像素权重越高。因此，相对于均值滤波(mean filter）它的平滑效果更柔和，而且边缘保留的也更好。
>
> 高斯滤波被用作为平滑滤波器的本质原因是因为它是一个低通滤波器(让某一频率以下的信号分量通过，而对该频率以上的信号分量大大抑制）

调用函数为：

```python
skimage.filters.gaussian(image, sigma)
```

通过调节sigma的值来调整滤波效果

```python
from skimage import data,filters
import matplotlib.pyplot as plt
img = data.astronaut()
edges1 = filters.gaussian(img,sigma=0.4)   #sigma=0.4
edges2 = filters.gaussian(img,sigma=5)   #sigma=5

plt.figure('gaussian',figsize=(8,8))
plt.subplot(121)
plt.imshow(edges1,plt.cm.gray)  

plt.subplot(122)
plt.imshow(edges2,plt.cm.gray)

plt.show()
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160112180630600-1668779591.png)

可见sigma越大，过滤后的图像越模糊。



#### 5.2.8 median滤波

中值滤波，一种平滑滤波，可以消除噪声。

需要用skimage.morphology模块来设置滤波器的形状。

```python
skimage.filters.median(image, selem=None, out=None, mode='nearest', 
cval=0.0, behavior='ndimage')
```

> **`Image` must be a 2-dimensional array, that is gray image.**

**Parameters**

> **image**			array-like
>
> Input image.
>
> **selem**			ndarray, optional
>
> If `behavior=='rank'`, `selem` is a 2-D array of 1's and 0's. If `behavior=='ndimage'`, `selem` is a N-D array of 1's and 0's with the same number of dimension than `image`. If None, `selem` will be a N-D array with 3 elements for each dimension (e.g., vector, square, cube, etc.)
>
> **out	**			ndarray, (same dtype as image), optional
>
> If None, a new array is allocated.
>
> **mode**			{'reflect', 'constant', 'nearest', 'mirror', 'wrap'}, optional
>
> The mode parameter determines how the array borders are handled, where `cval` is the value when mode is equal to 'constant'. Default is 'nearest'.New in version 0.15: `mode` is used when `behavior='ndimage'`.
>
> **cval**				scalar, optional
>
> Value to fill past edges of input if mode is 'constant'. Default is 0.0New in version 0.15: `cval` was added in 0.15 is used when `behavior='ndimage'`.
>
> **behavior**		{'ndimage',  'rank'}, optional
>
> Either to use the old behavior (i.e., < 0.15) or the new behavior. The old behavior will call the `skimage.filters.rank.median()`. The new behavior will call the `scipy.ndimage.median_filter()`. Default is 'ndimage'.New in version 0.15: `behavior` is introduced in 0.15Changed in version 0.16: Default `behavior` has been changed from 'rank' to 'ndimage'



```python
from skimage import data,filters
import matplotlib.pyplot as plt
from skimage.morphology import disk
img = data.camera()
edges1 = filters.median(img,disk(5))
edges2= filters.median(img,disk(9))

plt.figure('median',figsize=(8,8))

plt.subplot(121)
plt.imshow(edges1,plt.cm.gray)  

plt.subplot(122)
plt.imshow(edges2,plt.cm.gray)

plt.show()
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160112182116053-1956206043.png)

从结果可以看出，滤波器越大，图像越模糊。



#### 5.2.9 水平、垂直边缘检测

上边所举的例子都是进行全部边缘检测，有些时候我们只需要检测水平边缘，或垂直边缘，就可用下面的方法。

> **`Image` must be a 2-dimensional array, that is gray image.**

水平边缘检测：sobel_h, prewitt_h, scharr_h

垂直边缘检测： sobel_v, prewitt_v, scharr_v

```python
from skimage import data,filters
import matplotlib.pyplot as plt
img = data.camera()
edges1 = filters.sobel_h(img)  
edges2 = filters.sobel_v(img) 

plt.figure('sobel_v_h',figsize=(8,8))

plt.subplot(121)
plt.imshow(edges1,plt.cm.gray)  

plt.subplot(122)
plt.imshow(edges2,plt.cm.gray)

plt.show()
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160112181548678-424625426.png)

上边左图为检测出的水平边缘，右图为检测出的垂直边缘。



#### 5.2.10 交叉边缘检测

可使用Roberts的十字交叉核来进行过滤，以达到检测交叉边缘的目的。这些交叉边缘实际上是梯度在某个方向上的一个分量。

> **`Image` must be a 2-dimensional array, that is gray image.**

其中一个核：

```
 0   1
-1   0
```

对应的函数：

```python
roberts_neg_diag(image)
```

 例：

```python
from skimage import data,filters
import matplotlib.pyplot as plt
img =data.camera()
dst =filters.roberts_neg_diag(img) 

plt.figure('filters',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('filted image')
plt.imshow(dst,plt.cm.gray)
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160115143207303-1110393879.png)

另外一个核：

```python
1   0
0  -1
```

对应函数为：

```python
roberts_pos_diag(image）
```

**实例**

```python
from skimage import data,filters
import matplotlib.pyplot as plt
img =data.camera()
dst =filters.roberts_pos_diag(img) 

plt.figure('filters',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('filted image')
plt.imshow(dst,plt.cm.gray)
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160115143403757-1522337026.png)



### 5.3 图像自动阈值分割

图像阈值分割是一种广泛应用的分割技术，利用图像中要提取的目标区域与其背景在灰度特性上的差异，把图像看作具有不同灰度级的两类区域(目标区域和背景区域)的组合，选取一个比较合理的阈值，以确定图像中每个像素点应该属于目标区域还是背景区域，从而产生相应的二值图像。

在skimage库中，阈值分割的功能是放在filters模块中。

我们可以手动指定一个阈值，从而来实现分割。也可以让系统自动生成一个阈值，下面几种方法就是用来自动生成阈值。

#### 5.3.1 threshold_otsu

基于Otsu的阈值分割方法，函数调用格式：

```python
skimage.filters.threshold_otsu(image, nbins=256)
```

参数image是指灰度图像，返回一个阈值。

```python
from skimage import data,filters
import matplotlib.pyplot as plt
image = data.camera()
thresh = filters.threshold_otsu(image)   #返回一个阈值
dst =(image <= thresh)*1.0   #根据阈值进行分割

plt.figure('thresh',figsize=(8,8))

plt.subplot(121)
plt.title('original image')
plt.imshow(image,plt.cm.gray)

plt.subplot(122)
plt.title('binary image')
plt.imshow(dst,plt.cm.gray)

plt.show()
```

返回阈值为87，根据87进行分割得下图:

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160114171601053-1017024447.png)

#### 5.3.2 threshold_yen

使用方法同上：

```python
thresh = filters.threshold_yen(image) 
```

返回阈值为198，分割如下图：

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160114171909460-229103995.png)

#### 5.3.3 threshold_li

使用方法同上：

```python
thresh = filters.threshold_li(image)
```

返回阈值64.5，分割如下图：

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160114172121038-976915406.png)

#### 5.3.4 threshold_isodata

阈值计算方法：

```python
threshold = (image[image <= threshold].mean() +
             image[image > threshold].mean()) / 2.0
```

使用方法同上：

```python
thresh = filters.threshold_isodata(image)
```

返回阈值为87，因此分割效果和threshold_otsu一样。

#### 5.3.5 threshold_local

调用函数为：

```python
skimage.filters.threshold_local(image, block_size, method='gaussian', 
                                offset=0, mode='reflect', param=None, 
                                cval=0)
```

Compute a threshold mask image based on local pixel neighborhood.

Also known as adaptive or dynamic thresholding. The threshold value is the weighted mean for the local neighborhood of a pixel subtracted by a constant. Alternatively the threshold can be determined dynamically by a given function, using the 'generic' method.

**Parameters**

> **image**
>
> (N, M[, …, P]) ndarray
>
> Grayscale input image.
>
> **block_size**
>
> int or sequence of int
>
> Odd size of pixel neighborhood which is used to calculate the threshold value (e.g. 3, 5, 7, …, 21, …).
>
> **method**
>
> {'generic',  'gaussian',  'mean',  'median'}, optional
>
> Method used to determine adaptive threshold for local neighbourhood in weighted mean image.'generic': use custom function (see `param` parameter)'gaussian': apply gaussian filter (see `param` parameter for custom sigma value)'mean': apply arithmetic mean filter'median': apply median rank filterBy default the 'gaussian' method is used.
>
> **offset**
>
> float, optional
>
> Constant subtracted from weighted mean of neighborhood to calculate the local threshold value. Default offset is 0.
>
> **mode**
>
> {'reflect',  'constant',  'nearest',  'mirror',  'wrap'}, optional
>
> The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to 'constant'.  Default is 'reflect'.
>
> **param**
>
> {int, function}, optional
>
> Either specify sigma for 'gaussian' method or function object for 'generic' method. This functions takes the flat array of local neighbourhood as a single argument and returns the calculated threshold for the centre pixel.
>
> **cval**
>
> float, optional
>
> Value to fill past edges of input if mode is 'constant'.

**Returns**

> **threshold**
>
> (N, M[, …, P]) ndarrayThreshold image. All pixels in the input image higher than the corresponding pixel in the threshold image are considered foreground.

block_size: 块大小，指当前像素的相邻区域大小，一般是奇数(如3，5，7。。。）

method: 用来确定自适应阈值的方法，有'mean', 'generic', 'gaussian' 和 'median'。省略时默认为gaussian

该函数直接访问一个阈值后的图像，而不是阈值。

```python
image = data.camera()
dst =filters.threshold_local(image, 15) #返回一个阈值图像

plt.figure('thresh',figsize=(8,8))

plt.subplot(121)
plt.title('original image')
plt.imshow(image,plt.cm.gray)

plt.subplot(122)
plt.title('binary image')
plt.imshow(dst,plt.cm.gray)

plt.show()
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160114174026069-1947238729.png)

大家可以修改block_size的大小和method值来查看更多的效果。如：

```python
dst1 =filters.threshold_local(image,31,'mean') 
dst2 =filters.threshold_local(image,5,'median')
```

两种效果如下：

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160114174317553-483158220.png)



### 5.4 基本图形的绘制

图形包括线条、圆形、椭圆形、多边形等。

在skimage包中，绘制图形用的是draw模块，不要和绘制图像搞混了。

#### 5.4.1 画线条

函数调用格式为：

```python
skimage.draw.line(r1,c1,r2,c2)
```

r1,r2: 开始点的行数和结束点的行数

c1,c2: 开始点的列数和结束点的列数

返回当前绘制图形上所有点的坐标，如：

```python
rr, cc =draw.line(1, 5, 8, 2)
```

表示从(1，5）到(8，2）连一条线，返回线上所有的像素点坐标[rr,cc]

```python
from skimage import draw,data
import matplotlib.pyplot as plt
img=data.chelsea()
rr, cc =draw.line(1, 150, 470, 450)
img[rr, cc] =255
plt.imshow(img,plt.cm.gray)
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160114182442194-2142227060.png)

如果想画其它颜色的线条，则可以使用set_color(）函数，格式为：

```python
skimage.draw.set_color(img, coords, color)
```

例：绘制红色线条。

```python
from skimage import draw,data
import matplotlib.pyplot as plt
img=data.chelsea()
rr, cc =draw.line(1, 150, 270, 250)
draw.set_color(img,[rr,cc],[0,0,255])
plt.imshow(img,plt.cm.gray)
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160114182859241-4704866.png)

#### 5.4.2 画圆

函数格式：

```python
skimage.draw.circle(cy, cx, radius）
```

cy和cx表示圆心点，radius表示半径

```python
from skimage import draw,data
import matplotlib.pyplot as plt
img=data.chelsea()
rr, cc=draw.circle(150,150,50)
draw.set_color(img,[rr,cc],[255,0,0])
plt.imshow(img,plt.cm.gray)
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160114183742022-1207630354.png)

#### 5.4.3 多边形

函数格式：

```python
skimage.draw.polygon(Y,X)
```

Y为多边形顶点的行集合，X为各顶点的列值集合。

```python
from skimage import draw,data
import matplotlib.pyplot as plt
import numpy as np
img=data.chelsea()
Y=np.array([10,10,60,60])
X=np.array([200,400,400,200])
rr, cc=draw.polygon(Y,X)
draw.set_color(img,[rr,cc],[255,0,0])
plt.imshow(img,plt.cm.gray)
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160114184505241-2000875584.png)

我在此处只设置了四个顶点，因此是个四边形。

#### 5.4.4 椭圆

格式：

```python
skimage.draw.ellipse(cy, cx, yradius, xradius）
```

cy和cx为中心点坐标，yradius和xradius代表长短轴。

```python
from skimage import draw,data
import matplotlib.pyplot as plt
img=data.chelsea()
rr, cc=draw.ellipse(150, 150, 30, 80)
draw.set_color(img,[rr,cc],[255,0,0])
plt.imshow(img,plt.cm.gray)
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160114184931600-1746813110.png)

#### 5.4.5 贝塞儿曲线

格式：

```python
skimage.draw.bezier_curve(y1,x1,y2,x2,y3,x3,weight)
```

y1,x1表示第一个控制点坐标

y2,x2表示第二个控制点坐标

y3,x3表示第三个控制点坐标

weight表示中间控制点的权重，用于控制曲线的弯曲度。

```python
from skimage import draw,data
import matplotlib.pyplot as plt
img=data.chelsea()
rr, cc=draw.bezier_curve(150,50,50,280,260,400,2)
draw.set_color(img,[rr,cc],[255,0,0])
plt.imshow(img,plt.cm.gray)
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160114185637100-589550175.png)

#### 5.4.6 画空心圆

和前面的画圆是一样的，只是前面是实心圆，而此处画空心圆，只有边框线。

格式：

```python
skimage.draw.circle_perimeter(yx,yc,radius)
```

yx,yc是圆心坐标，radius是半径

```python
from skimage import draw,data
import matplotlib.pyplot as plt
img=data.chelsea()
rr, cc=draw.circle_perimeter(150,150,50)
draw.set_color(img,[rr,cc],[255,0,0])
plt.imshow(img,plt.cm.gray)
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160114190012725-22593896.png)

#### 5.4.7 空心椭圆

格式：

```python
skimage.draw.ellipse_perimeter(cy, cx, yradius, xradius）
```

cy,cx表示圆心

yradius,xradius表示长短轴

```python
from skimage import draw,data
import matplotlib.pyplot as plt
img=data.chelsea()
rr, cc=draw.ellipse_perimeter(150, 150, 30, 80)
draw.set_color(img,[rr,cc],[255,0,0])
plt.imshow(img,plt.cm.gray)
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160114190319913-31478197.png)



### 5.5 基本形态学处理

对图像进行形态学变换。变换对象一般为灰度图或二值图，功能函数放在morphology子模块内。

#### 5.5.1 膨胀(dilation)

原理：一般对**二值图像或灰度图**进行操作。找到像素值为1的点，将它的邻近像素点都设置成这个值。1值表示白，0值表示黑，因此**膨胀操作可以扩大白色值范围，压缩黑色值范围。一般用来扩充边缘或填充小的孔洞。**

若输入RGB图，则会返回IndexError。

功能函数：

```python
skimage.morphology.dilation(image, selem=None)
```

selem表示结构元素，用于设定局部区域的形状和大小。

```python
from skimage import data
import skimage.morphology as sm
import matplotlib.pyplot as plt
img=data.checkerboard()
dst1=sm.dilation(img,sm.square(5))  #用边长为5的正方形滤波器进行膨胀滤波
dst2=sm.dilation(img,sm.square(15))  #用边长为15的正方形滤波器进行膨胀滤波

plt.figure('morphology',figsize=(8,8))
plt.subplot(131)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(132)
plt.title('morphological image')
plt.imshow(dst1,plt.cm.gray)

plt.subplot(133)
plt.title('morphological image')
plt.imshow(dst2,plt.cm.gray)
```

分别用边长为5或15的正方形滤波器对棋盘图片进行膨胀操作，结果如下：

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160115095959350-212020996.png)

可见滤波器的大小，对操作结果的影响非常大。一般设置为奇数。

除了正方形的滤波器外，滤波器的形状还有一些，现列举如下：

> morphology.square: 正方形
>
> morphology.disk:  平面圆形
>
> morphology.ball: 球形
>
> morphology.cube: 立方体形
>
> morphology.diamond: 钻石形
>
> morphology.rectangle: 矩形
>
> morphology.star: 星形
>
> morphology.octagon: 八角形
>
> morphology.octahedron： 八面体

注意，如果处理图像为二值图像(只有0和1两个值），则可以调用：

```python
skimage.morphology.binary_dilation(image, selem=None)
```

用此函数比处理灰度图像要快。



#### 5.5.2 腐蚀(erosion)

函数：

```python
skimage.morphology.erosion(image, selem=None)
```

selem表示结构元素，用于设定局部区域的形状和大小。

和膨胀相反的操作，将0值扩充到邻近像素。扩大黑色部分，减小白色部分。可用来提取骨干信息，去掉毛刺，去掉孤立的像素。

```python
from skimage import data
import skimage.morphology as sm
import matplotlib.pyplot as plt
img=data.checkerboard()
dst1=sm.erosion(img,sm.square(5))  #用边长为5的正方形滤波器进行膨胀滤波
dst2=sm.erosion(img,sm.square(25))  #用边长为25的正方形滤波器进行膨胀滤波

plt.figure('morphology',figsize=(8,8))
plt.subplot(131)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(132)
plt.title('morphological image')
plt.imshow(dst1,plt.cm.gray)

plt.subplot(133)
plt.title('morphological image')
plt.imshow(dst2,plt.cm.gray)
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160115101502835-2057654714.png)

注意，如果处理图像为二值图像(只有0和1两个值），则可以调用：

```python
skimage.morphology.binary_erosion(image, selem=None)
```

用此函数比处理灰度图像要快。



#### 5.5.3 开运算(opening)

函数：

```python
skimage.morphology.openning(image, selem=None)
```

selem表示结构元素，用于设定局部区域的形状和大小。

**先腐蚀再膨胀，可以消除小物体或小斑块。**

```python
from skimage import io,color
import skimage.morphology as sm
import matplotlib.pyplot as plt
img=color.rgb2gray(io.imread('d:/pic/mor.png'))
dst=sm.opening(img,sm.disk(9))  #用边长为9的圆形滤波器进行膨胀滤波

plt.figure('morphology',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)
plt.axis('off')

plt.subplot(122)
plt.title('morphological image')
plt.imshow(dst,plt.cm.gray)
plt.axis('off')
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160115104308663-472327996.png)

注意，如果处理图像为二值图像(只有0和1两个值），则可以调用：

```python
skimage.morphology.binary_opening(image, selem=None)
```

用此函数比处理灰度图像要快。



#### 5.5.4 闭运算(closing)

函数：

```python
skimage.morphology.closing(image, selem=None)
```

selem表示结构元素，用于设定局部区域的形状和大小。

**先膨胀再腐蚀，可用来填充孔洞。**

```python
from skimage import io,color
import skimage.morphology as sm
import matplotlib.pyplot as plt
img=color.rgb2gray(io.imread('d:/pic/mor.png'))
dst=sm.closing(img,sm.disk(9))  #用边长为5的圆形滤波器进行膨胀滤波

plt.figure('morphology',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)
plt.axis('off')

plt.subplot(122)
plt.title('morphological image')
plt.imshow(dst,plt.cm.gray)
plt.axis('off')
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160115104400694-2008040157.png)

注意，如果处理图像为二值图像(只有0和1两个值），则可以调用：

```python
skimage.morphology.binary_closing(image, selem=None)
```

用此函数比处理灰度图像要快。



#### 5.5.5 白帽(white-tophat)

函数：

```python
skimage.morphology.white_tophat(image, selem=None)
```

selem表示结构元素，用于设定局部区域的形状和大小。

**将原图像减去它的开运算值，返回比结构化元素小的白点**

```python
from skimage import io,color
import skimage.morphology as sm
import matplotlib.pyplot as plt
img=color.rgb2gray(io.imread('d:/pic/mor.png'))
dst=sm.white_tophat(img,sm.square(21))  

plt.figure('morphology',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)
plt.axis('off')

plt.subplot(122)
plt.title('morphological image')
plt.imshow(dst,plt.cm.gray)
plt.axis('off')
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160115105131632-38243992.png)

**实例：Removing small objects in grayscale images with a top hat filter**

This example shows how to remove small objects from grayscale images. The top-hat transform [1](https://scikit-image.org/docs/stable/auto_examples/filters/plot_tophat.html#id2) is an operation that extracts small elements and details from given images. Here we use a white top-hat transform, which is defined as the difference between the input image and its (mathematical morphology) opening.

![Original, White tophat, Complementary](https://scikit-image.org/docs/stable/_images/sphx_glr_plot_tophat_001.png)

```python
import numpy as np
import matplotlib.pyplot as plt

from skimage import data
from skimage import color, morphology

image = color.rgb2gray(data.hubble_deep_field())[:500, :500]

selem =  morphology.disk(1)
res = morphology.white_tophat(image, selem)

fig, ax = plt.subplots(ncols=3, figsize=(20, 8))
ax[0].set_title('Original')
ax[0].imshow(image, cmap='gray')
ax[1].set_title('White tophat')
ax[1].imshow(res, cmap='gray')
ax[2].set_title('Complementary')
ax[2].imshow(image - res, cmap='gray')

plt.show()
```



#### 5.5.6 黑帽(black-tophat)

函数：

```python
skimage.morphology.black_tophat(image, selem=None)
```

selem表示结构元素，用于设定局部区域的形状和大小。

**将原图像减去它的闭运算值，返回比结构化元素小的黑点，且将这些黑点反色。**

```python
from skimage import io,color
import skimage.morphology as sm
import matplotlib.pyplot as plt
img=color.rgb2gray(io.imread('d:/pic/mor.png'))
dst=sm.black_tophat(img,sm.square(21))  

plt.figure('morphology',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)
plt.axis('off')

plt.subplot(122)
plt.title('morphological image')
plt.imshow(dst,plt.cm.gray)
plt.axis('off')
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160115105418538-962346927.png)



### 5.6 高级滤波

这些方法需要用户自己设定滤波器的形状和大小，因此需要导入morphology模块来设定。

#### 5.6.1 autolevel

这个词在photoshop里面翻译成自动色阶，用局部直方图来对图片进行滤波分级。

该滤波器局部地拉伸灰度像素值的直方图，以覆盖整个像素值范围。

格式：

```python
skimage.filters.rank.autolevel(image, selem)
```

selem表示结构化元素，用于设定滤波器。

```python
from skimage import data,color
import matplotlib.pyplot as plt
from skimage.morphology import disk
import skimage.filters.rank as sfr
img =color.rgb2gray(data.lena())
auto =sfr.autolevel(img, disk(5))  #半径为5的圆形滤波器

plt.figure('filters',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('filted image')
plt.imshow(auto,plt.cm.gray)
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160115092410225-1805475573.png)

#### 5.6.2 bottomhat 与 tophat

bottomhat: 此滤波器先计算图像的形态学闭运算，然后用原图像减去运算的结果值，有点像黑帽操作。

tophat: 此滤波器先计算图像的形态学开运算，然后用原图像减去运算的结果值，有点像白帽操作。

格式：

```python
skimage.filters.rank.bottomhat(image, selem)
skimage.filters.rank.tophat(image, selem)
```

selem表示结构化元素，用于设定滤波器。

下面是bottomhat滤波的例子：

```python
from skimage import data,color
import matplotlib.pyplot as plt
from skimage.morphology import disk
import skimage.filters.rank as sfr
img =color.rgb2gray(data.lena())
auto =sfr.bottomhat(img, disk(5))  #半径为5的圆形滤波器

plt.figure('filters',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('filted image')
plt.imshow(auto,plt.cm.gray)
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160115110840397-1123644996.png)

#### 5.6.3 enhance_contrast

对比度增强。求出局部区域的最大值和最小值，然后看当前点像素值最接近最大值还是最小值，然后替换为最大值或最小值。

函数： 

```python
enhance_contrast(image, selem)
```

selem表示结构化元素，用于设定滤波器。

```python
from skimage import data,color
import matplotlib.pyplot as plt
from skimage.morphology import disk
import skimage.filters.rank as sfr
img =color.rgb2gray(data.lena())
auto =sfr.enhance_contrast(img, disk(5))  #半径为5的圆形滤波器

plt.figure('filters',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('filted image')
plt.imshow(auto,plt.cm.gray)
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160115123542882-284365071.png)

#### 5.6.4 entropy

求局部熵，熵是使用基为2的对数运算出来的。该函数将局部区域的灰度值分布进行二进制编码，返回编码的最小值。

函数格式：

```python
entropy(image, selem)
```

selem表示结构化元素，用于设定滤波器。

```python
from skimage import data,color
import matplotlib.pyplot as plt
from skimage.morphology import disk
import skimage.filters.rank as sfr
img =color.rgb2gray(data.lena())
dst =sfr.entropy(img, disk(5))  #半径为5的圆形滤波器

plt.figure('filters',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('filted image')
plt.imshow(dst,plt.cm.gray)
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160115124955178-698384740.png)

#### 5.6.5 equalize

均衡化滤波。利用局部直方图对图像进行均衡化滤波。

函数格式：equalize(image, selem）

selem表示结构化元素，用于设定滤波器。

```python
from skimage import data,color
import matplotlib.pyplot as plt
from skimage.morphology import disk
import skimage.filters.rank as sfr
img =color.rgb2gray(data.lena())
dst =sfr.equalize(img, disk(5))  #半径为5的圆形滤波器

plt.figure('filters',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('filted image')
plt.imshow(dst,plt.cm.gray)
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160115125738647-16345677.png)

#### 5.6.6 gradient

返回图像的局部梯度值(如：最大值-最小值），用此梯度值代替区域内所有像素值。

函数格式：gradient(image, selem）

selem表示结构化元素，用于设定滤波器。

```python
from skimage import data,color
import matplotlib.pyplot as plt
from skimage.morphology import disk
import skimage.filters.rank as sfr
img =color.rgb2gray(data.lena())
dst =sfr.gradient(img, disk(5))  #半径为5的圆形滤波器

plt.figure('filters',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('filted image')
plt.imshow(dst,plt.cm.gray)
```

![img](https://images2015.cnblogs.com/blog/140867/201601/140867-20160115130606303-762382147.png)

#### 5.6.7 其它滤波器

滤波方式很多，下面不再一一详细讲解，仅给出核心代码，所有的函数调用方式都是一样的。

**最大值滤波器(maximum)**

返回图像局部区域的最大值，用此最大值代替该区域内所有像素值。

```python
dst =sfr.maximum(img, disk(5)) 
```

**最小值滤波器(minimum)**

返回图像局部区域内的最小值，用此最小值取代该区域内所有像素值。

```python
dst =sfr.minimum(img, disk(5))
```

**均值滤波器(mean)**

返回图像局部区域内的均值，用此均值取代该区域内所有像素值。

```python
dst =sfr.mean(img, disk(5)) 
```

**中值滤波器(median)**

返回图像局部区域内的中值，用此中值取代该区域内所有像素值。

```python
dst =sfr.median(img, disk(5))
```

**莫代尔滤波器(modal)**

返回图像局部区域内的modal值，用此值取代该区域内所有像素值。

```python
dst =sfr.modal(img, disk(5))
```

**otsu阈值滤波(otsu)**

返回图像局部区域内的otsu阈值，用此值取代该区域内所有像素值。

```python
dst =sfr.otsu(img, disk(5))
```

**阈值滤波(threshhold)**

将图像局部区域中的每个像素值与均值比较，大于则赋值为1，小于赋值为0，得到一个二值图像。

```python
dst =sfr.threshold(img, disk(5)) 
```

**减均值滤波(subtract_mean)**  

将局部区域中的每一个像素，减去该区域中的均值。

```python
dst =sfr.subtract_mean(img, disk(5))
```

**求和滤波(sum)** 

求局部区域的像素总和，用此值取代该区域内所有像素值。

```python
dst =sfr.sum(img, disk(5))
```



### 5.7 霍夫线变换

#### 5.7.1 霍夫变换

在图片处理中，**霍夫变换主要是用来检测图片中的几何形状，包括直线、圆、椭圆等**。

在skimage中，霍夫变换是放在tranform模块内，本篇主要讲解霍夫线变换。

对于平面中的一条直线，在笛卡尔坐标系中，可用y=mx+b来表示，其中m为斜率，b为截距。但是如果直线是一条垂直线，则m为无穷大，所有通常我们在另一坐标系中表示直线，即极坐标系下的r=xcos(theta)+ysin(theta)。即可用（r,theta）来表示一条直线。其中r为该直线到原点的距离，theta为该直线的垂线与x轴的夹角。如下图所示。

 ![img](https://upload-images.jianshu.io/upload_images/1496926-ebaef7f44178600a.gif)

对于一个给定的点（x0,y0), 我们在极坐标下绘出所有通过它的直线（r,theta)，将得到一条正弦曲线。如果将图片中的所有非0点的正弦曲线都绘制出来，则会存在一些交点。所有经过这个交点的正弦曲线，说明都拥有同样的(r,theta), 意味着这些点在一条直线上。

![img](https://upload-images.jianshu.io/upload_images/1496926-f2cb4e1dc09f3cd3.jpg)


发上图所示，三个点(对应图中的三条正弦曲线）在一条直线上，因为这三个曲线交于一点，具有相同的（r, theta)。霍夫线变换就是利用这种方法来寻找图中的直线。
函数：

```python
skimage.transform.hough_line(img)
```

> 返回三个值：
>
> h: 霍夫变换累积器
>
> theta: 点与x轴的夹角集合，一般为0-179度
>
> distance: 点到原点的距离，即上面的所说的r.

例：

```python
import skimage.transform as st
import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline

# 构建测试图片
image = np.zeros((100, 100))  #背景图
idx = np.arange(25, 75)    #25-74序列
image[idx[::-1], idx] = 255  # 线条\
image[idx, idx] = 255        # 线条/

# hough线变换
h, theta, d = st.hough_line(image)

#生成一个一行两列的窗口（可显示两张图片）.
fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(8, 6))
plt.tight_layout()

#显示原始图片
ax0.imshow(image, plt.cm.gray)
ax0.set_title('Input image')
ax0.set_axis_off()

#显示hough变换所得数据
ax1.imshow(np.log(1 + h))
ax1.set_title('Hough transform')
ax1.set_xlabel('Angles (degrees)')
ax1.set_ylabel('Distance (pixels)')
ax1.axis('image')
plt.show()
```

![img](https://upload-images.jianshu.io/upload_images/1496926-8673cb03d731099b.png)

从右边那张图可以看出，有两个交点，说明原图像中有两条直线。
如果我们要把图中的两条直线绘制出来，则需要用到另外一个函数：

```python
skimage.transform.hough_line_peaks(hspace, angles, dists）
```

用这个函数可以取出峰值点，即交点，也即原图中的直线。
返回的参数与输入的参数一样。我们修改一下上边的程序，在原图中将两直线绘制出来。

```python
import skimage.transform as st
import numpy as np
import matplotlib.pyplot as plt

# 构建测试图片
image = np.zeros((100, 100))  #背景图
idx = np.arange(25, 75)    #25-74序列
image[idx[::-1], idx] = 255  # 线条\
image[idx, idx] = 255        # 线条/

# hough线变换
h, theta, d = st.hough_line(image)

#生成一个一行三列的窗口（可显示三张图片）.
fig, (ax0, ax1,ax2) = plt.subplots(1, 3, figsize=(8, 6))
plt.tight_layout()

#显示原始图片
ax0.imshow(image, plt.cm.gray)
ax0.set_title('Input image')
ax0.set_axis_off()

#显示hough变换所得数据
ax1.imshow(np.log(1 + h))
ax1.set_title('Hough transform')
ax1.set_xlabel('Angles (degrees)')
ax1.set_ylabel('Distance (pixels)')
ax1.axis('image')

#显示检测出的线条
ax2.imshow(image, plt.cm.gray)
row1, col1 = image.shape
for _, angle, dist in zip(*st.hough_line_peaks(h, theta, d)):
    y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
    y1 = (dist - col1 * np.cos(angle)) / np.sin(angle)
    ax2.plot((0, col1), (y0, y1), '-r')
ax2.axis((0, col1, row1, 0))
ax2.set_title('Detected lines')
ax2.set_axis_off()
plt.show()
```

![img](https://upload-images.jianshu.io/upload_images/1496926-ece726bc9b1d7442.png)

注意，绘制线条的时候，要从极坐标转换为笛卡尔坐标，公式为： 

![img](https://upload-images.jianshu.io/upload_images/1496926-919808695ab6c395.gif)

skimage还提供了另外一个检测直线的霍夫变换函数，

概率霍夫线变换：

```python
skimage.transform.probabilistic_hough_line(img, threshold=10, 
                                           line_length=5,line_gap=3)
```

参数：

> img: 待检测的图像。
>
> threshold： 阈值，可先项，默认为10
>
> line_length: 检测的最短线条长度，默认为50
>
> line_gap: 线条间的最大间隙。增大这个值可以合并破碎的线条。默认为10

返回：

> lines: 线条列表, 格式如((x0, y0), (x1, y0))，标明开始点和结束点。

下面，我们用canny算子提取边缘，然后检测哪些边缘是直线？

```python
import skimage.transform as st
import matplotlib.pyplot as plt
from skimage import data,feature

#使用Probabilistic Hough Transform.
image = data.camera()
edges = feature.canny(image, sigma=2, low_threshold=1, high_threshold=25)
lines = st.probabilistic_hough_line(edges, threshold=10, line_length=5,line_gap=3)
print(len(lines))
# 创建显示窗口.
fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(16, 6))
plt.tight_layout()

#显示原图像
ax0.imshow(image, plt.cm.gray)
ax0.set_title('Input image')
ax0.set_axis_off()

#显示canny边缘
ax1.imshow(edges, plt.cm.gray)
ax1.set_title('Canny edges')
ax1.set_axis_off()

#用plot绘制出所有的直线
ax2.imshow(edges * 0)
for line in lines:
    p0, p1 = line
    ax2.plot((p0[0], p1[0]), (p0[1], p1[1]))
row2, col2 = image.shape
ax2.axis((0, col2, row2, 0))
ax2.set_title('Probabilistic Hough')
ax2.set_axis_off()
plt.show()
```

![img](https://upload-images.jianshu.io/upload_images/1496926-ce29e3e6d64e08df.png)

------

在极坐标中，圆的表示方式为：

```python
x=x0+rcosθ
y=y0+rsinθ
```

圆心为(x0,y0),r为半径，θ为旋转度数，值范围为0-359。

如果给定圆心点和半径，则其它点是否在圆上，我们就能检测出来了。在图像中，我们将每个非0像素点作为圆心点，以一定的半径进行检测，如果有一个点在圆上，我们就对这个圆心累加一次。如果检测到一个圆，那么这个圆心点就累加到最大，成为峰值。因此，在检测结果中，一个峰值点，就对应一个圆心点。

霍夫圆检测的函数：

```css
skimage.transform.hough_circle(image, radius)
```

radius是一个数组，表示半径的集合，如[3，4，5，6]

返回一个3维的数组（radius index, M, N), 第一维表示半径的索引，后面两维表示图像的尺寸。

例1：绘制两个圆形，用霍夫圆变换将它们检测出来。

```python
import numpy as np
import matplotlib.pyplot as plt
from skimage import draw,transform,feature

img = np.zeros((250, 250,3), dtype=np.uint8)
rr, cc = draw.circle_perimeter(60, 60, 50)  #以半径50画一个圆
rr1, cc1 = draw.circle_perimeter(150, 150, 60) #以半径60画一个圆
img[cc, rr,:] =255
img[cc1, rr1,:] =255

fig, (ax0,ax1) = plt.subplots(1,2, figsize=(8, 5))

ax0.imshow(img)  #显示原图
ax0.set_title('origin image')

hough_radii = np.arange(50, 80, 5)  #半径范围
hough_res =transform.hough_circle(img[:,:,0], hough_radii)  #圆变换 

centers = []  #保存所有圆心点坐标
accums = []   #累积值
radii = []    #半径

for radius, h in zip(hough_radii, hough_res):
    #每一个半径值，取出其中两个圆
    num_peaks = 2
    peaks =feature.peak_local_max(h, num_peaks=num_peaks) #取出峰值
    centers.extend(peaks)
    accums.extend(h[peaks[:, 0], peaks[:, 1]])
    radii.extend([radius] * num_peaks)

#画出最接近的圆
image =np.copy(img)
for idx in np.argsort(accums)[::-1][:2]:
    center_x, center_y = centers[idx]
    radius = radii[idx]
    cx, cy =draw.circle_perimeter(center_y, center_x, radius)
    image[cy, cx] =(255,0,0)

ax1.imshow(image)
ax1.set_title('detected image')
```

结果图如下：原图中的圆用白色绘制，检测出的圆用红色绘制。

![img](https://upload-images.jianshu.io/upload_images/1496926-a03fca2209a433c8.png)

例2，检测出下图中存在的硬币。

![img](https://upload-images.jianshu.io/upload_images/1496926-52b16b4f05557b9c.png)

```python
import numpy as np
import matplotlib.pyplot as plt
from skimage import data, color,draw,transform,feature,util

image = util.img_as_ubyte(data.coins()[0:95, 70:370]) #裁剪原图片
edges =feature.canny(image, sigma=3, low_threshold=10, 
                     high_threshold=50) #检测canny边缘

fig, (ax0,ax1) = plt.subplots(1,2, figsize=(8, 5))

ax0.imshow(edges, cmap=plt.cm.gray)  #显示canny边缘
ax0.set_title('original iamge')

hough_radii = np.arange(15, 30, 2)  #半径范围
hough_res =transform.hough_circle(edges, hough_radii)  #圆变换 

centers = []  #保存中心点坐标
accums = []   #累积值
radii = []    #半径

for radius, h in zip(hough_radii, hough_res):
    #每一个半径值，取出其中两个圆
    num_peaks = 2
    peaks =feature.peak_local_max(h, num_peaks=num_peaks) #取出峰值
    centers.extend(peaks)
    accums.extend(h[peaks[:, 0], peaks[:, 1]])
    radii.extend([radius] * num_peaks)

#画出最接近的5个圆
image = color.gray2rgb(image)
for idx in np.argsort(accums)[::-1][:5]:
    center_x, center_y = centers[idx]
    radius = radii[idx]
    cx, cy =draw.circle_perimeter(center_y, center_x, radius)
    image[cy, cx] = (255,0,0)

ax1.imshow(imge)
ax1.set_title('detected image')
```

![img](https://upload-images.jianshu.io/upload_images/1496926-5a0f8393aeb16f54.png)

椭圆变换是类似的，使用函数为：

```python
skimage.transform.hough_ellipse(img,accuracy, threshold,
                                min_size, max_size)
```

输入参数：

> img: 待检测图像。
>
> accuracy: 使用在累加器上的短轴二进制尺寸，是一个double型的值，默认为1
>
> thresh: 累加器阈值，默认为4
>
> min_size: 长轴最小长度，默认为4
>
> max_size: 短轴最大长度，默认为None,表示图片最短边的一半。

返回一个 [(accumulator, y0, x0, a, b, orientation)] 数组，accumulator表示累加器，（y0,x0)表示椭圆中心点，（a,b)分别表示长短轴，orientation表示椭圆方向

例：检测出咖啡图片中的椭圆杯口

```python
import matplotlib.pyplot as plt
from skimage import data,draw,color,transform,feature

#加载图片，转换成灰度图并检测边缘
image_rgb = data.coffee()[0:220, 160:420] #裁剪原图像，不然速度非常慢
image_gray = color.rgb2gray(image_rgb)
edges = feature.canny(image_gray, sigma=2.0, low_threshold=0.55, 
                      high_threshold=0.8)

#执行椭圆变换
result =transform.hough_ellipse(edges, accuracy=20, threshold=250,
                                min_size=100, max_size=120)
result.sort(order='accumulator') #根据累加器排序

#估计椭圆参数
best = list(result[-1])  #排完序后取最后一个
yc, xc, a, b = [int(round(x)) for x in best[1:5]]
orientation = best[5]

#在原图上画出椭圆
cy, cx =draw.ellipse_perimeter(yc, xc, a, b, orientation)
image_rgb[cy, cx] = (0, 0, 255) #在原图中用蓝色表示检测出的椭圆

#分别用白色表示canny边缘，用红色表示检测出的椭圆，进行对比
edges = color.gray2rgb(edges)
edges[cy, cx] = (250, 0, 0) 

fig2, (ax1, ax2) = plt.subplots(ncols=2, nrows=1, figsize=(8, 4))

ax1.set_title('Original picture')
ax1.imshow(image_rgb)

ax2.set_title('Edge (white) and result (red)')
ax2.imshow(edges)

plt.show()
```

![img](https://upload-images.jianshu.io/upload_images/1496926-916142ca06985d79.png)

霍夫椭圆变换速度非常慢，应避免图像太大。

在图像简单滤波中，我们已经讲解了很多算子用来检测边缘，其中用得最多的canny算子边缘检测。

本篇我们讲解一些其它方法来检测轮廓。

#### 5.7.2 查找轮廓（find_contours)

measure模块中的find_contours()函数，可用来检测二值图像的边缘轮廓。

函数原型为：

```python
skimage.measure.find_contours(array, level)
```

> array: 一个二值数组图像
>
> level: 在图像中查找轮廓的级别值

返回轮廓列表集合，可用for循环取出每一条轮廓。

例1：

```python
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure,draw 

#生成二值测试图像
img=np.zeros([100,100])
img[20:40,60:80]=1  #矩形
rr,cc = draw.circle(60,60,10)  #小圆
rr1,cc1 = draw.circle(20,30,15) #大圆
img[rr,cc]=1
img[rr1,cc1]=1

#检测所有图形的轮廓
contours = measure.find_contours(img, 0.5)

#绘制轮廓
fig, (ax0,ax1) = plt.subplots(1,2,figsize=(8,8))
ax0.imshow(img,plt.cm.gray)
ax1.imshow(img,plt.cm.gray)
for n, contour in enumerate(contours):
    ax1.plot(contour[:, 1], contour[:, 0], linewidth=2)
ax1.axis('image')
ax1.set_xticks([])
ax1.set_yticks([])
plt.show()
```

结果如下：不同的轮廓用不同的颜色显示

![img](https://upload-images.jianshu.io/upload_images/1496926-9784c27a13b21f94.png)

 

例2：

```python
import matplotlib.pyplot as plt
from skimage import measure,data,color

#生成二值测试图像
img=color.rgb2gray(data.horse())

#检测所有图形的轮廓
contours = measure.find_contours(img, 0.5)

#绘制轮廓
fig, axes = plt.subplots(1,2,figsize=(8,8))
ax0, ax1= axes.ravel()
ax0.imshow(img,plt.cm.gray)
ax0.set_title('original image')

rows,cols=img.shape
ax1.axis([0,rows,cols,0])
for n, contour in enumerate(contours):
    ax1.plot(contour[:, 1], contour[:, 0], linewidth=2)
ax1.axis('image')
ax1.set_title('contours')
plt.show()
```

 

![img](https://upload-images.jianshu.io/upload_images/1496926-ba1580015b4390be.png)

#### 5.7.3 逼近多边形曲线

> 逼近多边形曲线有两个函数：subdivide_polygon（)和 approximate_polygon（）

subdivide_polygon（)采用B样条（B-Splines)来细分多边形的曲线，该曲线通常在凸包线的内部。

函数格式为：

```php
skimage.measure.subdivide_polygon(coords, degree=2, preserve_ends=False)
```

> coords: 坐标点序列。
>
> degree: B样条的度数，默认为2
>
> preserve_ends: 如果曲线为非闭合曲线，是否保存开始和结束点坐标，默认为false

返回细分为的坐标点序列。



approximate_polygon（）是基于Douglas-Peucker算法的一种近似曲线模拟。它根据指定的容忍值来近似一条多边形曲线链，该曲线也在凸包线的内部。

函数格式为:

```python
skimage.measure.approximate_polygon(coords, tolerance)
```

> coords: 坐标点序列
>
> tolerance: 容忍值

返回近似的多边形曲线坐标序列。
例：

```csharp
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure,data,color

#生成二值测试图像
hand = np.array([[1.64516129, 1.16145833],
                 [1.64516129, 1.59375],
                 [1.35080645, 1.921875],
                 [1.375, 2.18229167],
                 [1.68548387, 1.9375],
                 [1.60887097, 2.55208333],
                 [1.68548387, 2.69791667],
                 [1.76209677, 2.56770833],
                 [1.83064516, 1.97395833],
                 [1.89516129, 2.75],
                 [1.9516129, 2.84895833],
                 [2.01209677, 2.76041667],
                 [1.99193548, 1.99479167],
                 [2.11290323, 2.63020833],
                 [2.2016129, 2.734375],
                 [2.25403226, 2.60416667],
                 [2.14919355, 1.953125],
                 [2.30645161, 2.36979167],
                 [2.39112903, 2.36979167],
                 [2.41532258, 2.1875],
                 [2.1733871, 1.703125],
                 [2.07782258, 1.16666667]])

#检测所有图形的轮廓
new_hand = hand.copy()
for _ in range(5):
    new_hand = measure.subdivide_polygon(new_hand, degree=2)

# approximate subdivided polygon with Douglas-Peucker algorithm
appr_hand =measure.approximate_polygon(new_hand, tolerance=0.02)

print("Number of coordinates:", len(hand), len(new_hand), 
      len(appr_hand))

fig, axes= plt.subplots(2,2, figsize=(9, 8))
ax0,ax1,ax2,ax3=axes.ravel()

ax0.plot(hand[:, 0], hand[:, 1],'r')
ax0.set_title('original hand')
ax1.plot(new_hand[:, 0], new_hand[:, 1],'g')
ax1.set_title('subdivide_polygon')
ax2.plot(appr_hand[:, 0], appr_hand[:, 1],'b')
ax2.set_title('approximate_polygon')

ax3.plot(hand[:, 0], hand[:, 1],'r')
ax3.plot(new_hand[:, 0], new_hand[:, 1],'g')
ax3.plot(appr_hand[:, 0], appr_hand[:, 1],'b')
ax3.set_title('all')
```

 

![img](https://upload-images.jianshu.io/upload_images/1496926-bf6a8ee2716e2ddc.png)

------

### 5.8 高级形态学处理

形态学处理，除了最基本的膨胀、腐蚀、开/闭运算、黑/白帽处理外，还有一些更高级的运用，如凸包，连通区域标记，删除小块区域等。

#### 5.8.1 凸包

凸包是指一个凸多边形，这个凸多边形将图片中所有的白色像素点都包含在内。

函数为：

```python
skimage.morphology.convex_hull_image(image)
```

输入为二值图像，输出一个逻辑二值图像。在凸包内的点为True, 否则为False
例：

```python
import matplotlib.pyplot as plt
from skimage import data,color,morphology

#生成二值测试图像
img=color.rgb2gray(data.horse())
img=(img<0.5)*1

chull = morphology.convex_hull_image(img)

#绘制轮廓
fig, axes = plt.subplots(1,2,figsize=(8,8))
ax0, ax1= axes.ravel()
ax0.imshow(img,plt.cm.gray)
ax0.set_title('original image')

ax1.imshow(chull,plt.cm.gray)
ax1.set_title('convex_hull image') 
```

![img](https://upload-images.jianshu.io/upload_images/1496926-b5d2203ef30ff8c0.png)

convex_hull_image()是将图片中的所有目标看作一个整体，因此计算出来只有一个最小凸多边形。如果图中有多个目标物体，每一个物体需要计算一个最小凸多边形，则需要使用convex_hull_object（）函数。

函数格式：

```python
skimage.morphology.convex_hull_object(image, neighbors=8)
```

输入参数image是一个二值图像，neighbors表示是采用4连通还是8连通，默认为8连通。
例：

```python
import matplotlib.pyplot as plt
from skimage import data,color,morphology,feature

#生成二值测试图像
img=color.rgb2gray(data.coins())
#检测canny边缘,得到二值图片
edgs=feature.canny(img, sigma=3, low_threshold=10, high_threshold=50) 

chull = morphology.convex_hull_object(edgs)

#绘制轮廓
fig, axes = plt.subplots(1,2,figsize=(8,8))
ax0, ax1= axes.ravel()
ax0.imshow(edgs,plt.cm.gray)
ax0.set_title('many objects')
ax1.imshow(chull,plt.cm.gray)
ax1.set_title('convex_hull image')
plt.show()
```

![img](https://upload-images.jianshu.io/upload_images/1496926-e1e56f713b57a5ea.png)

 

#### 5.8.2 连通区域标记

在二值图像中，如果两个像素点相邻且值相同（同为0或同为1），那么就认为这两个像素点在一个相互连通的区域内。而同一个连通区域的所有像素点，都用同一个数值来进行标记，这个过程就叫连通区域标记。在判断两个像素是否相邻时，我们通常采用4连通或8连通判断。在图像中，最小的单位是像素，每个像素周围有8个邻接像素，常见的邻接关系有2种：4邻接与8邻接。4邻接一共4个点，即上下左右，如下左图所示。8邻接的点一共有8个，包括了对角线位置的点，如下右图所示。

![img](https://upload-images.jianshu.io/upload_images/1496926-884cf5a127430dcd.png)

在skimage包中，我们采用measure子模块下的label（）函数来实现连通区域标记。
函数格式：

```python
skimage.measure.label(image,connectivity=None)
```

参数中的image表示需要处理的二值图像，connectivity表示连接的模式，1代表4邻接，2代表8邻接。

输出一个标记数组（labels), 从0开始标记。

```python
import numpy as np
import scipy.ndimage as ndi
from skimage import measure,color
import matplotlib.pyplot as plt

#编写一个函数来生成原始二值图像
def microstructure(l=256):
    n = 5
    x, y = np.ogrid[0:l, 0:l]  #生成网络
    mask = np.zeros((l, l))
    generator = np.random.RandomState(1)  #随机数种子
    points = l * generator.rand(2, n**2)
    mask[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
    mask = ndi.gaussian_filter(mask, sigma=l/(4.*n)) #高斯滤波
    return mask > mask.mean()

data = microstructure(l=128)*1 #生成测试图片

labels=measure.label(data,connectivity=2)  #8连通区域标记
dst=color.label2rgb(labels)  #根据不同的标记显示不同的颜色
print('regions number:',labels.max()+1)  #显示连通区域块数(从0开始标记)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.imshow(data, plt.cm.gray, interpolation='nearest')
ax1.axis('off')
ax2.imshow(dst,interpolation='nearest')
ax2.axis('off')

fig.tight_layout()
plt.show()
```

在代码中，有些地方乘以1，则可以将bool数组快速地转换为int数组。

结果如图：有10个连通的区域，标记为0-9

![img](https://upload-images.jianshu.io/upload_images/1496926-df5787211a5597ec.png)

如果想分别对每一个连通区域进行操作，比如计算面积、外接矩形、凸包面积等，则需要调用measure子模块的regionprops（）函数。该函数格式为：

```python
skimage.measure.regionprops(label_image)
```

返回所有连通区块的属性列表，常用的属性列表如下表：

```cpp
属性名称    类型  描述
area    int     区域内像素点总数
bbox    tuple   边界外接框(min_row, min_col, max_row, max_col)
centroid    array　　     质心坐标
convex_area     int     凸包内像素点总数
convex_image    ndarray     和边界外接框同大小的凸包　　
coords  ndarray     区域内像素点坐标
Eccentricity    float   离心率
equivalent_diameter     float   和区域面积相同的圆的直径
euler_number    int　　   区域欧拉数
extent      float   区域面积和边界外接框面积的比率
filled_area     int     区域和外接框之间填充的像素点总数
perimeter   float   区域周长
label   int     区域标记
```

#### 5.8.3 删除小块区域

有些时候，我们只需要一些大块区域，那些零散的、小块的区域，我们就需要删除掉，则可以使用morphology子模块的remove_small_objects（)函数。

函数格式：

```python
skimage.morphology.remove_small_objects(ar, min_size=64, 
                                        connectivity=1, in_place=False)
```

参数：

> ar: 待操作的bool型数组。
>
> min_size: 最小连通区域尺寸，小于该尺寸的都将被删除。默认为64.
>
> connectivity: 邻接模式，1表示4邻接，2表示8邻接
>
> in_place: bool型值，如果为True,表示直接在输入图像中删除小块区域，否则进行复制后再删除。默认为False.

返回删除了小块区域的二值图像。

```python
import numpy as np
import scipy.ndimage as ndi
from skimage import morphology
import matplotlib.pyplot as plt

#编写一个函数来生成原始二值图像
def microstructure(l=256):
    n = 5
    x, y = np.ogrid[0:l, 0:l]  #生成网络
    mask = np.zeros((l, l))
    generator = np.random.RandomState(1)  #随机数种子
    points = l * generator.rand(2, n**2)
    mask[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
    mask = ndi.gaussian_filter(mask, sigma=l/(4.*n)) #高斯滤波
    return mask > mask.mean()

data = microstructure(l=128) #生成测试图片

dst=morphology.remove_small_objects(data,min_size=300,connectivity=1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.imshow(data, plt.cm.gray, interpolation='nearest')
ax2.imshow(dst,plt.cm.gray,interpolation='nearest')

fig.tight_layout()
plt.show()
```

在此例中，我们将面积小于300的小块区域删除（由1变为0），结果如下图： ![img](https://upload-images.jianshu.io/upload_images/1496926-5aea6767aa486d9e.png)

Keep the labels with 2 largest areas.

```python
        label_image =measure.label(newpr) 
        areas = [r.area for r in regionprops(label_image)]
        areas.sort()
        if len(areas) > 2:
            for region in regionprops(label_image):
                if region.area < areas[-2]:
                    for coordinates in region.coords:
                        label_image[coordinates[0], coordinates[1]] = 0
        binary = label_image > 0
        label_image = morphology.remove_small_holes(binary, areas[-2])
    areas = [r.area for r in regionprops(label_image)]
    areas.sort()
    if len(areas) > 2:
        for region in regionprops(label_image):
            if region.area < areas[-2]:
                for coordinates in region.coords:
                       label_image[coordinates[0], coordinates[1]] = 0
    binary = label_image > 0
    if plot == True:
        plots[3].axis('off')
plots[3].imshow(binary, cmap=plt.cm.bone)
```

#### 5.8.4 综合示例

阈值分割+闭运算+连通区域标记+删除小区块+分色显示

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from skimage import data,filters,segmentation,measure,morphology,color

#加载并裁剪硬币图片
image = data.coins()[50:-50, 50:-50]

thresh =filters.threshold_otsu(image) #阈值分割
bw =morphology.closing(image > thresh, morphology.square(3)) #闭运算

cleared = bw.copy()  #复制
cleared=segmentation.clear_border(cleared)  #清除与边界相连的目标物
cleared = sm.opening(cleared,sm.disk(2)) 
cleared = sm.closing(cleared,sm.disk(2))

label_image =measure.label(cleared)  #连通区域标记
borders = np.logical_xor(bw, cleared) #异或
label_image[borders] = -1
image_label_overlay =color.label2rgb(label_image, image=image) 
#不同标记用不同颜色显示

fig,(ax0,ax1)= plt.subplots(1,2, figsize=(8, 6))
ax0.imshow(cleared,plt.cm.gray)
ax1.imshow(image_label_overlay)

for region in measure.regionprops(label_image): 
  #循环得到每一个连通区域属性集
    
    #忽略小区域
    if region.area < 100:
        continue

    #绘制外包矩形
    minr, minc, maxr, maxc = region.bbox
    rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                              fill=False, edgecolor='red', linewidth=2)
    ax1.add_patch(rect)
fig.tight_layout()
plt.show()
```

![img](https://upload-images.jianshu.io/upload_images/1496926-c07dd5e2a307b689.png)

------

### 5.9 骨架提取与分水岭算法

骨架提取与分水岭算法也属于形态学处理范畴，都放在morphology子模块内。

#### 5.9.1 骨架提取

骨架提取，也叫二值图像细化。这种算法能将一个连通区域细化成一个像素的宽度，用于特征提取和目标拓扑表示。

morphology子模块提供了两个函数用于骨架提取，分别是Skeletonize（）函数和medial_axis（）函数。我们先来看Skeletonize（）函数。

函数格式为:

```python
skimage.morphology.skeletonize(image)
```

输入和输出都是一幅二值图像。
例1：

```python
from skimage import morphology,draw
import numpy as np
import matplotlib.pyplot as plt

#创建一个二值图像用于测试
image = np.zeros((400, 400))

#生成目标对象1(白色U型)
image[10:-10, 10:100] = 1
image[-100:-10, 10:-10] = 1
image[10:-10, -100:-10] = 1

#生成目标对象2（X型）
rs, cs = draw.line(250, 150, 10, 280)
for i in range(10):
    image[rs + i, cs] = 1
rs, cs = draw.line(10, 150, 250, 280)
for i in range(20):
    image[rs + i, cs] = 1

#生成目标对象3（O型）
ir, ic = np.indices(image.shape)
circle1 = (ic - 135)**2 + (ir - 150)**2 < 30**2
circle2 = (ic - 135)**2 + (ir - 150)**2 < 20**2
image[circle1] = 1
image[circle2] = 0

#实施骨架算法
skeleton =morphology.skeletonize(image)

#显示结果
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

ax1.imshow(image, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('original', fontsize=20)

ax2.imshow(skeleton, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('skeleton', fontsize=20)

fig.tight_layout()
plt.show()
```

生成一幅测试图像，上面有三个目标对象，分别进行骨架提取，结果如下：

![img](https://upload-images.jianshu.io/upload_images/1496926-cb374e73a8a63fdc.png)

例2：利用系统自带的马图片进行骨架提取

```python
from skimage import morphology,data,color
import matplotlib.pyplot as plt

image=color.rgb2gray(data.horse())
image=1-image #反相
#实施骨架算法
skeleton =morphology.skeletonize(image)

#显示结果
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

ax1.imshow(image, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('original', fontsize=20)

ax2.imshow(skeleton, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('skeleton', fontsize=20)

fig.tight_layout()
plt.show()
```

![img](https://upload-images.jianshu.io/upload_images/1496926-bc4b45b3b744196a.png)

medial_axis就是中轴的意思，利用中轴变换方法计算前景（1值）目标对象的宽度，格式为：

```python
skimage.morphology.medial_axis(image, mask=None, return_distance=False)
```

> mask: 掩模。默认为None, 如果给定一个掩模，则在掩模内的像素值才执行骨架算法。
>
> return_distance: bool型值，默认为False. 如果为True, 则除了返回骨架，还将距离变换值也同时返回。这里的距离指的是中轴线上的所有点与背景点的距离。

```python
import numpy as np
import scipy.ndimage as ndi
from skimage import morphology
import matplotlib.pyplot as plt

#编写一个函数，生成测试图像
def microstructure(l=256):
    n = 5
    x, y = np.ogrid[0:l, 0:l]
    mask = np.zeros((l, l))
    generator = np.random.RandomState(1)
    points = l * generator.rand(2, n**2)
    mask[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
    mask = ndi.gaussian_filter(mask, sigma=l/(4.*n))
    return mask > mask.mean()

data = microstructure(l=64) #生成测试图像

#计算中轴和距离变换值
skel, distance =morphology.medial_axis(data, return_distance=True)

#中轴上的点到背景像素点的距离
dist_on_skel = distance * skel

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.imshow(data, cmap=plt.cm.gray, interpolation='nearest')
#用光谱色显示中轴
ax2.imshow(dist_on_skel, cmap=plt.cm.spectral, interpolation='nearest')
ax2.contour(data, [0.5], colors='w')  #显示轮廓线

fig.tight_layout()
plt.show()
```

![img](https://upload-images.jianshu.io/upload_images/1496926-d9c8a4a6a4c18193.png)

 

#### 5.9.2 分水岭算法

分水岭在地理学上就是指一个山脊，水通常会沿着山脊的两边流向不同的“汇水盆”。分水岭算法是一种用于图像分割的经典算法，是基于拓扑理论的数学形态学的分割方法。如果图像中的目标物体是连在一起的，则分割起来会更困难，分水岭算法经常用于处理这类问题，通常会取得比较好的效果。

分水岭算法可以和距离变换结合，寻找“汇水盆地”和“分水岭界限”，从而对图像进行分割。二值图像的距离变换就是每一个像素点到最近非零值像素点的距离，我们可以使用scipy包来计算距离变换。

在下面的例子中，需要将两个重叠的圆分开。我们先计算圆上的这些白色像素点到黑色背景像素点的距离变换，选出距离变换中的最大值作为初始标记点（如果是反色的话，则是取最小值），从这些标记点开始的两个汇水盆越集越大，最后相交于分山岭。从分山岭处断开，我们就得到了两个分离的圆。

例1：基于距离变换的分山岭图像分割

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage import morphology,feature

#创建两个带有重叠圆的图像
x, y = np.indices((80, 80))
x1, y1, x2, y2 = 28, 28, 44, 52
r1, r2 = 16, 20
mask_circle1 = (x - x1)**2 + (y - y1)**2 < r1**2
mask_circle2 = (x - x2)**2 + (y - y2)**2 < r2**2
image = np.logical_or(mask_circle1, mask_circle2)

#现在我们用分水岭算法分离两个圆
distance = ndi.distance_transform_edt(image) #距离变换
local_maxi =feature.peak_local_max(distance, indices=False, 
                                   footprint=np.ones((3, 3)),
                            labels=image)   #寻找峰值
markers = ndi.label(local_maxi)[0] #初始标记点
labels =morphology.watershed(-distance, markers, mask=image) 
#基于距离变换的分水岭算法

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))
axes = axes.ravel()
ax0, ax1, ax2, ax3 = axes

ax0.imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax0.set_title("Original")
ax1.imshow(-distance, cmap=plt.cm.jet, interpolation='nearest')
ax1.set_title("Distance")
ax2.imshow(markers, cmap=plt.cm.spectral, interpolation='nearest')
ax2.set_title("Markers")
ax3.imshow(labels, cmap=plt.cm.spectral, interpolation='nearest')
ax3.set_title("Segmented")

for ax in axes:
    ax.axis('off')

fig.tight_layout()
plt.show()
```

 

![img](https://upload-images.jianshu.io/upload_images/1496926-7d521b7511080d38.png)

分水岭算法也可以和梯度相结合，来实现图像分割。一般梯度图像在边缘处有较高的像素值，而在其它地方则有较低的像素值，理想情况 下，分山岭恰好在边缘。因此，我们可以根据梯度来寻找分山岭。

例2：基于梯度的分水岭图像分割

```python
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage import morphology,color,data,filter

image =color.rgb2gray(data.camera())
denoised = filter.rank.median(image, morphology.disk(2)) #过滤噪声

#将梯度值低于10的作为开始标记点
markers = filter.rank.gradient(denoised, morphology.disk(5)) <10
markers = ndi.label(markers)[0]

gradient = filter.rank.gradient(denoised, morphology.disk(2)) 
#计算梯度
labels =morphology.watershed(gradient, markers, mask=image) 
#基于梯度的分水岭算法

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(6, 6))
axes = axes.ravel()
ax0, ax1, ax2, ax3 = axes

ax0.imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax0.set_title("Original")
ax1.imshow(gradient, cmap=plt.cm.spectral, interpolation='nearest')
ax1.set_title("Gradient")
ax2.imshow(markers, cmap=plt.cm.spectral, interpolation='nearest')
ax2.set_title("Markers")
ax3.imshow(labels, cmap=plt.cm.spectral, interpolation='nearest')
ax3.set_title("Segmented")

for ax in axes:
    ax.axis('off')

fig.tight_layout()
plt.show() 
```

![img](https://upload-images.jianshu.io/upload_images/1496926-059885bb38b2b4aa.png)

### 5.10 给图像加入噪声

**函数格式：**

```python
skimage.util.random_noise(image, mode='gaussian', seed=None, clip=True,
                          **kwargs)
```

该函数可以方便的为图像添加各种类型的噪声如高斯白噪声、椒盐噪声等。 

**参数介绍**

> **image**
>
> 为输入图像数据，类型应为ndarray，输入后将转换为浮点数。
>
> **mode**
>
> 选择添加噪声的类别。字符串str类型。应为以下几种之一：
>
> > 'gaussian'高斯加性噪声。
> >
> > 'localvar'  高斯加性噪声，每点具有特定的局部方差。
> >
> > 'poisson'  泊松分布的噪声。
> >
> > 'salt' 盐噪声，随机用1替换像素。属于高灰度噪声。
> >
> > 'pepper' 胡椒噪声，随机用0或-1替换像素，属于低灰度噪声。
> >
> > 's&p' 椒盐噪声，两种噪声同时出现，呈现出黑白杂点。
> >
> > 'speckle' 使用out = image + n *图像的乘法噪声，其中n是具有指定均值和方差的均匀噪声。
> 
>**seed** 
> 
>int 将在生成噪声之前设置随机种子，以进行有效的伪随机比较。
> 
>**clip**	
> 
>bool 若为True(default)则在加入'speckle', 'poisson', 或 'gaussian'这三种噪声后进行剪切以保证图像数据点都在[0,1]或[-1.1]之间。若为False，则数据可能超出这个范围。
> 
>**mean**
> 
>float 随机分布的均值，用于'gaussian'和'speckle'。 默认为0。 
> 
>**var**
> 
>float 随机分布的方差，（标准差^2）用于'gaussian'和'speckle'。 默认为0.01。 
> 
>**local_vars**
> 
>ndarray 图像每个像素点处的局部方差，正浮点数矩阵，和图像同型，用于'localvar'. 
> 
>**amount**
> 
>float 椒盐噪声像素点替换的比例，在[0,1]之间。用于'salt', 'pepper',和 'salt & pepper'. 默认 : 0.05 
> 
>**salt_vs_pepper** 
> 
>float 盐噪声和胡椒噪声的比例，在[0,1]之间。数字越大代表用1替换越多（more salt）. 默认 : 0.5 输出 
> 
>**out**
> 
>ndarray 输出为浮点图像数据，在[0,1]或[-1,1]之间。Skimage读取图像后格式为(height, width, channel)。注意RGB图像数据若为浮点数则范围为[0,1],若为整型则范围为[0,255]。



## 6. Demo

### 6.1 Face Detect

**Face detection using a cascade classifier**

This computer vision example shows how to detect faces on an image using object detection framework based on machine learning.

First, you will need an xml file, from which the trained data can be read. The framework works with files, trained using Multi-block Local Binary Patterns Features (See [MB-LBP](https://scikit-image.org/docs/stable/auto_examples/applications/plot_multiblock_local_binary_pattern.html)) and Gentle Adaboost with attentional cascade. So, the detection framework will also work with [xml files from OpenCV](https://github.com/opencv/opencv/tree/master/data/lbpcascades). There you can find files that were trained to detect cat faces, profile faces and other things. But if you want to detect frontal faces, the respective file is already included in scikit-image.

Next you will have to specify the parameters for the `detect_multi_scale` function. Here you can find the meaning of each of them.

First one is `scale_ratio`. To find all faces, the algorithm does the search on multiple scales. This is done by changing the size of searching window. The smallest window size is the size of window that was used in training. This size is specified in the xml file with trained parameters. The `scale_ratio` parameter specifies by which ratio the search window is increased on each step. If you increase this parameter, the search time decreases and the accuracy decreases. So, faces on some scales can be not detected.

`step_ratio` specifies the step of sliding window that is used to search for faces on each scale of the image. If this parameter is equal to one, then all the possible locations are searched. If the parameter is greater than one, for example, two, the window will be moved by two pixels and not all of the possible locations will be searched for faces. By increasing this parameter we can reduce the working time of the algorithm, but the accuracy will also be decreased.

`min_size` is the minimum size of search window during the scale search. `max_size` specifies the maximum size of the window. If you know the size of faces on the images that you want to search, you should specify these parameters as precisely as possible, because you can avoid doing expensive computations and possibly decrease the amount of false detections. You can save a lot of time by increasing the `min_size` parameter, because the majority of time is spent on searching on the smallest scales.

`min_neighbour_number` and `intersection_score_threshold` parameters are made to cluster the excessive detections of the same face and to filter out false detections. True faces usually has a lot of dectections around them and false ones usually have single detection. First algorithm searches for clusters: two rectangle detections are placed in the same cluster if the intersection score between them is larger then `intersection_score_threshold`. The intersection score is computed using the equation (intersection area) / (small rectangle ratio). The described intersection criteria was chosen over intersection over union to avoid a corner case when small rectangle inside of a big one have small intersection score. Then each cluster is thresholded using `min_neighbour_number` parameter which leaves the clusters that have a same or bigger number of detections in them.

You should also take into account that false detections are inevitable and if you want to have a really precise detector, you will have to train it yourself using [OpenCV train cascade utility](https://docs.opencv.org/2.4/doc/user_guide/ug_traincascade.html).

**Code：**

```python
from skimage import data
from skimage.feature import Cascade

import matplotlib.pyplot as plt
from matplotlib import patches

# Load the trained file from the module root.
trained_file = data.lbp_frontal_face_cascade_filename()

# Initialize the detector cascade.
detector = Cascade(trained_file)

img = data.astronaut()

detected = detector.detect_multi_scale(img=img,
                                       scale_factor=1.2,
                                       step_ratio=1,
                                       min_size=(60, 60),
                                       max_size=(123, 123))

plt.imshow(img)
img_desc = plt.gca()
plt.set_cmap('gray')

for patch in detected:

    img_desc.add_patch(
        patches.Rectangle(
            (patch['c'], patch['r']),
            patch['width'],
            patch['height'],
            fill=False,
            color='r',
            linewidth=2
        )
    )

plt.show()
```

**Result：**

![plot face detection](https://scikit-image.org/docs/stable/_images/sphx_glr_plot_face_detection_001.png)



### 6.2 Colors separation

Color deconvolution consists of the separation of features by their colors.

In this example we separate the immunohistochemical (IHC) staining from the hematoxylin counterstaining. The separation is achieved with the method described in [1](https://scikit-image.org/docs/stable/auto_examples/color_exposure/plot_ihc_color_separation.html#id2), known as “color deconvolution”.

The IHC staining expression of the FHL2 protein is here revealed with Diaminobenzidine (DAB) which gives a brown color.

A. C. Ruifrok and D. A. Johnston, “Quantification of histochemical staining by color deconvolution.,” Analytical and quantitative cytology and histology / the International Academy of Cytology [and] American Society of Cytology, vol. 23, no. 4, pp. 291-9, Aug. 2001.

```PYTHON
import matplotlib.pyplot as plt

from skimage import data
from skimage.color import rgb2hed
from matplotlib.colors import LinearSegmentedColormap

# Create an artificial color close to the original one
cmap_hema = LinearSegmentedColormap.from_list('mycmap', ['white', 'navy'])
cmap_dab = LinearSegmentedColormap.from_list('mycmap', ['white',
                                             'saddlebrown'])
cmap_eosin = LinearSegmentedColormap.from_list('mycmap', ['darkviolet',
                                               'white'])

ihc_rgb = data.immunohistochemistry()
ihc_hed = rgb2hed(ihc_rgb)

fig, axes = plt.subplots(2, 2, figsize=(7, 6), sharex=True, sharey=True)
ax = axes.ravel()

ax[0].imshow(ihc_rgb)
ax[0].set_title("Original image")

ax[1].imshow(ihc_hed[:, :, 0], cmap=cmap_hema)
ax[1].set_title("Hematoxylin")

ax[2].imshow(ihc_hed[:, :, 1], cmap=cmap_eosin)
ax[2].set_title("Eosin")

ax[3].imshow(ihc_hed[:, :, 2], cmap=cmap_dab)
ax[3].set_title("DAB")

for a in ax.ravel():
    a.axis('off')

fig.tight_layout()
```

![Original image, Hematoxylin, Eosin, DAB](https://scikit-image.org/docs/stable/_images/sphx_glr_plot_ihc_color_separation_001.png)

Now we can easily manipulate the hematoxylin and DAB “channels”:

```
import numpy as np
from skimage.exposure import rescale_intensity

# Rescale hematoxylin and DAB signals and give them a fluorescence look
h = rescale_intensity(ihc_hed[:, :, 0], out_range=(0, 1))
d = rescale_intensity(ihc_hed[:, :, 2], out_range=(0, 1))
zdh = np.dstack((np.zeros_like(h), d, h))

fig = plt.figure()
axis = plt.subplot(1, 1, 1, sharex=ax[0], sharey=ax[0])
axis.imshow(zdh)
axis.set_title("Stain separated image (rescaled)")
axis.axis('off')
plt.show()
```

![Stain separated image (rescaled)](https://scikit-image.org/docs/stable/_images/sphx_glr_plot_ihc_color_separation_002.png)

### 6.3 RGB adaptor

There are many filters that are designed to work with gray-scale images but not with color images. To simplify the process of creating functions that can adapt to RGB images, scikit-image provides the `adapt_rgb` decorator.

To actually use the `adapt_rgb` decorator, you have to decide how you want to adapt the RGB image for use with the gray-scale filter. There are two pre-defined handlers:

- `each_channel`

  Pass each of the RGB channels to the filter one-by-one, and stitch the results back into an RGB image.

- `hsv_value`

  Convert the RGB image to HSV and pass the value channel to the filter. The filtered result is inserted back into the HSV image and converted back to RGB.

Below, we demonstrate the use of `adapt_rgb` on a couple of gray-scale filters:

```PYTHON
from skimage.color.adapt_rgb import adapt_rgb, each_channel, hsv_value
from skimage import filters


@adapt_rgb(each_channel)
def sobel_each(image):
    return filters.sobel(image)


@adapt_rgb(hsv_value)
def sobel_hsv(image):
    return filters.sobel(image)
```

We can use these functions as we would normally use them, but now they work with both gray-scale and color images. Let’s plot the results with a color image:

```PYTHON
from skimage import data
from skimage.exposure import rescale_intensity
import matplotlib.pyplot as plt

image = data.astronaut()

fig, (ax_each, ax_hsv) = plt.subplots(ncols=2, figsize=(14, 7))

# We use 1 - sobel_each(image) but this won't work if image is not normalized
ax_each.imshow(rescale_intensity(1 - sobel_each(image)))
ax_each.set_xticks([]), ax_each.set_yticks([])
ax_each.set_title("Sobel filter computed\n on individual RGB channels")

# We use 1 - sobel_hsv(image) but this won't work if image is not normalized
ax_hsv.imshow(rescale_intensity(1 - sobel_hsv(image)))
ax_hsv.set_xticks([]), ax_hsv.set_yticks([])
ax_hsv.set_title("Sobel filter computed\n on (V)alue converted image (HSV)")
```

![Sobel filter computed  on individual RGB channels, Sobel filter computed  on (V)alue converted image (HSV)](https://scikit-image.org/docs/stable/_images/sphx_glr_plot_adapt_rgb_001.png)

Out:

```PYTHON
Text(0.5, 1.0, 'Sobel filter computed\n on (V)alue converted image (HSV)')
```

![Copy to clipboard](https://scikit-image.org/docs/stable/_static/copy-button.svg)

Notice that the result for the value-filtered image preserves the color of the original image, but channel filtered image combines in a more surprising way. In other common cases, smoothing for example, the channel filtered image will produce a better result than the value-filtered image.

You can also create your own handler functions for `adapt_rgb`. To do so, just create a function with the following signature:

```PYTHON
def handler(image_filter, image, *args, **kwargs):
    # Manipulate RGB image here...
    image = image_filter(image, *args, **kwargs)
    # Manipulate filtered image here...
    return image![Copy to clipboard](https://scikit-image.org/docs/stable/_static/copy-button.svg)
```

Note that `adapt_rgb` handlers are written for filters where the image is the first argument.

As a very simple example, we can just convert any RGB image to grayscale and then return the filtered result:

```PYTHON
from skimage.color import rgb2gray


def as_gray(image_filter, image, *args, **kwargs):
    gray_image = rgb2gray(image)
    return image_filter(gray_image, *args, **kwargs)
```

It’s important to create a signature that uses `*args` and `**kwargs` to pass arguments along to the filter so that the decorated function is allowed to have any number of positional and keyword arguments.

Finally, we can use this handler with `adapt_rgb` just as before:

```PYTHON
@adapt_rgb(as_gray)
def sobel_gray(image):
    return filters.sobel(image)

  
fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(7, 7))

# We use 1 - sobel_gray(image) but this won't work if image is not normalized
ax.imshow(rescale_intensity(1 - sobel_gray(image)), cmap=plt.cm.gray)
ax.set_xticks([]), ax.set_yticks([])
ax.set_title("Sobel filter computed\n on the converted grayscale image")

plt.show()
```

![Sobel filter computed  on the converted grayscale image](https://scikit-image.org/docs/stable/_images/sphx_glr_plot_adapt_rgb_002.png)

Note

A very simple check of the array shape is used for detecting RGB images, so `adapt_rgb` is not recommended for functions that support 3D volumes or color images in non-RGB spaces.



### 6.4 Random shape

Example of generating random shapes with particular properties.

![Grayscale shape, Colored shapes, #0, Colored shapes, #1, Colored shapes, #2, Colored shapes, #3, Overlapping shapes](https://scikit-image.org/docs/stable/_images/sphx_glr_plot_random_shapes_001.png)

Out:

```python
Image shape: (128, 128)
Labels: [('rectangle', ((117, 119), (47, 116)))]
```

```python
import matplotlib.pyplot as plt

from skimage.draw import random_shapes

# Let's start simple and generate a 128x128 image
# with a single grayscale rectangle.
result = random_shapes((128, 128), max_shapes=1, shape='rectangle',
                       multichannel=False, random_seed=0)

# We get back a tuple consisting of (1) the image with the generated shapes
# and (2) a list of label tuples with the kind of shape (e.g. circle,
# rectangle) and ((r0, r1), (c0, c1)) coordinates.
image, labels = result
print(f"Image shape: {image.shape}\nLabels: {labels}")

# We can visualize the images.
fig, axes = plt.subplots(nrows=2, ncols=3)
ax = axes.ravel()
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Grayscale shape')

# The generated images can be much more complex. For example, let's try many
# shapes of any color. If we want the colors to be particularly light, we can
# set the `intensity_range` to an upper subrange of (0,255).
image1, _ = random_shapes((128, 128), max_shapes=10,
                          intensity_range=((100, 255),))

# Moar :)
image2, _ = random_shapes((128, 128), max_shapes=10,
                          intensity_range=((200, 255),))
image3, _ = random_shapes((128, 128), max_shapes=10,
                          intensity_range=((50, 255),))
image4, _ = random_shapes((128, 128), max_shapes=10,
                          intensity_range=((0, 255),))

for i, image in enumerate([image1, image2, image3, image4], 1):
    ax[i].imshow(image)
    ax[i].set_title(f"Colored shapes, #{i-1}")

# These shapes are well suited to test segmentation algorithms. Often, we
# want shapes to overlap to test the algorithm. This is also possible:
image, _ = random_shapes((128, 128), min_shapes=5, max_shapes=10,
                         min_size=20, allow_overlap=True)
ax[5].imshow(image)
ax[5].set_title('Overlapping shapes')

for a in ax:
    a.set_xticklabels([])
    a.set_yticklabels([])

plt.show()
```



### 6.5 Denoising 

In this example, we denoise a noisy version of a picture using the total variation, bilateral, and wavelet denoising filters.

Total variation and bilateral algorithms typically produce “posterized” images with flat domains separated by sharp edges. It is possible to change the degree of posterization by controlling the tradeoff between denoising and faithfulness to the original image.

#### Total variation filter

The result of this filter is an image that has a minimal total variation norm, while being as close to the initial image as possible. The total variation is the L1 norm of the gradient of the image.

##### Bilateral filter

A bilateral filter is an edge-preserving and noise reducing filter. It averages pixels based on their spatial closeness and radiometric similarity.

##### Wavelet denoising filter

A wavelet denoising filter relies on the wavelet representation of the image. The noise is represented by small values in the wavelet domain which are set to 0.

In color images, wavelet denoising is typically done in the YCbCr color space as denoising in separate color channels may lead to more apparent noise.



Out:

```python
Estimated Gaussian noise standard deviation = 0.1504735072480644
Clipping input data to the valid range 
for imshow with RGB data ([0..1] for floats or [0..255] for integers).
```

**Code**

```python
import matplotlib.pyplot as plt

from skimage.restoration import (denoise_tv_chambolle, denoise_bilateral,
                                 denoise_wavelet, estimate_sigma)
from skimage import data, img_as_float
from skimage.util import random_noise


original = img_as_float(data.chelsea()[100:250, 50:300])

sigma = 0.155
noisy = random_noise(original, var=sigma**2)

fig, ax = plt.subplots(nrows=2, ncols=4, figsize=(8, 5),
                       sharex=True, sharey=True)

plt.gray()

# Estimate the average noise standard deviation across color channels.
sigma_est = estimate_sigma(noisy, multichannel=True, average_sigmas=True)
# Due to clipping in random_noise, the estimate will be a bit smaller than the
# specified sigma.
print(f"Estimated Gaussian noise standard deviation = {sigma_est}")

ax[0, 0].imshow(noisy)
ax[0, 0].axis('off')
ax[0, 0].set_title('Noisy')
ax[0, 1].imshow(denoise_tv_chambolle(noisy, weight=0.1, multichannel=True))
ax[0, 1].axis('off')
ax[0, 1].set_title('TV')
ax[0, 2].imshow(denoise_bilateral(noisy, sigma_color=0.05, sigma_spatial=15,
                multichannel=True))
ax[0, 2].axis('off')
ax[0, 2].set_title('Bilateral')
ax[0, 3].imshow(denoise_wavelet(noisy, multichannel=True, rescale_sigma=True))
ax[0, 3].axis('off')
ax[0, 3].set_title('Wavelet denoising')

ax[1, 1].imshow(denoise_tv_chambolle(noisy, weight=0.2, multichannel=True))
ax[1, 1].axis('off')
ax[1, 1].set_title('(more) TV')
ax[1, 2].imshow(denoise_bilateral(noisy, sigma_color=0.1, sigma_spatial=15,
                multichannel=True))
ax[1, 2].axis('off')
ax[1, 2].set_title('(more) Bilateral')
ax[1, 3].imshow(denoise_wavelet(noisy, multichannel=True, convert2ycbcr=True,
                                rescale_sigma=True))
ax[1, 3].axis('off')
ax[1, 3].set_title('Wavelet denoising\nin YCbCr colorspace')
ax[1, 0].imshow(original)
ax[1, 0].axis('off')
ax[1, 0].set_title('Original')

fig.tight_layout()

plt.show()
```

![](https://scikit-image.org/docs/stable/_images/sphx_glr_plot_denoise_001.png)