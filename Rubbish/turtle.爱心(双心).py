import turtle
turtle.speed(0)
turtle.Turtle().screen.delay(0)


def curvemove():  # 定义函数画圆,200度
    for i in range(100):
        turtle.right(2)
        turtle.forward(2)
        turtle.speed(10)


turtle.color('red', ('#F05B72'))  # 设置画笔及填充颜色
turtle.pensize(3)
turtle.hideturtle()  # 隐藏画笔形状
turtle.speed(5)
turtle.begin_fill()  # 开始填充
# 第一个爱心
turtle.left(140)
turtle.forward(111.65)
curvemove()
turtle.left(120)
curvemove()
turtle.forward(111.65)
turtle.end_fill()
# 第二个爱心
turtle.color(('#F05B72'), 'red')
turtle.begin_fill()
turtle.penup()
turtle.goto(60, 0)
turtle.pendown()
turtle.right(80)
turtle.forward(111.65)
curvemove()
turtle.left(120)
curvemove()
turtle.forward(111.65)
turtle.end_fill()
# 箭头
turtle.color('red', 'red')
turtle.begin_fill()
turtle.hideturtle()
turtle.penup()
turtle.goto(-150, 20)
turtle.pendown()
turtle.pensize(5)
turtle.right(20)
turtle.right(60)
turtle.forward(15)
turtle.right(120)
turtle.forward(40)
turtle.right(60)
turtle.forward(14)
turtle.left(60)
turtle.forward(375)
turtle.left(90)
turtle.forward(10)
turtle.right(110)
turtle.forward(30)
turtle.right(140)
turtle.forward(30)
turtle.right(110)
turtle.forward(10)
turtle.left(90)
turtle.forward(375)
turtle.left(60)
turtle.forward(14)
turtle.right(60)
turtle.forward(40)
turtle.right(120)
turtle.forward(15)
turtle.end_fill()

turtle.penup()
turtle.goto(10.5, 85)
turtle.color("violet")
turtle.write("L O V E", font=('Dutch801 XBd BT', 20, 'normal'))

turtle.done()
