# Pygame库基本语法

## pygame最小框架

```python
import pygame,sys
pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("pygame游戏之旅")
while True:
  for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
pygame.display.update()
```

 

pygame.init()										初始化pygame库所有函数的默认值

window = pygame.display.set_mode([width,height])		创建窗口;

clock.tick(framerate)								控制帧频率(次/秒);

image = pygame.image.load("res/game.ico")				加载资源图片，返回一个surface图												片对象,形成一个与图片对象紧密相												切的矩形，支持jpg，png，gif（非动												画）等13种常用图片格式;

pygame.display.set_caption(title,icontitle=None)			设置窗口标题及窗口小标题

pygame.display.get_caption(title,icontitle=None)			返回窗口标题及窗口小标题pygame.display.set_mode(r=(0,0),flags=0)				设置大小，其中r是游戏的分辨率，												采用(width,height)方式输入，flages												用来控制显示类型，可用|组合使用，												常用标签有:pygame.RESIZABLE(窗口可调节),pygame.NOFRAME(无边界显示),pygame.FULLSCREEN(全屏显示)

pygame.display.set_icon(surface)						设置窗口图标

pygame.display.Info()

\# 更新界面

pygame.display.update()								全屏幕更新

pygame.display.filp()								动态部分更新

pygame.display.update()

 

事件：
pygame.event.KEYDOWN

pygame.event.UP

Key

Mod(修饰符),如：KMOD_LSHIFT，KMOD_SHIFT | KMOD_ALT

事件处理函数：

pygame.event.get()								获取所有事件列表

pygame.event.poll()							获取并删除一个事件

pygame.event.clear()  						清理所有事件        

pygame.event.set_blocked(type or typelist)			控制某些事件不被保存到事件队列中

pygame.event.get_blocked(type)					测试事件类型是否被事件队列被禁止

pygame.event.set_allowed(type or typelist)			控制某些事件能被保存到事件队列中

pygame.event.post(Event)						生成一个事件并将其放入事件队列

pygame.event.Event(type,dict)					创建一个指定类型事件

alpha通道表示不透明度

pygame.color

pygame.freetype.font(file, size=0)

Pygame.freetype.render_to(surf, dest, text, fgcolor=none, bgcolor=none, rotation=0, size=0)

 

 

 

 

## mixer.music

Pygame 中控制音频流的模块。

### 主函数

> pygame.mixer.music.load()  ——  载入一个音乐文件用于播放
>
>
> pygame.mixer.music.play()  ——  开始播放音乐流
>
> pygame.mixer.music.rewind()  ——  重新开始播放音乐
>
> pygame.mixer.music.stop()  ——  结束音乐播放
>
> pygame.mixer.music.pause()  ——  暂停音乐播放
>
> pygame.mixer.music.unpause()  ——  恢复音乐播放
>
> pygame.mixer.music.fadeout()  ——  淡出的效果结束音乐播放
>
> pygame.mixer.music.set_volume()  ——  设置音量
>
> pygame.mixer.music.get_volume()  ——  获取音量
>
> pygame.mixer.music.get_busy()  ——  检查是否正在播放音乐
>
> pygame.mixer.music.set_pos()  ——  设置播放的位置
>
> pygame.mixer.music.get_pos()  ——  获取播放的位置
>
> pygame.mixer.music.queue()  ——  将一个音乐文件放入队列中，并排在当前播放的音乐之后
>
> pygame.mixer.music.set_endevent()  ——  当播放结束时发出一个事件
>
> pygame.mixer.music.get_endevent()  ——  获取播放结束时发送的事件
> Pygame 中播放音乐的模块和 pygame.mixer 模块是密切联系的。使用音乐模块去控制在调音器上的音乐播放。

音乐（music）播放和声音（sound）播放的不同之处在于音乐是流式的，并且绝对不会在一开始就把一个音乐文件全部载入。调音系统在工作刚开始时仅支持单音乐流。

注意：对于 MP3 格式的支持是受限制的。在一些系统上，一种不受支持的格式将会是系统崩溃，例如 Debian Linux。为了游戏的稳定性，建议使用 OGG 进行替代。

### 函数详解

pygame.mixer.music.load()

载入一个音乐文件用于播放。

> load(filename) -> None
>
> load(object) -> None
>

该函数将会载入一个音乐文件名或者文件对象，并且准备播放。如果已经有音乐流正在播放，该音乐流将被停止。另外，函数不会开始播放音乐。



pygame.mixer.music.play()

开始播放音乐流。



play(loops=0, start=0.0) -> None

该函数用于播放已载入的音乐流。如果音乐已经开始播放，则将会重新开始播放。

loops 参数控制重复播放的次数，例如 play(5) 意味着被载入的音乐将会立即开始播放 1 次并且再重复 5 次，共 6 次。如果 loops = -1，则表示无限重复播放。

start 参数控制音乐从哪里开始播放。开始的位置取决于音乐的格式。MP3 和 OGG 使用时间表示播放位置（以秒为单位）。MOD使用模式顺序编号表示播放位置。如果音乐文件无法设置开始位置，则传递了start参数后会产生一个NotImplementedError 错误。



pygame.mixer.music.rewind()

重新开始播放音乐。



rewind() -> None

从文件开头开始重新播放音乐。



pygame.mixer.music.stop()
结束音乐播放。

stop() -> None

如果音乐正在播放则立即结束播放。



pygame.mixer.music.pause()
暂停音乐流的播放。

pause() -> None

通过调用 pygame.mixer.music.unpause() 函数继续播放音乐。



pygame.mixer.music.unpause()
恢复音乐播放。

unpause() -> None

在播放暂停后使用该函数可以继续音乐流的播放。



pygame.mixer.music.fadeout()
淡出的效果结束音乐播放。

fadeout(time) -> None

该函数将会在音乐淡出（也就是不在有声音放出）一段指定长度的时间（以毫秒为单位）后结束播放。

注意：该函数在调用后会一直处于阻塞状态，直到音乐已经淡出。



pygame.mixer.music.set_volume()
设置音量。



set_volume(value) -> None

设置音乐的播放音量。

value 参数值范围为 0.0~1.0。当新的音乐文件被载入，音量会被重置。



pygame.mixer.music.get_volume()
获取音量。



get_volume() -> value

返回正在播放的音乐的音量（此音量应该是调音器音量，注意与其他音量参数区分）。返回值范围为 0.0~1.0。



pygame.mixer.music.get_busy()
检查是否正在播放音乐。

get_busy() -> bool

如果有音乐流正在播放，此方法返回 True。否则返回 False。



pygame.mixer.music.set_pos()
设置播放的位置。

set_pos(pos) -> None

设置播放的起始位置。pos 参数是一个浮点数（或者一个可以转换为浮点数的数值），其值取决于音乐文件的格式：

对于 MOD 文件，它是模块中的整型模式号；

对于 OGG 文件，它是一个以音频开头为零点的绝对时间值（以秒为单位）；

对于 MP3 文件，它是以当前播放位置为零点的绝对时间值（以秒为单位）。

为了对一个 MP3 文件的进行绝对定位，建议首先调用 rewind() 函数（其他文件格式不受支持）。SDL_mixer 更新的版本提供了更好的定位支持。如果一种特殊的格式不支持定位，将会产生一个 SDLError 错误。

该函数会调用 SDL_mixer 内的 Mix_SetMusicPosition() 函数。



pygame.mixer.music.get_pos()

获取播放的位置。



get_pos() -> time

此函数会获得音乐的播放时长（以毫秒为单数的数值）。返回值仅代表已经音乐已经播放了多久，并不考虑任何起始位置偏移量。



pygame.mixer.music.queue()

将一个音乐文件放入队列中，并排在当前播放的音乐之后。



queue(filename) -> None

此函数将会载入一个音乐文件并将其放入队列中。当前的音乐一旦播放完毕，正在排队的音乐文件就会开始播放。如果当前音乐被人为停止或者切换到其他音乐，则正在排队的音乐会被丢弃。

下面的示例意思是先播放 6 次 Bach 然后再播放 1 次 Mozart：

pygame.mixer.music.load('bach.ogg')

pygame.mixer.music.play(5)        # Plays six times, not five!

pygame.mixer.music.queue('mozart.ogg')

pygame.mixer.music.set_endevent()



当播放结束时发出一个事件。

set_endevent() -> None

set_endevent(type) -> None

调用此函数会使 Pygame 在音乐结束播放后发出信号（通过事件队列）。

type 参数决定了什么样的事件将被放入事件队列中。

任何时候音乐结束，都会放入指定事件到队列中（不仅仅是第一次）。调用该函数并不带任何参数，表示停止投放事件到队列中。

pygame.mixer.music.get_endevent()
获取播放结束时发送的事件。

get_endevent() -> type

返回音乐结束时被放入队列的事件类型。

如果没有指定 endevent 事件，此方法会返回 pygame.NOEVENT 。


















































另外说一下，就产品而言，Pygame更致力于2D游戏的开发，也就是说，你可以用Pygame写一个植物大战僵尸，但是写一个魔兽世界则相当困难……请不要做出鄙夷的目光，底层的东西永远是相通的，而且对于新手而言，从简单的2D入手才是正途。

 

使用Pygame

 

模块名	功能

pygame.cdrom	访问光驱

pygame.cursors	加载光标

pygame.display	访问设备显示

pygame.draw		绘制形状、线和点

pygame.event		管理事件

pygame.font		使用字体

pygame.image		加载和存储图片

pygame.joystick	使用手柄或类似的东西

pygame.key		读取键盘按键

pygame.mixer		声音

pygame.mouse	鼠标

pygame.movie		播放视频

pygame.music		播放音频

pygame.overlay	访问高级视频叠加

pygame.rect		管理矩形区域

pygame.sndarray	操作声音数据

pygame.sprite		操作移动图像

pygame.surface	管理图像和屏幕

pygame.surfarray	管理点阵图像数据

pygame.time		管理时间和帧信息

pygame.transform	缩放和移动图像

有些模块可能在某些平台上不存在，你可以用None来测试一下。

 

if pygame.transform is None:

  print 'The transform module is not available!'

  exit()

Hello Pygame

刚开始学习一门编程语言的时候总会写一个Hello World程序，但那只是在终端上打印一句话，现在我们来点更帅的！写好以后会是这样子的效果：

 

 

代码如下：

 

\# _*_ coding: utf-8 _*_

import pygame

 

from pygame.locals import *

from sys import exit

background_image_filename = 'sea.jpg'

mouse_image_filename = 'fish.png'

 

\# 初始化pygame，为使用硬件做准备

pygame.init()

 

\# 创建一个窗口

screen = pygame.display.set_mode((640, 480), 0, 32)

 

\# 设置窗口标题

pygame.display.set_caption("hello,world!")

 

\# 加载图片并转换

background = pygame.image.load(background_image_filename)

mouse_cursor = pygame.image.load(mouse_image_filename)

 

\# 游戏主循环

while True:

  for event in pygame.event.get():

​    if event.type == QUIT:

​      \# 接收到退出时间后退出程序

​      exit()

 

  \# 将背景图画上去

  screen.blit(background, (0, 0))

 

  \# 获得鼠标位置

  x, y = pygame.mouse.get_pos()

  \# 计算光标左上角位置

  x -= mouse_cursor.get_width() / 2

  y -= mouse_cursor.get_height() / 2

 

  \# 将光标画上去

  screen.blit(mouse_cursor, (x, y))

 

  \# 刷新画面

  pygame.display.update()

 

这段代码中用到了两张图片，图片可以从网上找，让后用ps简单修改一下就行。（sea.jpg是背景，fish.png是黄色小鱼，fish.png是我用ps抠出来的，背景是透明的）

 

下面稍微解释一下比较重要的部分：

 

set_mode会返回一个Surface对象，代表了在桌面上出现的那个窗口，三个参数第一个为元祖，代表分辨率（必须）；第二个是一个标志位，具体意思见下表，如果不用什么特性，就指定0；第三个为色深。

 

标识位功能

FULLSCREEN	创建一个全屏窗口

DOUBLEBUF	创建一个“双缓冲“窗口，建议在HWSURFACE或OPENGL时使用

HWSURFACE	创建一个硬件加速窗口，必须和FULLSCREEN同时使用

OPENGL		创建一个OPENGL渲染的窗口

RESIZABLE	创建一个可以改变大小的窗口

NOFRAME	创建一个没有边框的窗口

convert函数是将图像数据都转化为Surface对象，每次加载完图像以后就应该做这件事件（事实上因为 它太常用了，如果你不写pygame也会帮你做）；convert_alpha相比convert，保留了Alpha 通道信息（可以简单理解为透明的部分），这样我们的光标才可以是不规则的形状。

 

游戏的主循环是一个无限循环，直到用户跳出。在这个主循环里做的事情就是不停地画背景和更新光标位置，虽然背景是不动的，我们还是需要每次都画它， 否则鼠标覆盖过的位置就不能恢复正常了。

 

blit是个重要函数，第一个参数为一个Surface对象，第二个为左上角位置。画完以后一定记得用update更新一下，否则画面一片漆黑。

 

这就是一个pygame程序的大致流程，接下来我们会学习更多深层次的东西，并且把各条语句都真正的读懂。

 

Python之pygame，从入门到精通（二）

 

上次我们试着写了一个最简单的Pygame程序并且解释了一个大概的框架，这次就Pygame中也是游戏中最关键的事件来展开。

 

理解事件

事件是什么，其实从名称来看我们久能想到些什么，而且你所想到的基本就是事件的真正意思了。我们上一个程序，会一直运行下去，知道你关闭窗口而产生一个QUIT事件，Pygame会接受用户的各种操作（比如按键盘，移动鼠标等）产生事件。事件随时可能发生，而且量也可能会很大，Pygame的做法是把一系列的事件存放一个队列里，逐个的处理。

 

事件检索

上个程序中，使用了pygame.event.get()来处理所有的事件，这好像打开大门让所有的人进入。如果我们使用pygame.event.wait()，Pygame就会等到发生一个事件才继续下去，就好像有哨兵把守的门一样，来一个进一个…一般游戏中不太实用，因为游戏往往是需要动态运作的；而另一个方法pygame.event.poll()就好一些，一旦调用，它会根据现在的情形返回一个真实的事件，或者一个“什么都没有”。下表是一个常用事件集：

 

事件					产生途径					参数

QUIT				用户按下关闭按钮				none

ATIVEEVENT			Pygame被激活或者隐藏			gain, state

KEYDOWN				键盘被按下				unicode(编码), key(名称), mod()

KEYUP					键盘被放开					key, mod

MOUSEMOTION			鼠标移动				pos, rel, buttons

MOUSEBUTTONDOWN		鼠标按下					pos, button

MOUSEBUTTONUP			鼠标放开					pos, button

JOYAXISMOTION		游戏手柄（Joystick or pad）移动	joy, axis, value

JOYBALLMOTION		游戏球（Joy ball）移动			joy, axis, value

JOYHATMOTION		游戏手柄（Joystick）移动		joy, axis, value

JOYBUTTONDOWN			游戏手柄按下				joy, button

JOYBUTTONUP			游戏手柄放开				joy, button

VIDEORESIZE	Pygame		窗口缩放					size, w, h

VIDEOEXPOSE	Pygame	窗口部分公开（expose）			none

USEREVENT			触发了一个用户事件				code

下面我们写一个把所有方法输出的一段代码，它的结果是这样的：

 

我们这里使用了wait()，因为这个程序在有事件发生的时候动弹就可以了。还用了font模块来显示文字，下面是源代码：

 

import pygame

from pygame.locals import *

from sys import exit

from random import randint

 

SCREEN_SIZE = (640, 480)

 

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

 

font = pygame.font.SysFont("arial", 16)

font_height = font.get_linesize()

event_text = []

 

while True:

  event = pygame.event.wait()

  event_text.append(str(event))

 

  event_text = event_text[-SCREEN_SIZE[1]/font_height:]

 

  if event.type == QUIT:

​    exit()

 

  screen.fill((255, 255, 255))

 

  y = SCREEN_SIZE[1]-font_height

 

  for text in event_text:

​    screen.blit(font.render(text, True, (randint(0, 255), randint(0, 255), randint(0, 255))), (0, y))

​    y -= font_height

 

  pygame.display.update()

处理鼠标事件

MOUSEMOTION事件会在鼠标动作时发生，它有三个参数：

 

buttons：一个含有三个数字的元组，三个值分别代表左键、中键和右键，1就是按下了。

pos：鼠标光标的位置

rel：代表了现在距离上次产生鼠标事件时的距离

和MOUSEMOTION类似的，我们还有MOUSEBUTTONDOWN和MOUSEBUTTONUP两个事件，看名字就知道什么意思了。很多时候，你只需要知道鼠标点下就可以了，那就可以不用上面那个比较强大（也比较复杂）的事件了。它们的参数为：

 

button：看清楚了少了个s，这个值代表了哪个按键被操作

pos：鼠标光标的位置

处理键盘事件

键盘和游戏手柄的事件比较类似，为KEYDOWN和KEYUP，下面有一个例子来演示使用方向键移动一些东西。

 

\# _*_coding:utf-8_*_

 

import pygame

from pygame.locals import *

from sys import exit

 

background_image_file = 'sea.jpg'

 

pygame.init()

pygame.display.set_caption('move')

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_file).convert()

 

x, y = 0, 0

move_x, move_y = 0, 0

 

while True:

  for event in pygame.event.get():

​    if event.type == QUIT:

​      exit()

​    if event.type == KEYDOWN:

​      if event.key == K_LEFT:

​        move_x = -1

​      elif event.key == K_RIGHT:

​        move_x = 1

​      elif event.key == K_UP:

​        move_y = -1

​      elif event.key == K_DOWN:

​        move_y = 1

​    elif event.type == KEYUP:

​      move_x = 0

​      move_y = 0

 

​      \# 计算出新的坐标

  x += move_x

  y += move_y

 

  screen.fill((0, 0, 0))

  screen.blit(background, (x, y))

  \# 在新的位置上画图

  pygame.display.update()

KEYDOWN和KEYUP的参数秒速如下：

 

key -按下或者放开的键值，是一个数字，估计地球上很少有人可以记住，所以Pygame中你可以使用K_xxx来表示，比如字母a就是K_a，还有K_SPACE和K_RETURN等。

mod -包含了组合键信息，如果mod & KMOD_CTRL是真值，表示用户同时按下了Ctrl键。类似的还有KMOD_SHIFT，KMOD_ALT。

unicode -代表了按下键的Unicode值，这个自行google。

事件过滤

并不是所有的事件都需要处理的，就好像不是所有登门造访的人都是我们欢迎的一样。比如，俄罗斯方块就无视你的鼠标，而在游戏场景切换的时候，你按什么都是徒劳的。我们应该有一个方法来过滤掉一些我们不感兴趣的事件（当然我们可以不处理这些没兴趣的事件，但最好的方法还是让它们根本不进入我们的事件队列），我们使用pygame.event.set_blocked(事件名)来完成。如果有好多事件需要过滤，可以传递一个列表，比如pygame.event.set_blocked([KEYDOWN, KEYUP]),如果你设置参数None，那么所有的事件都被打开了。与之相对的，我们使用pygame.event,set_allowed()来设定允许的事件。

 

产生事件

通常玩家做什么，Pygame就产生对应的事件就可以了，不过有的时候我们需要模拟出一些事件来，不如录像回放的时候，我们就要把用户的操作再现一遍。

 

为了产生事件，必须先造一个出来，然后再传递它：

 

 

Python之pygame，从入门到精通（三）

 

首先，没有人可以否定好的画面是一款游戏吸引人最直接最诱人得因素（网易游戏的美工是真的好!!），虽说滥画面高游戏度的作品也有，但优秀的画面无疑是一张过硬的通行证，可以让你争取到更多得机会。

 

其实上两回也已经打开过显示了，不过没有特别说明而已，pygame.display.set_mode()就是创建一个游戏窗口，也就是显示的意思。

 

全屏显示

我们再第一个程序里使用了如下的语句

 

screen = pygame.display.set_mode((640, 480), 0, 32)

1

也讲诉了各个参数的意思，当我们把第二个参数设置为FULLSCREEN时，就能得到一个全屏窗口了。

 

screen = pygame.display.set_mode((640, 480), FULLSCREEN ,32)

1

注意：如果你的程序有什么问题，很可能进入全屏模式就不太容易退出来了，所以最好先用窗口模式调试好，再改为全屏模式。

 

在全屏模式下，显卡可能就切换了一种模式，你可以用如下代码获取你的机器支持的显示模式：

 

import pygame

pygame.init()

pygame.display.list_modes()

1

2

3

看下一个实例：

 

\# _*_coding:utf-8_*_

 

import pygame

from pygame.locals import *

from sys import exit

 

 

pygame.init()

pygame.display.set_caption('window-size')

 

background_image = 'yys1.jpg'

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image).convert()

 

fullscreen = False

 

while True:

 

  for event in pygame.event.get():

​    if event.type == QUIT:

​      exit()

  if event.type == KEYDOWN:

​    if event.key == K_F1:

​      fullscreen = not fullscreen

​      if fullscreen:

​        screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)

​      else:

​        screen = pygame.display.set_mode((640, 480), 0, 32)

 

  screen.blit(background, (0, 0))

  pygame.display.update()

运行这个程序，默认还是窗口模式，但按下F1，显示模式就会在窗口和全屏之间切换。

 

可变尺寸显示

虽然一般的程序窗口都能拖边框来改变大小，pygame的默认显示窗口是不行的，而事实上，很多游戏确实不能改变显示窗口的大小，我们可以使用一个参数来改变这个默认行为。

 

\# _*_coding:utf-8_*_

 

import pygame

from pygame.locals import *

from sys import exit

 

 

SCREEN_SIZE = (640, 480)

 

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)

 

background_image = 'yys1.jpg'

background = pygame.image.load(background_image).convert()

 

while True:

  event = pygame.event.wait()

  if event.type == QUIT:

​    exit()

 

  if event.type == VIDEORESIZE:

​    SCREEN_SIZE = event.size

​    screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)

​    pygame.display.set_caption("Window resize to" + str(event.size))

 

  screen_width, screen_height = SCREEN_SIZE

  for y in range(0, screen_height, background.get_height()):

​    for x in range(0, screen_width, background.get_width()):

​      screen.blit(background, (x, y))

 

  pygame.display.update()

当你更改大小的时候，后端控制台会显出最新的尺寸，这里我们学习到一个新事件VIDEORESIZE，它包含如下内容：

 

size：一个二维元组，值为更改后的窗口尺寸，size[0]为宽，size[1]为高

w：宽

h：高

其它、复合模式

我们还有一些其他的显示模式，但未必所有的操作系统都支持（window、各种比较流行的Linux发行办都是没有问题的），一般来说窗口就用0，全屏就用FULLSCREEN，这两个时没有问题的。

 

如果你想创建一个硬件显示（surface会存放在显存里，从而有着更高的速度），但必须和全屏一起用：

 

screen  = pygame.display.set_mode(SCREEN, HWSURFACE | FULLSCREEN, 32)

当然你完全可以把双缓冲（更快）DOUBLEBUF也加上，这就是一个很nice的游戏显示了，不过记得你要使用pygame.display.flip()来刷新显示。pygame.display.update()是将数据画到前面显示，而这个是交替显示的意思。

 

还有OPENGL模式，这是一个得到广泛应用的3D加速显示模式。不过一旦使用了这个模式，pygame中的2D图像函数就不能使用了，我们会在以后讲详细的内容。

————————————————

 