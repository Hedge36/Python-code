import turtle
turtle.setup(700,700)
turtle.pensize(10)
turtle.speed(0)
in_radius = 270
up = turtle.penup
down = turtle.pendown


def tri():
    turtle.left(120)
    turtle.forward(in_radius*3**0.5)
    turtle.right(120)
    turtle.forward(in_radius*3**0.5)
    turtle.right(120)
    turtle.forward(in_radius*3**0.5)


def reveal():
    up()
    turtle.pencolor('pink')
    turtle.goto(0, -300)
    down()
    turtle.circle(300)
    up()
    turtle.goto(0, -in_radius)
    down()
    turtle.circle(in_radius)
    turtle.pencolor('blue')
    tri()
    up()
    turtle.goto(0, in_radius)
    down()
    turtle.right(60)
    tri()

for i in range(10):
    reveal()
    turtle.clear()
    up()
    turtle.home()
    down()
    in_radius+=5
turtle.pencolor("cyan")
turtle.write("Send a flower!", font = ('Simet',32))
turtle.done()

'''
如何做出动态特效？
绘制速度太慢了
'''
