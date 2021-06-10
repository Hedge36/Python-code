# Pillow 中文教程

**翻译自[官方文档](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html)**

## Image类

Pillow中最重要的类就是Image，该类存在于同名的模块中。可以通过以下几种方式实例化：从文件中读取图片，处理其他图片得到，或者直接创建一个图片。

使用Image模块中的open函数打开一张图片：

```python
from PIL import Image
im = Image.open("lena.ppm")
```

如果打开成功，返回一个Image对象，可以通过对象属性检查文件内容

```python
from __future__ import print_function
print(im.format, im.size, im.mode)
PPM (512, 512) RGB
```

format属性定义了图像的格式，如果图像不是从文件打开的，那么该属性值为None；size属性是一个tuple，表示图像的宽和高（单位为像素）；mode属性为表示图像的模式，常用的模式为：L为灰度图，RGB为真彩色，CMYK为pre-press图像。

如果文件不能打开，则抛出IOError异常。

当有一个Image对象时，可以用Image类的各个方法进行处理和操作图像，例如显示图片：

```python
im.show()
```

> ps：标准版本的show()方法不是很有效率，因为它先将图像保存为一个临时文件，然后使用xv进行显示。如果没有安装xv，该函数甚至不能工作。但是该方法非常便于debug和test。（windows中应该调用默认图片查看器打开）

**多图像处理只需通过list操作即可**



## 读写图片

Pillow库支持相当多的图片格式。直接使用Image模块中的open()函数读取图片，而不必先处理图片的格式，Pillow库自动根据文件决定格式。

Image模块中的save()函数可以保存图片，除非你指定文件格式，那么文件名中的扩展名用来指定文件格式。

### 1. 图片读取

```python
PIL.Image.open(fp, mode='r')
```

Opens and identifies the given image file.

This is a lazy operation; this function identifies the file, but the file remains open and the actual image data is not read from the file until you try to process the data (or call the [`load()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.load) method). See [`new()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.new).

**Parameters:**  

> **fp** – A filename (string), pathlib.Path object or a file object. The file object must implement `read()`, `seek()`, and `tell()` methods, and be opened in binary mode.
>
> **mode** – The mode. If given, this argument must be “r”. 

 **Returns:**    

>  An `Image` object. 

**Raises:** 

> **IOError** – If the file cannot be found, or the image cannot be opened and identified. 

### 2.图片创建

```python
PIL.Image.new(mode, size, color=0)
```

Creates a new image with the given mode and size.

**Parameters:** 

> **mode** – The mode to use for the new image. See: [Modes](https://pillow.readthedocs.io/en/3.0.x/handbook/concepts.html#concept-modes).
>
> **size** – A 2-tuple, containing (width, height) in pixels.
>
> **color** – What color to use for the image. Default is black. If given, this should be a single integer or floating point value for single-band modes, and a tuple for multi-band modes (one value per band). When creating RGB images, you can also pythonuse color strings as supported by the ImageColor module. If the color is None, the image is not initialised. 

> **Returns:**    
>
> An `Image` object. 

**创建缩略图**

```python
from __future__ import print_function
import os, sys
from PIL import Image

size = (128, 128)

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size)
            im.save(outfile, "JPEG")
        except IOError:
            print("cannot create thumbnail for", infile)
```

必须指出的是除非必须，Pillow不会解码或raster数据。当你打开一个文件，Pillow通过文件头确定文件格式，大小，mode等数据，余下数据直到需要时才处理。

这意味着打开文件非常快，与文件大小和压缩格式无关。下面的程序用来快速确定图片属性：

**确定图片属性**

```python
from __future__ import print_function
import sys
from PIL import Image

for infile in sys.argv[1:]:
    try:
        with Image.open(infile) as im:
            print(infile, im.format, "%dx%d" % im.size, im.mode)
    except IOError:
        pass
```

## 图像基本操作

Image类包含还多操作图片区域的方法。如crop()方法可以从图片中提取一个子矩形

**从图片中复制子图像**

```python
box = im.copy() #直接复制图像
box = (100, 100, 400, 400)
region = im.crop(box)
```

区域由4-tuple决定，该tuple中信息为(left, upper, right, lower)。 Pillow左边系统的原点（0，0）为图片的左上角。坐标中的数字单位为像素点，所以上例中截取的图片大小为300*300像素^2。

**处理子图，粘贴回原图**

```python
region = region.transpose(Image.ROTATE_180)
im.paste(region, box)
```

将子图paste回原图时，子图的region必须和给定box的region吻合。该region不能超过原图。而原图和region的mode不需要匹配，Pillow会自动处理。

**Rolling an image**

```python
def roll(image, delta):
    "Roll an image sideways"

    image = image.copy() #复制图像
    xsize, ysize = image.size

    delta = delta % xsize
    if delta == 0: 
      return image
    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize-delta, ysize))
    image.paste(part1, (xsize-delta, 0, xsize, ysize))

    return image
```

**分离和合并通道**

```python
r, g, b = im.split()
im = Image.merge("RGB", (b, g, r))
```

对于单通道图片，split()返回图像本身。为了处理单通道图片，必须先将图片转成RGB。

**图片混合**

```python
PIL.Image.blend(im1, im2, alpha)
```

Creates a new image by interpolating between two input images, using a constant alpha.:`out = image1 * (1.0 - alpha) + image2 * alpha `

**Parameters:**

> **im1** – The first image.
>
> **im2** – The second image. Must have the same mode and size as the first image.**alpha** – The interpolation alpha factor. If alpha is 0.0, a copy of the first image is returned. If alpha is 1.0, a copy of the second image is returned. There are no restrictions on the alpha value. If necessary, the result is clipped to fit into the allowed output range.Returns:An `Image` object.

```python
PIL.Image.composite(image1, image2, mask)
```

Create composite image by blending images using a transparency mask.

**Parameters:**

> *image1* – The first image.
>
> *image2* – The second image. Must have the same mode and size as the first image.
>
> **mask** – A mask image. This image can have mode “1”, “L”, or “RGBA”, and must have the same size as the other two images.





## 几何变换

Image类有resize()、rotate()和transpose()、transform()方法进行几何变换。

**简单几何变换**

```python
out = im.resize((128, 128))
out = im.rotate(45) # 顺时针角度表示
```

**置换图像**

```python
out = im.transpose(Image.FLIP_LEFT_RIGHT)
out = im.transpose(Image.FLIP_TOP_BOTTOM)
out = im.transpose(Image.ROTATE_90)
out = im.transpose(Image.ROTATE_180)
out = im.transpose(Image.ROTATE_270)
```

transpose()和象的rotate()没有性能差别。

更通用的图像变换方法可以使用[transform()](http://pillow.readthedocs.org/en/latest/reference/Image.html#PIL.Image.Image.transform)

## 模式转换

[convert()](http://pillow.readthedocs.org/en/latest/reference/Image.html#PIL.Image.Image.convert)方法

**模式转换**

```python
im = Image.open('lena.ppm').convert('L')
```



## 像素点处理

### point

通过一个函数或者查询表对图像中的像素点进行处理（例如对比度操作）。

**像素点变换**

```python
# multiply each pixel by 1.2
out = im.point(lambda i: i * 1.2)
```

上述方法可以利用简单的表达式进行图像处理，通过组合point()和paste()还能选择性地处理图片的某一区域。

**处理单独通道**

```python
# split the image into individual bands
source = im.split()

R, G, B = 0, 1, 2

# select regions where red is less than 100
mask = source[R].point(lambda i: i < 100 and 255)

# process the green band
out = source[G].point(lambda i: i * 0.7)

# paste the processed band back, but only where red was < 100
source[G].paste(out, None, mask)

# build a new multiband image
im = Image.merge(im.mode, source)
```

注意到创建mask的语句：

```python
mask = source[R].point(lambda i: i < 100 and 255)
```

该句可以用下句表示

```python
imout = im.point(lambda i: expression and 255)
```

如果expression为假则返回expression的值为0（因为and语句已经可以得出结果了），否则返回255。（[mask](http://pillow.readthedocs.org/en/latest/reference/Image.html#PIL.Image.Image.point)参数用法：当为0时，保留当前值，255为使用paste进来的值，中间则用于transparency效果）

### eval

```python
PIL.Image.eval(image, **args)
```

Applies the function (which should take one argument) to each pixel in the given image. If the image has more than one band, the same function is applied to each band. Note that the function is evaluated once for each possible pixel value, so you cannot use random components or other generators.

**Parameters:** 

> *image* – The input image.
>
> **function** – A function object, taking one integer argument. 

**Returns:**    

> An `Image` object. 

## Filter

[ImageFilter](http://pillow.readthedocs.org/en/latest/reference/ImageFilter.html#module-PIL.ImageFilter)模块包含很多预定义的增强filters，通过[filter()](http://pillow.readthedocs.org/en/latest/reference/Image.html#PIL.Image.Image.filter)方法使用

图像增强也是图像预处理中的一个基本技术，Pillow中的图像增强函数主要在ImageEnhance模块下，通过该模块可以调节图像的白平衡（Color）、亮度（Brightness）、对比度（Contrast）和锐化（Sharpness）等。

**直接应用filters**

```python
from PIL import ImageFilter
out = im.filter(ImageFilter.DETAIL) 
```

**图像增强**

```python
from PIL import ImageEnhance
enh = ImageEnhance.Contrast(im)
enh.enhance(1.3).show("30% more contrast")
```

**动态图**

Pillow支持一些动态图片的格式如FLI/FLC，GIF和其他一些处于实验阶段的格式。TIFF文件同样可以包含数帧图像。

当读取动态图时，PIL自动读取动态图的第一帧，可以使用seek和tell方法读取不同帧。

```python
from PIL import Image

im = Image.open("animation.gif")
im.seek(1) # skip to the second frame

try:
    while 1:
        im.seek(im.tell()+1)
        # do something to im
except EOFError:
    pass # end of sequence
```

当读取到最后一帧时，Pillow抛出EOFError异常。

当前版本只允许seek到下一帧。为了倒回之前，必须重新打开文件。

或者可以使用下述迭代器类

**动态图迭代器类**

```python
class ImageSequence:
    def __init__(self, im):
        self.im = im
    def __getitem__(self, ix):
        try:
            if ix:
                self.im.seek(ix)
            return self.im
        except EOFError:
            raise IndexError # end of sequence

for frame in ImageSequence(im):
    # ...do something to frame...
```

**过滤**

filter方法可以将一些过滤器操作应用于原始图像，比如模糊，边缘增强、浮雕等。filter是过滤器函数，在PIL.ImageFilter函数中定义了大量内置的filter函数，比如BLUR(普通模糊)，GaussianBlur(高斯模糊) FIND_EDGES(查找边)等

```python
from PIL import Image
ImageFilter
im = Image.open('cat.jpg')

# 高斯模糊

im_gaussianblur = im.filter(ImageFilter.GaussianBlur)
im_gaussianblur.show()

# 普通模糊

im_blur = im.filter(ImageFilter.BLUR)
im_blur.show()

# 找到边缘

im_find_edge = im.filter(ImageFilter.FIND_EDGES)
im_find_edges.show()

# 浮雕

im_emboss = im.filter(ImageFilter.EMBOSS)
im_emboss.show()

# 轮廓

im_contour = im.filter(ImageFilter.CONTOUR)
im_contour.show()

# 锐化

im_sharpen = im.filter(ImageFilter.SHARPEN)
im_sharpen.show()

# 平滑

im_smooth = im.filter(ImageFilter.SMOOTH)
im_smooth.show()

# 细节

im_detail = im.filter(ImageFilter.DETAIL)
im_detail.show()
```

## 更多读取图片方法

之前说到Image模块的open()函数已经足够日常使用。该函数的参数也可以是一个文件对象。

**从string中读取**

```python
import StringIO

im = Image.open(StringIO.StringIO(buffer))
```

**从tar文件中读取**

```python
from PIL import TarIO

fp = TarIO.TarIO("Imaging.tar", "Imaging/test/lena.ppm")
im = Image.open(fp)
```



## 草稿模式

draft()方法允许在不读取文件内容的情况下尽可能（可能不会完全等于给定的参数）地将图片转成给定模式和大小，这在生成缩略图的时候非常有效（速度要求比质量高的场合）。

**draft模式**

```python
from __future__ import print_function
im = Image.open(file)
print("original =", im.mode, im.size)

im.draft("L", (100, 100))
print("draft =", im.mode, im.size)
```

```python
img = img.convert("L") #转化成灰度图像
#获取每个坐标的像素点的RGB值
r,g,b = img.getpixel((j,i))
#重设图片大小
img = img.resize(width,height)
#创建缩略图
img.thumbnail(size)
```

**实例**

其实应该很容易想到，如果要达到这种效果，应该能想得到就是获取图上每一点的RGB值，然后根据这三种值确定这一点采用什么字符，其实根据RGB来确定的交灰值，所以可以将图片转化成灰度图片，来直接获取每一点的灰度，或者通过灰度的转换公式来使得RGB三值转化成灰度

```python
#coding:utf-8
from PIL import Image
#要索引的字符列表
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
length = len(ascii_char)
img = Image.open('03.jpg')  #读取图像文件
(width,height) = img.size
img = img.resize((int(width*0.9),int(height*0.5))) #对图像进行一定缩小
print(img.size)
def convert(img):
	img = img.convert("L") # 转为灰度图像
   txt = ""
	for i in range(img.size[1]):
    for j in range(img.size[0]):
			gray = img.getpixel((j, i))  # 获取每个坐标像素点的灰度
		unit = 256.0 / length
		txt += ascii_char[int(gray / unit)] #获取对应坐标的字符值
  txt += '\n'
	return txt

def convert1(img):
	txt = ""
	for i in range(img.size[1]):
    for j in range(img.size[0]):
			r,g,b = img.getpixel((j, i))   #获取每个坐标像素点的rgb值
		gray = int(r * 0.299 + g * 0.587 + b * 0.114) #通过灰度转换公式获取灰度
		unit = (256.0+1)/length
		txt += ascii_char[int(gray / unit)] # 获取对应坐标的字符值
	txt += '\n'
	return txt

txt = convert(img)
f = open("03_convert.txt","w")
f.write(txt)   #存储到文件中
f.close()
```



## Postscript Printing

PSDraw模块为Postscript打印机提供简单的打印支持。

> 您可以通过这个模块打印文本、图形和图像。类PSDrawPSDraw.PSDraw(file) ⇒ PSDraw instance设置文件打印。如果文件被省略了，使用sys.stdout。

| 方法 | 说明 |
| ---- | ---- |
| begin_document() | 设置文档的打印。|
| end_document() | 结束打印。|
| line(from, to) | 在两点之间画一条线。坐标是指Postscript点坐标(每英寸72个点，(0，0)是页面的左下角)。|
| rectangle(box) | 绘制一个矩形。|
| text(position, text, alignment) | 在给定位置绘制文本。在调用此方法之前，必须使用setfont设置字体。|
| image(box, image, dpi=None) | 画一个以给定方框为中心的图像。|
| setfont(font, size) | 设置使用哪种字体。字体参数是一个Postscript字体名称，大小参数以点表示。|
| setink(ink) | 设置与后续操作一起使用的像素值。|
| setfill(onoff) | 设置随后的矩形操作是否应该填充矩形区域还是仅仅绘制轮廓。|

**给图片加上数字**

这个大家应该见过的，就是有些头像的左上角的那个小红圈加上白色的数字，其实方法和上面那个加文字的差不多 

```python
#coding:utf-8
from PIL import Image,ImageDraw,ImageFont
img = Image.open("03.jpg")
draw = ImageDraw.Draw(img)
myfont = ImageFont.truetype(u"时光体.ttf",50)
(width,height) = img.size
draw.ellipse((width-40,0,width,40),fill="red",outline="red") #在图上画一个圆
draw.text((width-30,-8),'1',font=myfont,fill='white')
img.save('03_modify.jpg')
```

**给图片插入汉字**

```python
from PIL import Image,ImageDraw,ImageFont

draw = ImageDraw.Draw(img)
myfont = ImageFont.truetype(r'C:\Users\Hedge\Documents\Fonts\msyh.ttf',
                            size=80)
#第一个参数是加入字体的坐标
#第二个参数是文字内容
#第三个参数是字体格式
#第四个参数是字体颜色
draw.text((640,800),u'萌萌哒',font=myfont,fill='pink')
```

**不知道在干嘛**

```python
from PIL import Image
from PIL import PSDraw

im = Image.open("lena.ppm")
title = "lena"
box = (1*72, 2*72, 7*72, 10*72) # in points

ps = PSDraw.PSDraw() # default is sys.stdout
ps.begin_document(title)

# draw the image (75 dpi)
ps.image(box, im, 75)
ps.rectangle(box)

# draw centered title
ps.setfont("HelveticaNarrow-Bold", 36)
w, h, b = ps.textsize(title)
ps.text((4*72-w/2, 1*72-h), title)

ps.end_document()

# img.save('1_1.jpg','jpeg')
```



## 实例

**生成4位随机验证码**

```python
#coding:utf-8
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
"""
创建四位数的验证码
"""
#产生随机验证码内容
def rndTxt():
	txt = []
	txt.append(random.randint(97,123))  #大写字母
	txt.append(random.randint(65,90))  #小写字母
	txt.append(random.randint(48,57))  #数字
	return chr(txt[random.randint(0,2)])

#随机颜色(背景)
def rndColor1():
	return (random.randint(64, 255), random.randint(64, 255), 
          random.randint(64, 255))

#随机颜色（字体）
def rndColor2():
	return (random.randint(32, 127), random.randint(32, 127), 
          random.randint(32, 127))

#240x60:
width = 60*4
height = 60
img = Image.new('RGB',(width,height),(255,255,255))
font = ImageFont.truetype(u'时光体.ttf',36)
draw = ImageDraw.Draw(img)
#填充每个像素
for x in range(width):
	for y in range(height):
		draw.point((x,y),fill=rndColor1())

#输出文字
for txt in range(4):
	draw.text((60*txt+10,10),rndTxt(),font=font,fill=rndColor2())
#模糊化处理
#img = img.filter(ImageFilter.BLUR)
img.save("code.jpg")
```

```python
im.show()
```





# Tutorial

Please get url:https://pillow.readthedocs.io/en/3.0.x/reference/Image.html

## Using the Image class

The most important class in the Python Imaging Library is the `Image` class, defined in the module with the same name. You can create instances of this class in several ways; either by loading images from files, processing other images, or creating images from scratch.

To load an image from a file, use the [`open()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.open) function in the [`Image`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#module-PIL.Image) module:

```python
from PIL import Image
im = Image.open("lena.ppm")
```

If successful, this function returns an `Image` object. You can now use instance attributes to examine the file contents:

```python
from __future__ import print_function
print(im.format, im.size, im.mode)
PPM (512, 512) RGB
```

The `format` attribute identifies the source of an image. If the image was not read from a file, it is set to None. The size attribute is a 2-tuple containing width and height (in pixels). The `mode` attribute defines the number and names of the bands in the image, and also the pixel type and depth. Common modes are “L” (luminance) for greyscale images, “RGB” for true color images, and “CMYK” for pre-press images.

If the file cannot be opened, an `IOError` exception is raised.

Once you have an instance of the `Image` class, you can use the methods defined by this class to process and manipulate the image. For example, let’s display the image we just loaded:

```python
im.show()
```

Note

The standard version of [`show()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.show) is not very efficient, since it saves the image to a temporary file and calls the **xv** utility to display the image. If you don’t have **xv** installed, it won’t even work. When it does work though, it is very handy for debugging and tests.

The following sections provide an overview of the different functions provided in this library.

## Reading and writing images

The Python Imaging Library supports a wide variety of image file formats. To read files from disk, use the [`open()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.open) function in the [`Image`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#module-PIL.Image) module. You don’t have to know the file format to open a file. The library automatically determines the format based on the contents of the file.

To save a file, use the [`save()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.save) method of the `Image` class. When saving files, the name becomes important. Unless you specify the format, the library uses the filename extension to discover which file storage format to use.

### Convert files to JPEG

```python
from __future__ import print_function
import os, sys
from PIL import Image

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("cannot convert", infile)
```

A second argument can be supplied to the [`save()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.save) method which explicitly specifies a file format. If you use a non-standard extension, you must always specify the format this way:

### Create JPEG thumbnails

```python
from __future__ import print_function
import os, sys
from PIL import Image

size = (128, 128)

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size)
            im.save(outfile, "JPEG")
        except IOError:
            print("cannot create thumbnail for", infile)
```

It is important to note that the library doesn’t decode or load the raster data unless it really has to. When you open a file, the file header is read to determine the file format and extract things like mode, size, and other properties required to decode the file, but the rest of the file is not processed until later.

This means that opening an image file is a fast operation, which is independent of the file size and compression type. Here’s a simple script to quickly identify a set of image files:

### Identify Image Files

```python
from __future__ import print_function
import sys
from PIL import Image

for infile in sys.argv[1:]:
    try:
        with Image.open(infile) as im:
            print(infile, im.format, "%dx%d" % im.size, im.mode)
    except IOError:
        pass
```

## Cutting, pasting, and merging images

The `Image` class contains methods allowing you to manipulate regions within an image. To extract a sub-rectangle from an image, use the [`crop()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.crop) method.

### Copying a subrectangle from an image

```python
box = (100, 100, 400, 400)
region = im.crop(box)
```

The region is defined by a 4-tuple, where coordinates are (left, upper, right, lower). The Python Imaging Library uses a coordinate system with (0, 0) in the upper left corner. Also note that coordinates refer to positions between the pixels, so the region in the above example is exactly 300x300 pixels.

The region could now be processed in a certain manner and pasted back.

### Processing a subrectangle, and pasting it back

```python
region = region.transpose(Image.ROTATE_180)
im.paste(region, box)
```

When pasting regions back, the size of the region must match the given region exactly. In addition, the region cannot extend outside the image. However, the modes of the original image and the region do not need to match. If they don’t, the region is automatically converted before being pasted (see the section on [Color transforms](https://pillow.readthedocs.io/en/3.0.x/handbook/tutorial.html#color-transforms) below for details).

Here’s an additional example:

### Rolling an image

```python
def roll(image, delta):
    "Roll an image sideways"

    xsize, ysize = image.size

    delta = delta % xsize
    if delta == 0: return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize-delta, ysize))
    image.paste(part1, (xsize-delta, 0, xsize, ysize))

    return image
```

For more advanced tricks, the paste method can also take a transparency mask as an optional argument. In this mask, the value 255 indicates that the pasted image is opaque in that position (that is, the pasted image should be used as is). The value 0 means that the pasted image is completely transparent. Values in-between indicate different levels of transparency. For example, pasting an RGBA image and also using it as the mask would paste the opaque portion of the image but not its transparent background.

The Python Imaging Library also allows you to work with the individual bands of an multi-band image, such as an RGB image. The split method creates a set of new images, each containing one band from the original multi-band image. The merge function takes a mode and a tuple of images, and combines them into a new image. The following sample swaps the three bands of an RGB image:

### Splitting and merging bands

```python
r, g, b = im.split()
im = Image.merge("RGB", (b, g, r))
```

Note that for a single-band image, [`split()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.split) returns the image itself. To work with individual color bands, you may want to convert the image to “RGB” first.

## Geometrical transforms

The [`PIL.Image.Image`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image) class contains methods to [`resize()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.resize) and [`rotate()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.rotate) an image. The former takes a tuple giving the new size, the latter the angle in degrees counter-clockwise.

### Simple geometry transforms

```python
out = im.resize((128, 128))
out = im.rotate(45) # degrees counter-clockwise
```

To rotate the image in 90 degree steps, you can either use the [`rotate()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.rotate) method or the [`transpose()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.transpose) method. The latter can also be used to flip an image around its horizontal or vertical axis.

### Transposing an image

```python
out = im.transpose(Image.FLIP_LEFT_RIGHT)
out = im.transpose(Image.FLIP_TOP_BOTTOM)
out = im.transpose(Image.ROTATE_90)
out = im.transpose(Image.ROTATE_180)
out = im.transpose(Image.ROTATE_270)
```

There’s no difference in performance or result between `transpose(ROTATE)` and corresponding [`rotate()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.rotate) operations.

A more general form of image transformations can be carried out via the [`transform()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.transform) method.



## Color transforms

The Python Imaging Library allows you to convert images between different pixel representations using the [`convert()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.convert) method.

### Converting between modes

```python
im = Image.open("lena.ppm").convert("L")
```

The library supports transformations between each supported mode and the “L” and “RGB” modes. To convert between other modes, you may have to use an intermediate image (typically an “RGB” image).

## Image enhancement

The Python Imaging Library provides a number of methods and modules that can be used to enhance images.

### Filters

The [`ImageFilter`](https://pillow.readthedocs.io/en/3.0.x/reference/ImageFilter.html#module-PIL.ImageFilter) module contains a number of pre-defined enhancement filters that can be used with the [`filter()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.filter) method.

#### Applying filters

```python
from PIL import ImageFilter
out = im.filter(ImageFilter.DETAIL)
```

### Point Operations

The [`point()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.point) method can be used to translate the pixel values of an image (e.g. image contrast manipulation). In most cases, a function object expecting one argument can be passed to this method. Each pixel is processed according to that function:

#### Applying point transforms

```python
# multiply each pixel by 1.2
out = im.point(lambda i: i * 1.2)
```

Using the above technique, you can quickly apply any simple expression to an image. You can also combine the [`point()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.point) and [`paste()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.paste) methods to selectively modify an image:

#### Processing individual bands

```python
# split the image into individual bands
source = im.split()

R, G, B = 0, 1, 2

# select regions where red is less than 100
mask = source[R].point(lambda i: i < 100 and 255)

# process the green band
out = source[G].point(lambda i: i * 0.7)

# paste the processed band back, but only where red was < 100
source[G].paste(out, None, mask)

# build a new multiband image
im = Image.merge(im.mode, source)
```

Note the syntax used to create the mask:

```python
imout = im.point(lambda i: expression and 255)
```

Python only evaluates the portion of a logical expression as is necessary to determine the outcome, and returns the last value examined as the result of the expression. So if the expression above is false (0), Python does not look at the second operand, and thus returns 0. Otherwise, it returns 255.

### Enhancement

For more advanced image enhancement, you can use the classes in the [`ImageEnhance`](https://pillow.readthedocs.io/en/3.0.x/reference/ImageEnhance.html#module-PIL.ImageEnhance) module. Once created from an image, an enhancement object can be used to quickly try out different settings.

You can adjust contrast, brightness, color balance and sharpness in this way.

#### Enhancing images

```python
from PIL import ImageEnhance

enh = ImageEnhance.Contrast(im)
enh.enhance(1.3).show("30% more contrast")
```

## Image sequences

The Python Imaging Library contains some basic support for image sequences (also called animation formats). Supported sequence formats include FLI/FLC, GIF, and a few experimental formats. TIFF files can also contain more than one frame.

When you open a sequence file, PIL automatically loads the first frame in the sequence. You can use the seek and tell methods to move between different frames:

### Reading sequences

```python
from PIL import Image

im = Image.open("animation.gif")
im.seek(1) # skip to the second frame

try:
    while 1:
        im.seek(im.tell()+1)
        # do something to im
except EOFError:
    pass # end of sequence
```

As seen in this example, you’ll get an `EOFError` exception when the sequence ends.

Note that most drivers in the current version of the library only allow you to seek to the next frame (as in the above example). To rewind the file, you may have to reopen it.

The following iterator class lets you use the for-statement to loop over the sequence:

### A sequence iterator class

```python
class ImageSequence:
    def __init__(self, im):
        self.im = im
    def __getitem__(self, ix):
        try:
            if ix:
                self.im.seek(ix)
            return self.im
        except EOFError:
            raise IndexError # end of sequence

for frame in ImageSequence(im):
    # ...do something to frame...
```

## Postscript printing

The Python Imaging Library includes functions to print images, text and graphics on Postscript printers. Here’s a simple example:

### Drawing Postscript

```python
from PIL import Image
from PIL import PSDraw

im = Image.open("lena.ppm")
title = "lena"
box = (1*72, 2*72, 7*72, 10*72) # in points

ps = PSDraw.PSDraw() # default is sys.stdout
ps.begin_document(title)

# draw the image (75 dpi)
ps.image(box, im, 75)
ps.rectangle(box)

# draw title
ps.setfont("HelveticaNarrow-Bold", 36)
ps.text((3*72, 4*72), title)

ps.end_document()
```

## More on reading images

As described earlier, the [`open()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.open) function of the [`Image`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#module-PIL.Image) module is used to open an image file. In most cases, you simply pass it the filename as an argument:

```python
im = Image.open("lena.ppm")
```

If everything goes well, the result is an [`PIL.Image.Image`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image) object. Otherwise, an `IOError` exception is raised.

You can use a file-like object instead of the filename. The object must implement `read()`, `seek()` and `tell()` methods, and be opened in binary mode.

### Reading from an open file

```python
fp = open("lena.ppm", "rb")
im = Image.open(fp)
```

To read an image from string data, use the `StringIO` class:

### Reading from a string

```python
import StringIO

im = Image.open(StringIO.StringIO(buffer))
```

Note that the library rewinds the file (using `seek(0)`) before reading the image header. In addition, seek will also be used when the image data is read (by the load method). If the image file is embedded in a larger file, such as a tar file, you can use the [`ContainerIO`](https://pillow.readthedocs.io/en/3.0.x/PIL.html#module-PIL.ContainerIO) or [`TarIO`](https://pillow.readthedocs.io/en/3.0.x/PIL.html#module-PIL.TarIO) modules to access it.

### Reading from a tar archive

```python
from PIL import TarIO

fp = TarIO.TarIO("Imaging.tar", "Imaging/test/lena.ppm")
im = Image.open(fp)
```

## Controlling the decoder

Some decoders allow you to manipulate the image while reading it from a file. This can often be used to speed up decoding when creating thumbnails (when speed is usually more important than quality) and printing to a monochrome laser printer (when only a greyscale version of the image is needed).

The [`draft()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.draft) method manipulates an opened but not yet loaded image so it as closely as possible matches the given mode and size. This is done by reconfiguring the image decoder.

### Reading in draft mode

```python
from __future__ import print_function
im = Image.open(file)
print("original =", im.mode, im.size)

im.draft("L", (100, 100))
print("draft =", im.mode, im.size)
```

This prints something like:

```python
original = RGB (512, 512)
draft = L (128, 128)
```

Note that the resulting image may not exactly match the requested mode and size. To make sure that the image is not larger than the given size, use the thumbnail method instead.

# Concepts

The Python Imaging Library handles *raster images*; that is, rectangles of pixel data.



## Bands

An image can consist of one or more bands of data. The Python Imaging Library allows you to store several bands in a single image, provided they all have the same dimensions and depth. For example, a PNG image might have ‘R’, ‘G’, ‘B’, and ‘A’ bands for the red, green, blue, and alpha transparency values. Many operations act on each band separately, e.g., histograms. It is often useful to think of each pixel as having one value per band.

To get the number and names of bands in an image, use the [`getbands()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.getbands) method.



## Modes

The mode of an image defines the type and depth of a pixel in the image. The current release supports the following standard modes:

> 1` (1-bit pixels, black and white, stored with one pixel per byte)
> L` (8-bit pixels, black and white)
> P` (8-bit pixels, mapped to any other mode using a color palette)
> RGB` (3x8-bit pixels, true color)
> RGBA` (4x8-bit pixels, true color with transparency mask)
> CMYK` (4x8-bit pixels, color separation)
> YCbCr` (3x8-bit pixels, color video format)
> LAB` (3x8-bit pixels, the L*a*b color space)
> HSV` (3x8-bit pixels, Hue, Saturation, Value color space)
> I` (32-bit signed integer pixels)
> F` (32-bit floating point pixels)

PIL also provides limited support for a few special modes, including `LA` (L with alpha), `RGBX` (true color with padding) and `RGBa` (true color with premultiplied alpha). However, PIL doesn’t support user-defined modes; if you to handle band combinations that are not listed above, use a sequence of Image objects.

You can read the mode of an image through the `mode` attribute. This is a string containing one of the above values.

## Size

You can read the image size through the `size` attribute. This is a 2-tuple, containing the horizontal and vertical size in pixels.

## Coordinate System

The Python Imaging Library uses a Cartesian pixel coordinate system, with (0,0) in the upper left corner. Note that the coordinates refer to the implied pixel corners; the centre of a pixel addressed as (0, 0) actually lies at (0.5, 0.5).

Coordinates are usually passed to the library as 2-tuples (x, y). Rectangles are represented as 4-tuples, with the upper left corner given first. For example, a rectangle covering all of an 800x600 pixel image is written as (0, 0, 800, 600).

## Palette

The palette mode (`P`) uses a color palette to define the actual color for each pixel.

## Info

You can attach auxiliary information to an image using the `info` attribute. This is a dictionary object.

How such information is handled when loading and saving image files is up to the file format handler (see the chapter on [Image file formats](https://pillow.readthedocs.io/en/3.0.x/handbook/image-file-formats.html#image-file-formats)). Most handlers add properties to the `info` attribute when loading an image, but ignore it when saving images.

## Filters

For geometry operations that may map multiple input pixels to a single output pixel, the Python Imaging Library provides four different resampling *filters*.

NEAREST`

  Pick the nearest pixel from the input image. Ignore all other input pixels.

BILINEAR`

  For resize calculate the output pixel value using linear interpolation on all pixels that may contribute to the output value. For other transformations linear interpolation over a 2x2 environment in the input image is used.

BICUBIC`

  For resize calculate the output pixel value using cubic interpolation on all pixels that may contribute to the output value. For other transformations cubic interpolation over a 4x4 environment in the input image is used.

LANCZOS`

  Calculate the output pixel value using a high-quality Lanczos filter (a truncated sinc) on all pixels that may contribute to the output value. In the current version of PIL, this filter can only be used with the resize and thumbnail methods.*New in version 1.1.3.

# Appendices

## Writing Your Own File Decoder

The Python Imaging Library uses a plug-in model which allows you to add your own decoders to the library, without any changes to the library itself. Such plug-ins usually have names like `XxxImagePlugin.py`, where `Xxx` is a unique format name (usually an abbreviation).

Warning

Pillow >= 2.1.0 no longer automatically imports any file in the Python path with a name ending in `ImagePlugin.py`. You will need to import your decoder manually.

A decoder plug-in should contain a decoder class, based on the `PIL.ImageFile.ImageFile` base class. This class should provide an `_open()` method, which reads the file header and sets up at least the `mode` and `size` attributes. To be able to load the file, the method must also create a list of `tile` descriptors. The class must be explicitly registered, via a call to the [`Image`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#module-PIL.Image) module.

For performance reasons, it is important that the `_open()` method quickly rejects files that do not have the appropriate contents.

## Example

The following plug-in supports a simple format, which has a 128-byte header consisting of the words “SPAM” followed by the width, height, and pixel size in bits. The header fields are separated by spaces. The image data follows directly after the header, and can be either bi-level, greyscale, or 24-bit true color.

**SpamImagePlugin.py**:

```PYTHON
from PIL import Image, ImageFile
import string

class SpamImageFile(ImageFile.ImageFile):

    format = "SPAM"
    format_description = "Spam raster image"

    def _open(self):

        # check header
        header = self.fp.read(128)
        if header[:4] != "SPAM":
            raise SyntaxError, "not a SPAM file"

        header = string.split(header)

        # size in pixels (width, height)
        self.size = int(header[1]), int(header[2])

        # mode setting
        bits = int(header[3])
        if bits == 1:
            self.mode = "1"
        elif bits == 8:
            self.mode = "L"
        elif bits == 24:
            self.mode = "RGB"
        else:
            raise SyntaxError, "unknown number of bits"

        # data descriptor
        self.tile = [
            ("raw", (0, 0) + self.size, 128, (self.mode, 0, 1))
        ]

Image.register_open("SPAM", SpamImageFile)

Image.register_extension("SPAM", ".spam")
Image.register_extension("SPAM", ".spa") # dos version
```

The format handler must always set the `size` and `mode` attributes. If these are not set, the file cannot be opened. To simplify the decoder, the calling code considers exceptions like `SyntaxError`, `KeyError`, and `IndexError`, as a failure to identify the file.

Note that the decoder must be explicitly registered using [`PIL.Image.register_open()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.register_open). Although not required, it is also a good idea to register any extensions used by this format.

## The `tile` attribute

To be able to read the file as well as just identifying it, the `tile` attribute must also be set. This attribute consists of a list of tile descriptors, where each descriptor specifies how data should be loaded to a given region in the image. In most cases, only a single descriptor is used, covering the full image.

The tile descriptor is a 4-tuple with the following contents:

```
(decoder, region, offset, parameters)
```

The fields are used as follows:

- **decoder**

  Specifies which decoder to use. The `raw` decoder used here supports uncompressed data, in a variety of pixel formats. For more information on this decoder, see the description below.

- **region**

  A 4-tuple specifying where to store data in the image.

- **offset**

  Byte offset from the beginning of the file to image data.

- **parameters**

  Parameters to the decoder. The contents of this field depends on the decoder specified by the first field in the tile descriptor tuple. If the decoder doesn’t need any parameters, use None for this field.

Note that the `tile` attribute contains a list of tile descriptors, not just a single descriptor.

## The raw decoder

The `raw` decoder is used to read uncompressed data from an image file. It can be used with most uncompressed file formats, such as PPM, BMP, uncompressed TIFF, and many others. To use the raw decoder with the [`PIL.Image.fromstring()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.fromstring) function, use the following syntax:

```
image = Image.fromstring(
    mode, size, data, "raw",
    raw mode, stride, orientation
    )
```

When used in a tile descriptor, the parameter field should look like:

```
(raw mode, stride, orientation)
```

The fields are used as follows:

- **raw mode**

  The pixel layout used in the file, and is used to properly convert data to PIL’s internal layout. For a summary of the available formats, see the table below.

- **stride**

  The distance in bytes between two consecutive lines in the image. If 0, the image is assumed to be packed (no padding between lines). If omitted, the stride defaults to 0.

**orientation**

> Whether the first line in the image is the top line on the screen (1), or the bottom line (-1). If omitted, the orientation defaults to 1.

The **raw mode** field is used to determine how the data should be unpacked to match PIL’s internal pixel layout. PIL supports a large set of raw modes; for a complete list, see the table in the `Unpack.c` module. The following table describes some commonly used **raw modes**:

| mode    | description                                                  |
| ------- | ------------------------------------------------------------ |
| `1`     | 1-bit bilevel, stored with the leftmost pixel in the most significant bit. 0 means black, 1 means white. |
| `1;I`   | 1-bit inverted bilevel, stored with the leftmost pixel in the most significant bit. 0 means white, 1 means black. |
| `1;R`   | 1-bit reversed bilevel, stored with the leftmost pixel in the least significant bit. 0 means black, 1 means white. |
| `L`     | 8-bit greyscale. 0 means black, 255 means white.             |
| `L;I`   | 8-bit inverted greyscale. 0 means white, 255 means black.    |
| `P`     | 8-bit palette-mapped image.                                  |
| `RGB`   | 24-bit true colour, stored as (red, green, blue).            |
| `BGR`   | 24-bit true colour, stored as (blue, green, red).            |
| `RGBX`  | 24-bit true colour, stored as (blue, green, red, pad).       |
| `RGB;L` | 24-bit true colour, line interleaved (first all red pixels, the all green pixels, finally all blue pixels). |

Note that for the most common cases, the raw mode is simply the same as the mode.

The Python Imaging Library supports many other decoders, including JPEG, PNG, and PackBits. For details, see the `decode.c` source file, and the standard plug-in implementations provided with the library.

## Decoding floating point data

PIL provides some special mechanisms to allow you to load a wide variety of formats into a mode `F` (floating point) image memory.

You can use the `raw` decoder to read images where data is packed in any standard machine data type, using one of the following raw modes:

| mode     | description                            |
| -------- | -------------------------------------- |
| `F`      | 32-bit native floating point.          |
| `F;8`    | 8-bit unsigned integer.                |
| `F;8S`   | 8-bit signed integer.                  |
| `F;16`   | 16-bit little endian unsigned integer. |
| `F;16S`  | 16-bit little endian signed integer.   |
| `F;16B`  | 16-bit big endian unsigned integer.    |
| `F;16BS` | 16-bit big endian signed integer.      |
| `F;16N`  | 16-bit native unsigned integer.        |
| `F;16NS` | 16-bit native signed integer.          |
| `F;32`   | 32-bit little endian unsigned integer. |
| `F;32S`  | 32-bit little endian signed integer.   |
| `F;32B`  | 32-bit big endian unsigned integer.    |
| `F;32BS` | 32-bit big endian signed integer.      |
| `F;32N`  | 32-bit native unsigned integer.        |
| `F;32NS` | 32-bit native signed integer.          |
| `F;32F`  | 32-bit little endian floating point.   |
| `F;32BF` | 32-bit big endian floating point.      |
| `F;32NF` | 32-bit native floating point.          |
| `F;64F`  | 64-bit little endian floating point.   |
| `F;64BF` | 64-bit big endian floating point.      |
| `F;64NF` | 64-bit native floating point.          |

## The bit decoder

If the raw decoder cannot handle your format, PIL also provides a special “bit” decoder that can be used to read various packed formats into a floating point image memory.

To use the bit decoder with the fromstring function, use the following syntax:

```
image = fromstring(
    mode, size, data, "bit",
    bits, pad, fill, sign, orientation
    )
```

When used in a tile descriptor, the parameter field should look like:

```
(bits, pad, fill, sign, orientation)
```

The fields are used as follows:

- **bits**

  Number of bits per pixel (2-32). No default.

- **pad**

  Padding between lines, in bits. This is either 0 if there is no padding, or 8 if lines are padded to full bytes. If omitted, the pad value defaults to 8.

- **fill**

  Controls how data are added to, and stored from, the decoder bit buffer.

- **fill=0**

  Add bytes to the LSB end of the decoder buffer; store pixels from the MSB end.

- **fill=1**

  Add bytes to the MSB end of the decoder buffer; store pixels from the MSB end.

- **fill=2**

  Add bytes to the LSB end of the decoder buffer; store pixels from the LSB end.

- **fill=3**

  Add bytes to the MSB end of the decoder buffer; store pixels from the LSB end.If omitted, the fill order defaults to 0.

- **sign**

  If non-zero, bit fields are sign extended. If zero or omitted, bit fields are unsigned.

- **orientation**

  Whether the first line in the image is the top line on the screen (1), or the bottom line (-1). If omitted, the orientation defaults to 1.





# Reference

## ImageFilter Module

The `ImageFilter` module contains definitions for a pre-defined set of filters, which can be be used with the [`Image.filter()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.filter) method.

---

### Example: Filter an image

```python
from PIL import ImageFilter

im1 = im.filter(ImageFilter.BLUR)

im2 = im.filter(ImageFilter.MinFilter(3))
im3 = im.filter(ImageFilter.MinFilter)  # same as MinFilter(3)
```

--------

### Filters

The current version of the library provides the following set of predefined image enhancement filters:

- BLUR
- CONTOUR
- DETAIL
- EDGE_ENHANCE
- EDGE_ENHANCE_MORE
- EMBOSS
- FIND_EDGES
- SMOOTH
- SMOOTH_MORE
- SHARPEN

------

### Function

#### Gaussian blur

```python
PIL.ImageFilter.GaussianBlur(radius=2)
```

Gaussian blur filter.

**Parameters:**

> **radius** – Blur radius.





#### UnsharpMask

```python
PIL.ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3)
```

Unsharp mask filter.See Wikipedia’s entry on [digital unsharp masking](https://en.wikipedia.org/wiki/Unsharp_masking#Digital_unsharp_masking) for an explanation of the parameters.

**Parameters:**

> **radius** – Blur Radius
>
> **percent** – Unsharp strength, in percent
>
> **threshold** – Threshold controls the minimum brightness change that will be sharpened





#### Kernel

```python
PIL.ImageFilter.Kernel(size, kernel, scale=None, offset=0)
```

Create a convolution kernel. The current version only supports 3x3 and 5x5 integer and floating point kernels.In the current version, kernels can only be applied to “L” and “RGB” images.

**Parameters:**

> **size** – Kernel size, given as (width, height). In the current version, this must be (3,3) or (5,5).
>
> **kernel** – A sequence containing kernel weights.
>
> **scale** – Scale factor. If given, the result for each pixel is divided by this value. the default is the sum of the kernel weights.
>
> **offset** – Offset. If given, this value is added to the result, after it has been divided by the scale factor.





#### RankFilter

```python
PIL.ImageFilter.RankFilter(size, rank)
```

Create a rank filter. The rank filter sorts all pixels in a window of the given size, and returns the **rank**‘th value.

**Parameters:**

> **size** – The kernel size, in pixels.
>
> **rank** – What pixel value to pick. Use 0 for a min filter, `size * size / 2` for a median filter, `size * size - 1` for a max filter, etc.





#### MedianFilter

```python
PIL.ImageFilter.MedianFilter(size=3)
```

Create a median filter. Picks the median pixel value in a window with the given size.

**Parameters:**

> **size** – The kernel size, in pixels.





#### MinFilter

```python
PIL.ImageFilter.MinFilter(size=3)
```

Create a min filter. Picks the lowest pixel value in a window with the given size.

**Parameters:**

> **size** – The kernel size, in pixels.





#### MaxFilter

```python
PIL.ImageFilter.MaxFilter(size=3)
```

Create a max filter. Picks the largest pixel value in a window with the given size.

**Parameters:**

> **size** – The kernel size, in pixels.





#### ModeFilter

```python
PIL.ImageFilter.ModeFilter(size=3)
```

Create a mode filter. Picks the most frequent pixel value in a box with the given size. Pixel values that occur only once or twice are ignored; if no pixel value occurs more than twice, the original pixel value is preserved.

**Parameters:**

> **size** – The kernel size, in pixels.





## ImageChops Module

The `ImageChops` module contains a number of arithmetical image operations, called channel operations (“chops”). These can be used for various purposes, including special effects, image compositions, algorithmic painting, and more.

For more pre-made operations, see `ImageOps`.

At this time, most channel operations are only implemented for 8-bit images (e.g. “L” and “RGB”).

### Functions

Most channel operations take one or two image arguments and returns a new image. Unless otherwise noted, the result of a channel operation is always clipped to the range 0 to MAX (which is 255 for all modes supported by the operations in this module).

**All Return type:`Image`**



#### Add

```python
PIL.ImageChops.add(image1, image2, scale=1.0, offset=0)
```

  Adds two images, dividing the result by scale and adding the offset. If omitted, scale defaults to 1.0, and offset to 0.0.

`out = ((image1 + image2) / scale + offset) `



#### Add_modulo

```python
PIL.ImageChops.add_modulo(image1, image2)
```

  Add two images, without clipping the result.

`out = ((image1 + image2) % MAX) `



#### blend

```python
PIL.ImageChops.blend(image1, image2, alpha)
```

  Blend images using constant transparency weight. Alias for `PIL.Image.Image.blend()`.



#### Composite

```python
PIL.ImageChops.composite(image1, image2, mask)
```

  Create composite using transparency mask. Alias for `PIL.Image.Image.composite()`.



#### Constant

```python
PIL.ImageChops.constant(image, value)
```

  Fill a channel with a given grey level.



#### Darker

```python
PIL.ImageChops.darker(image1, image2)
```

  Compares the two images, pixel by pixel, and returns a new image containing the darker values.

`out = min(image1, image2) `



#### Difference

```python
PIL.ImageChops.difference(image1, image2)
```

  Returns the absolute value of the pixel-by-pixel difference between the two images.

`out = abs(image1 - image2) `



#### Duplicate

```python
PIL.ImageChops.duplicate(image)
```

  Copy a channel. Alias for [`PIL.Image.Image.copy()`](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.copy).



#### Invert(反色)

```python
PIL.ImageChops.invert(image)
```

  Invert an image (channel).

`out = MAX - image `



#### Light

```python
PIL.ImageChops.lighter(image1, image2)
```

  Compares the two images, pixel by pixel, and returns a new image containing the lighter values.

`out = max(image1, image2) `



#### Logical_and

```python
PIL.ImageChops.logical_and(image1, image2)
```

  Logical AND between two images.

`out = ((image1 and image2) % MAX) `



#### Logical_or

```python
PIL.ImageChops.logical_or(image1, image2)
```

  Logical OR between two images.

`out = ((image1 or image2) % MAX) `



#### Multiply

```python
PIL.ImageChops.multiply(image1, image2)
```

  Superimposes two images on top of each other.If you multiply an image with a solid black image, the result is black. If you multiply with a solid white image, the image is unaffected.

`out = image1 * image2 / MAX `



#### Offset

```python
PIL.ImageChops.offset(image, xoffset, yoffset=None)
```

  Returns a copy of the image where data has been offset by the given distances. Data wraps around the edges. If **yoffset** is omitted, it is assumed to be equal to **xoffset**.Parameters:**xoffset** – The horizontal distance.**yoffset** – The vertical distance. If omitted, both distances are set to the same value.



#### Screen

```python
PIL.ImageChops.screen(image1, image2)
```

  Superimposes two inverted images on top of each other.`out = MAX - ((MAX - image1) * (MAX - image2) / MAX) `



#### Subtract

```python
PIL.ImageChops.subtract(image1, image2, scale=1.0, offset=0)
```

  Subtracts two images, dividing the result by scale and adding the offset. If omitted, scale defaults to 1.0, and offset to 0.0.`out = ((image1 - image2) / scale + offset) `



#### subtract_modulo

```python
PIL.ImageChops.subtract_modulo(image1, image2)
```

  Subtract two images, without clipping the result.`out = ((image1 - image2) % MAX) `