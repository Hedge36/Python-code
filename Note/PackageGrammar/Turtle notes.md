# Turtle库基础语法

注：仅收录部分常用的函数

## 1. 绘图窗体函数

turtle.setup(width,height,startx,starty)

​								设置窗体大小及位置，并且setup函数及其后两个参数不是必须的，若不设置则默认窗体在屏幕正中间，其中width表示窗体宽度，height表示窗体高度，startx表示窗口左上角离屏幕左上角的距离，starty表示离屏幕左上角的高度。

bgcolor()							设置或者返回当前的TurtleScreen的背景颜色。

bgpic(path)						设置背景图片，path为图片的路径，且图片格式必须为gif。

reset()							重置，将屏幕中的图纸删除，重新居中并将所有变量设置为默认值。

clear()							删除图纸。对属性不做操作

 

## 2. 画笔控制函数

turtle.penup()或者turtle.pu()    将海龟画笔抬起，此时海龟不在画布上形成图案；

turtle.pendown()或者turtle.pd()  让海龟画笔落下，但是落笔不会形成图案。

turtle.pensize(width)或者turtle.width(width)

设置画笔宽度，相当于海龟腰围，设置以后一直有	效，直至下次重新设置。

turtle.pencolor(color)

其中color为颜色字符串或者r,g,b值（如color(1,1,1)或者color（（1，1，1）））。

  RGB色彩模式：

  GRB色彩取整数值（0，255）或者取小数值（0，1）

  相关函数：

turtle.colormode(1.0/255)修改色彩取值

turtle.pencolor(color)

 白色：255，255，255      white

  黄色：255，255，0      	yellow

  洋红：255，0，255       magenta

  青色：0，255，255       	cyan

蓝色： 0， 0，255       blue

  黑色：0，0，0         	black

  海贝色：255，245，238     	seashell

  金色：255,215,0        	gold

  粉红色：255,192,203     		pink

  棕色：165,42,42        	brown

紫色：160,32,240       	purple   

  番茄色：255,99,71        tomato

![img](file:///C:\Users\Hedge\AppData\Local\Temp\ksohtml12988\wps1.jpg) 

color():						同时设置pencolor和fillcolor，有先后顺序

goto(x,y)或者steps()或者setposition()

行进函数，让任何位置的海龟前往指定坐标。

turtle.circle(r[,rangle])			以海龟左侧距离为r（负值则在右）的点（默认点）为								圆心逆时针行进。（默认360°）

turtle.bk(d)					其中bk表示向海龟当前的反方向运行，d表示行进距								离且可以为负值；

turtle.fd(d)					其中fd表示向海龟当前方向运行，d表示行进距离  turtle.home					让海龟回到原点

turtle.seth(angle)				改变海龟的行进方向而不发生行进，负度数表示逆时针旋转

turtle.left(angle)				使海龟向右转，只改变方向而不行进

turtle.right(angle)				使海龟向右转，只改变方向而不行进

speed(0-10)					速度指令，其中，0直接成图，6为正常速度，1最慢，10最快,大于10即为0。

hideturtle()/showturtle()		隐藏或者显示乌龟

shape()						设置乌龟的图形形状，取值:“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”，自定义形状需要通过其他库的辅助，可上网查找。

isdown()						如果笔停止返回True，反之False

filling()						返回fillstate状态，如果填充则返回True，反之False。

begin_fill()					在填充前调用

end_fill()						填充结束

isvisible()						乌龟是否可见。如果可见返回True，反之则False。

tiltangle()						设置或者返回当前的倾斜角度。

shapetransform()				设置或返回乌龟的形状的当前转换矩阵。

clone()						创建并返回具有相同位置等等属性的乌龟克隆。

getturtle() | getpen()			获取trutle对象本身。

getscreen()					返回正在绘制的对象。

 

## 3. 事件函数

onclick()						鼠标点击事件。参数：fun-一个带有两个参数的函数，这些	参数将与画布上单击点的坐标一个调用。num-鼠标按钮的数量，默认为1(左键)。add- True的时候将添加新的绑定。否则替换以前的绑定。

onrelease()					鼠标释放事件。参数同点击事件。

ondrag()						鼠标移动事件。参数同点击事件。

begin_poly()					开始记录多边形的顶点。

end_poly()					停止记录多边形的顶点。

get_poly()					返回最后记录的多边形。

setundobuffer()				设置或禁用中断器。参数： size-整数。如果大小是None，							则禁用缓冲区。

delay()						设置或返回以毫秒为单位的绘制延迟，延迟越大，绘图越慢。

ontimer()						定时器。

mainloop() | done() 			开始循环 。

textinput() | numinput()			弹出一个输入字符串和数字的窗口。

 

## 4. 坐标函数

xcor()						返回x坐标

ycor()						返回y坐标

heading()						返回当前的方向值。

distance()						返回x，y两个点的直线距离

degrees()						设置一整圈的度数,默认是360度。

radians()						将角度测量单位设置为弧度,相当于 degrees(2*math.pi)

get_shapepoly()				返回当前形状的坐标。

 

 

## 5.文本输入函数

printer = Turtle()

write("str",font=("font", size(数字),"normal"))

文本输入

 关闭绘图轨迹与更新画布

```python
turtle.tracer(False)
turtle.update()
```

**D:\tools\Python\Lib\turtledemo**

