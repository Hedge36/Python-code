# [如何给自己的Python项目制作安装包](https://www.cnblogs.com/gongdiwudu/p/11070798.html)

# [1.Packaging Python Projects¶](https://packaging.python.org/tutorials/packaging-projects/)


本教程将指导您如何打包一个简单的Python项目。它将向您展示如何添加必要的文件和结构来创建包，如何构建包以及如何将其上载到Python包索引。

## A simple project


本教程使用名为example_pkg的简单项目。如果您不熟悉Python的模块和导入包，请花几分钟时间阅读包含文件包和模块的Python文档。即使您已经有一个要打包的项目，我们仍然建议您按照本示例包使用此示例包，然后尝试使用自己的包。 要在本地创建此项目，请创建以下文件结构：

```
/packaging_tutorial
  /example_pkg
    __init__.py
```


创建此结构后，您将需要在顶级文件夹中运行本教程中的所有命令 - 因此请务必使用cd packaging_tutorial。 您还应该编辑example_pkg / __ init__.py并将以下代码放在其中：

```
name = "example_pkg"
```


这只是为了让您可以在本教程后面验证它是否正确安装，并且PyPI不会使用它。

## Creating the package files


您现在将创建一些文件来打包此项目并准备分发。创建下面列出的新文件 - 您将在以下步骤中向其添加内容。

```
/packaging_tutorial
  /example_pkg
    __init__.py
  setup.py
  LICENSE
  README.md
```

## Creating setup.py

```
setup.py是setuptools的构建脚本。它告诉setuptools你的包（例如名称和版本）以及要包含的代码文件。

打开setup.py并输入以下内容。更新程序包名称以包含您的用户名（例如，example-pkg-theacodes），这可确保您拥有唯一的程序包名称，并且您的程序包不会与本教程后其他人上传的程序包冲突。
 
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-your-username",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)setup（）需要几个参数。此示例包使用相对最小的集：

name是包的分发名称。只要包含字母，数字，_和 - ，这可以是任何名称。它也不能在pypi.org上使用。请务必使用您的用户名更新此内容，因为这样可确保您不会尝试上传与上传程序包时已存在的程序包相同的程序包。
版本是包版本，请参阅PEP 440以获取有关版本的更多详细信息。
author和author_email用于标识包的作者。
描述是包的简短的一句话摘要。
long_description是包的详细描述。这显示在Python Package Index的包详细信息包中。在这种情况下，从README.md加载长描述，这是一种常见模式。
long_description_content_type告诉索引用于长描述的标记类型。在这种情况下，它是Markdown。
url是项目主页的URL。对于许多项目，这只是一个指向GitHub，GitLab，Bitbucket或类似代码托管服务的链接。
packages是应包含在分发包中的所有Python导入包的列表。我们可以使用find_packages（）自动发现所有包和子包，而不是手动列出每个包。在这种情况下，包列表将是example_pkg，因为它是唯一存在的包。
分类器为索引提供一些关于包的其他元数据。在这种情况下，该软件包仅与Python 3兼容，根据MIT许可证进行许可，并且与操作系统无关。您应始终至少包含您的软件包所使用的Python版本，软件包可用的许可证以及您的软件包将使用的操作系统。有关分类器的完整列表，请参阅https://pypi.org/classifiers/。
除了这里提到的还有很多。有关详细信息，请参阅打包和分发项目。
```

## Creating README.md


打开README.md并输入以下内容。如果您愿意，可以自定义此项。

```
# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.
```

## Creating a LICENSE


上传到Python Package Index的每个包都包含许可证，这一点很重要。这告诉用户安装您的软件包可以使用您的软件包的条款。有关选择许可证的帮助，请访问：http：//choosealicense.com/。选择许可证后，打开LICENSE并输入许可证文本。例如，如果您选择了MIT许可证：

```
Copyright (c) 2018 The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

##  生成分发档案

下一步是为包生成分发包。这些是上传到包索引的档案，可以通过pip安装。 确保安装了最新版本的setuptools和wheel：

```
python3 -m pip install --user --upgrade setuptools wheel
```


小费  如果您在安装它们时遇到问题，请参阅安装包教程。 现在从setup.py所在的同一目录运行此命令：

```
python3 setup.py sdist bdist_wheel
```


此命令应输出大量文本，一旦完成，应在dist目录中生成两个文件：

```
dist/
  example_pkg_your_username-0.0.1-py3-none-any.whl
  example_pkg_your_username-0.0.1.tar.gz
```

Note

```
如果您遇到麻烦，请复制输出并提出有关包装问题的问题，我们会尽力为您提供帮助！

tar.gz文件是源存档，而.whl文件是构建的分发。较新的pip版本优先安装构建的发行版，但如果需要，将回退到源代码存档。您应该始终上传源存档并为项目兼容的平台提供构建的存档。在这种情况下，我们的示例包在任何平台上都与Python兼容，因此只需要一个构建的发行版。
```

## Uploading the distribution archives


最后，是时候将您的包上传到Python Package Index了！ 您需要做的第一件事是在Test PyPI上注册一个帐户。 Test PyPI是用于测试和实验的包索引的单独实例。这对于像我们不一定想要上传到真实索引的本教程这样的东西很棒。要注册帐户，请访问https://test.pypi.org/account/register/并完成该页面上的步骤。在您上传任何套餐之前，您还需要验证您的电子邮件地址。有关Test PyPI的更多详细信息，请参阅使用TestPyPI。 现在您已注册，您可以使用twine上传分发包。你需要安装Twine：

```
python3 -m pip install --user --upgrade twine
```


安装完成后，运行Twine上传dist下的所有档案：

```
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```


系统将提示您输入使用Test PyPI注册的用户名和密码。命令完成后，您应该看到与此类似的输出：

```
Uploading distributions to https://test.pypi.org/legacy/
Enter your username: [your username]
Enter your password:
Uploading example_pkg_your_username-0.0.1-py3-none-any.whl
100%|█████████████████████| 4.65k/4.65k [00:01<00:00, 2.88kB/s]
Uploading example_pkg_your_username-0.0.1.tar.gz
100%|█████████████████████| 4.25k/4.25k [00:01<00:00, 3.05kB/s]
上传后，您的包应该可以在TestPyPI上查看，例如
```

, https://test.pypi.org/project/example-pkg-your-username

## Installing your newly uploaded package


您可以使用pip来安装包并验证它是否有效。创建一个新的virtualenv（请参阅安装包以获取详细说明）并从TestPyPI安装包：

```
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-your-username
```

Make sure to specify your username in the package name
确保在包名中指定您的用户名！ pip应该从Test PyPI安装包，输出应该如下所示：

```
Collecting example-pkg-your-username
  Downloading https://test-files.pythonhosted.org/packages/.../example-pkg-your-username-0.0.1-py3-none-any.whl
Installing collected packages: example-pkg-your-username
Successfully installed example-pkg-your-username-0.0.1
```

Note

```
此示例使用--index-url标志指定TestPyPI而不是实时PyPI。另外，它指定--no-deps。由于TestPyPI与实时PyPI没有相同的包，因此尝试安装依赖项可能会失败或安装意外的事情。虽然我们的示例包没有任何依赖关系，但在使用TestPyPI时避免安装依赖项是一种很好的做法。

您可以通过导入模块并引用之前放在__init__.py中的name属性来测试它是否已正确安装。

运行Python解释器（确保你仍然在你的virtualenv中）：
python
```


然后导入模块并打印出name属性。无论您在setup.py中给出的分发包名称是什么（在本例中为example-pkg-your-username），这都应该是相同的，因为您的import包是example_pkg。

\>>>

```
>>> import example_pkg
>>> example_pkg.name
'example_pkg'
```

## Next steps

**Congratulations, you’ve packaged and distributed a Python project!** ✨ 🍰 ✨

```
请记住，本教程向您展示了如何将程序包上传到Test PyPI，它不是永久存储。测试系统偶尔会删除软件包和帐户。最好使用Test PyPI进行测试和实验，如本教程。
```

# 2.Python 包制作

[官方文档](https://packaging.python.org/overview/)

## Python 包目录

> - ```
>   /package_parent_folder
>   ```
>
>   - ```
>     /package
>     ```
>
>     - `/__init__.py`

在`__init__.py`文件内添加`name = package`，其中`package`指的是`包名`

在`package_parent_folder`下添加包文件`setup.py`、`LICENSE`、`README.md`文件。

LICENSE: 包许可说明

README.md: 包说明文件

setup.py: 包安装设置文件

> [设置文档](https://packaging.python.org/tutorials/packaging-projects/#creating-setup-py)
>
> [设置项文档](https://packaging.python.org/guides/distributing-packages-using-setuptools/)

## 安装Python包制作依赖

1. setuptools
2. wheel

## 制作Python包

> python3 setup.py sdist bdist_wheel

 生成文件：

- /dist
  - package-yourname-version-*.whl
  - package_yourname-version-*.tar.gz

## 上传Python包

### 安装上传依赖

1. twine

### Test Pypi

##### 注册账号测试网站上传

```
> python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

##### 下载测试

```shell
python3 -m pip install --index-url https://test.pypi.org/simple/ example-pkg-your-username
```

PyPi上传

##### 注册账号上传

```shell
twine upload dist/*
```

> 报错：invalid command 'bdist_wheel'
>
> > 安装wheel



大家好 我又来了 这次给大家介绍如何在Python里自己制作一个包，并且安装。

------

我的Python环境设置：

- Python3.7 64位版本
- 自带IDLE
- Windows 7 专业版（说白了就是盗版）

------

总目录如下：

```
mymodule
| test
|   |  __init__.py
|   └ helloworld.py
└    setup.py
12345
```

------

首先，我们在Python的安装目录里新建一个文件夹（哪里都行，新建在安装目录里纯属方便）。



# 3.自制包方法

如，我们新建文件夹mymodule（任意名称都可）：![新建文件夹](https://img-blog.csdnimg.cn/20200708164153253.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjYyNDg0OA==,size_16,color_FFFFFF,t_70#pic_center)
进入目录，再新建一个文件夹，如test（要根据你想要包的名字重命名）：![再次新建](https://img-blog.csdnimg.cn/20200708164834885.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjYyNDg0OA==,size_16,color_FFFFFF,t_70#pic_center)
进入目录，新建文件__init__.py（不能更改其他）：![新建文件__init__.py](https://img-blog.csdnimg.cn/20200708165043446.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjYyNDg0OA==,size_16,color_FFFFFF,t_70#pic_center)
接下来，把你的Python源文件放到与__init__.py同一文件夹下。我这里就放个helloworld ~ (≧▽≦)/~啦啦啦

```python
'''
    helloworld.py
'''
print("Hi, I'm 叶·少·Great·Man\n------")
def hello():
    print('Hello, CSDN')
hello()
1234567
```

#### 重头戏到了！请将你的身体调至清醒状态！

回到mymodule目录下，新建文件setup.py，内容：

```python
import setuptools

setuptools.setup(
    name="test",
    version="5.2.0",
    author="叶·少·Great·Man",
    author_email="andysoftwareexp.co@qq.com",
    description="",
    long_description="test Module",
    long_description_content_type="text",
    url="http://baidu.com/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
123456789101112131415161718
其中，一些属性可以自由更改：
name属性：包的名字
version属性：包的版本
author属性：包的作者
author_email属性：包作者的邮件地址
description属性：包的描述
url属性：一个网址
1234567
```

保存，然后进入命令行窗口：![cmd窗口](https://img-blog.csdnimg.cn/20200708171010949.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjYyNDg0OA==,size_16,color_FFFFFF,t_70#pic_center)
输入以下代码：`python setup.py sdist`
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200708171459888.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjYyNDg0OA==,size_16,color_FFFFFF,t_70#pic_center)
当出现`removing 'test-5.2.0' (and everything under it)`时，你的包的`.tar.gz`文件就创建好了。

##### 安装

命令行输入：
`pip install "F:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\mymodu le\dist\test-5.2.0.tar.gz"`（我这里是相对路径，根据创建的包的路径进行更改）。
回车，执行。![install](https://img-blog.csdnimg.cn/20200708172053813.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjYyNDg0OA==,size_16,color_FFFFFF,t_70#pic_center)
出现`Successfully installed test-5.2.0`时，你的包就安装好了！进入Python运行试一下![import](https://img-blog.csdnimg.cn/20200708172303561.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjYyNDg0OA==,size_16,color_FFFFFF,t_70#pic_center)

###### 注意，使用包里的文件是使用`from test import helloworld`而不是直接导入`import test`

------

#### 大功告成

------

##### 更多功能

![help test](https://img-blog.csdnimg.cn/20200708172753107.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjYyNDg0OA==,size_16,color_FFFFFF,t_70#pic_center)
你们可能会问，为啥`help`其他的模块会有`DESCRIPTION`呢？如![help turtle](https://img-blog.csdnimg.cn/20200708173007442.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjYyNDg0OA==,size_16,color_FFFFFF,t_70#pic_center)
这是为什么？我翻了一下，发现原来是……
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
在包的__init__.py文件里添加多行注释！
就像这样，在__init__.py里添加多行注释：

```python
'''
test pakage module CSDN is good
I'm So great
'''
1234
```

再次编译，安装![reinstall](https://img-blog.csdnimg.cn/20200708173556111.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjYyNDg0OA==,size_16,color_FFFFFF,t_70#pic_center)
命令行：
`python`
`help()`
`test`
搞定！