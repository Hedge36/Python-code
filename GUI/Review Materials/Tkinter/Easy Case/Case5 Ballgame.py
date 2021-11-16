import random
import tkinter as tk
import time


class Ball:
    def __init__(self, canvas, color, winW, winH, racket):
        self.canvas = canvas
        self.racker = racket
        self.id = canvas.create_oval(0, 0, 20, 20, fill=color)
        self.canvas.move(self.id, winW/2, winH/2)   # 将小球移动至正中间
        startpos = list(range(-4, 5))
        random.shuffle(startpos)
        self.x, self.y = startpos[0], -step  # 小球运动速度
        self.nottouch = 1

    def hitracket(self, ballpos):
        racketpos = self.canvas.coords(self.racker.id)
        if ballpos[2] >= racketpos[0] and ballpos[0] <= racketpos[2]:
            if ballpos[3] >= racketpos[1] and ballpos[3] <= racketpos[3]:
                return 1
        return 0

    def ballMove(self):
        self.canvas.move(self.id, self.x, self.y)
        ballpos = self.canvas.coords(self.id)
        if ballpos[0] <= 0:
            self.x = step
        if ballpos[1] <= 0:
            self.y = step
        if ballpos[2] >= winH:
            self.x = -step
        if ballpos[3] >= winW:
            self.y = -step
        if self.hitracket(ballpos) == 1:
            self.y = -step
        if ballpos[3] >= winH:
            self.nottouch = 0


class Racket:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 15, fill=color)
        self.canvas.move(self.id, 270, 400)
        self.x = 0
        self.canvas.bind_all("<KeyPress-Right>", self.moveRight)
        self.canvas.bind_all("<KeyPress-Left>", self.moveLeft)

    def racketMove(self):
        self.canvas.move(self.id, self.x, 0)
        racketpos = self.canvas.coords(self.id)
        if racketpos[0] <= 0:
            self.x = 0
        elif racketpos[2] >= winW:
            self.x = 0

    def moveLeft(self, event):
        self.x = -3

    def moveRight(self, event):
        self.x = 3


winW = 640
winH = 480
step = 3
speed = 0.01

root = tk.Tk()
root.title("Bouncing Ball")
root.wm_attributes("-topmost", 1)
canvas = tk.Canvas(root, width=winW, height=winH)
canvas.pack()
root.update()

racket = Racket(canvas, "purple")
ball = Ball(canvas, "yellow", winW, winH, racket)

while ball.nottouch:
    try:
        ball.ballMove()
    except:
        print("单击关闭按钮结束程序")
        break
    racket.racketMove()
    root.update()
    time.sleep(speed)
