from tkinter import *
import time

root = Tk()
root.title("滚动字幕")
root.geometry("320x240+100+100")
show_str = StringVar(root)
show_str.set("突")
source_str = "突破自己,努力加油!好好学习，天天向上!"
stopflag = True

pos = 0


def marquee(widget):
    textwidth = 10
    strlen = len(source_str)
    global pos

    if strlen - pos < 10:
        show_str.set(source_str[pos:pos+textwidth] +
                     source_str[0:10 - strlen + pos])
    else:
        show_str.set(source_str[pos:pos+textwidth])
    pos += 1

    if pos > strlen:
        pos = 0

    global stopflag

    if stopflag:
        widget.after(300, marquee, widget)


show_lb = Label(root, textvariable=show_str)

show_lb.place(x=20, y=20, width=200, height=30)


def startmarque():
    global stopflag
    stopflag = True
    marquee(show_lb)


def stopmarquee():
    global stopflag
    stopflag = False


button1 = Button(root, text="start", command=startmarque)
button2 = Button(root, text="stop", command=stopmarquee)
button1.place(x=20, y=100, width=50, height=30)
button2.place(x=200, y=100, width=50, height=30)
root.mainloop()
