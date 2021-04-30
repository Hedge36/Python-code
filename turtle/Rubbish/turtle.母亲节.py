#爱心绘制
from turtle import *
speed(0)
Turtle().screen.delay(0)
#控制刻画速度
hideturtle()
#抑或ht()
def curvemove():
    for i in range(200):
        right(1)
        forward(1)
color('red','pink')
begin_fill()
left(140)
forward(111.65)
curvemove()
left(120)
curvemove()
forward(111.65)
end_fill()
penup()
goto(-65,200)
delay(200)
printer = Turtle()
write("5.10",font=("楷体", 50,"normal"))
penup()
goto(-150,-100)
delay(200)
printer = Turtle()
write("母亲节快乐",font=("楷体", 50,"normal"))
done()

