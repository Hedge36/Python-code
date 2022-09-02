## Anoconda升级方法

可在命令窗口通过conda直接升级组件或者通过管理员的身份启动 Anaconda Prompt来升级组组件，具体命令如下：

更新所有库

```
conda update --all
```

更新 conda 自身

```
conda update conda
```

pip更新

```
python -m pip install --user --upgrade pip
```

若pip损坏则需执行以下代码即可

```
easy_install pip
```

## Python配置清华镜像源

### 1. 前言

> 使用pip 安装服务器在国外的python 库时，下载需要很长时间，在配置文件中设置国内镜像可以提高速度，清华镜像源就是其中之一。
>

#### 2. pypi 镜像使用帮助

网址：https://mirrors.tuna.tsinghua.edu.cn/help/pypi/

#### 3. 临时配置

若只是临时下载一个python库的话，则可使用以下命令进行配置：

```python
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

说明：“some-package”为要下载的python库名（或称作包名）。

#### 4. 默认配置（永久配置）

```python
pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/
```

说明：

> （1）“pip install pip -U”是用于执行升级pip的命令；
>
> （2）若pip为10.0.0以上版本，则可以进行升级；
>
> （3）查看pip版本的命令：pip -V

### 5. 查看当前镜像源

```bash
pip config list
```

### 6. 常用源

> 阿里云：http://mirrors.aliyun.com/pypi/simple/
>
> 清华大学：https://pypi.tuna.tsinghua.edu.cn/simple/
>
> 中国科技大学：https://pypi.mirrors.ustc.edu.cn/simple/
>
> 中国科学技术大学：http://pypi.mirrors.ustc.edu.cn/simple/
>
> 豆瓣：https://pypi.douban.com/simple/

## pip-review更新所有python包

下面列出一些常用的pip操作：

> pip --version  # 查看版本和路径
>
> pip install -U pip  # 更新pip
>
> pip install SomePackage  # 安装包
>
> pip install --upgrade SomePackage  # 更新包
>
> pip uninstall SomePackage  # 卸载包
>
> pip show SomePackage  # 显示安装包信息
>
> pip search SomePackage  # 搜索包
>
> pip list  # 列出已安装的包
>
> pip list -o  # 列出可升级的包

 当我们想要一次性更新很多包时，使用pip则较为繁琐，这时可以安装并使用 pip-review 来实现：

> pip install pip-review  # 安装 pip-review
>
> pip-review  # 查看可更新的包
>
> pip-review --auto  # 自动更新所有包
>
> pip-review --local --interactive  # 更新包，提供操作可选项：[Y]es, [N]o, [A]ll, [Q]uit

问题出个无法更新 pycurl 这个包，可以先单独把这个包更新以后再重新运行 pip-review --auto 命令。顺便吐槽一下，这个命令好像是先全部下载下来所有更新包以后再安装？所以中间出了一个错误就全部安装失败了。。
