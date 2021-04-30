#爱心绘制
from turtle import *
speed(0)
Turtle().screen.delay(0)
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
done()
