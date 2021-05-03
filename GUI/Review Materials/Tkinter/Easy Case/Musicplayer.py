# coding：utf-8
from mutagen.mp3 import MP3
import random
import tkinter.messagebox
import tkinter.scrolledtext
from PIL import ImageTk, Image
import time
import threading
from threading import *
import os
import pygame
import tkinter.filedialog
from tkinter import *
import tkinter as tk
import requests
import json
import urllib.request

headers = {'Host': 'music.bbbbbb.me',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0',
           'Accept': 'application/json, text/javascript, */*; q=0.01',
           'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
           'Accept-Encoding': 'gzip, deflate',
           'Referer': 'http://music.bbbbbb.me/',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'X-Requested-With': 'XMLHttpRequest',
           'Content-Length': '47',
           'Connection': 'keep-alive',
           'Pragma': 'no-cache',
           'Cache-Control': 'no-cache'}


def search_Music(mname):
    global headers
    data = {'input': mname, 'filter': 'name', 'type': 'netease', 'page': '1'}
    url = 'http://music.bbbbbb.me/'
    wbdata = requests.post(url, headers=headers, data=data).text
    data = json.loads(wbdata)
    return data


def ShowList(data):
    i = 1
    for n in data['data']:
        author = n['author']
        url = n['url']
        print("编号:", i, "歌手:", author, "下载地址:", url)
        i = i+1


def DownLoad(data, mname, Number):
    try:
        url = data['data'][Number-1]['url']
        singer = data['data'][Number-1]['author']

        base = "G:/3.Google网页下载文件存放处/音乐/歌曲/周杰伦/"
        MusicName = singer+" - "+mname+".mp3"

        filepath = base+MusicName
        urllib.request.urlretrieve(url, filepath)

        # 添加新歌
        global SongName
        SongName.append(MusicName)
        SongPath.append(filepath)

        filepath
        print("下载完成")
        return True
    except:
        print("下载失败")
        return False


# ---------------------------------------------------------------------------------------------

# ----------------------一、音乐文本读取--------------------
filePath = 'D:\\Personal\\music\\Favorite\\'
SongName = os.listdir(filePath)
SongPath = [filePath+i for i in SongName]

Number = 0
volume = 0.3

Switch = True

# ----------------------二、功能区--------------------------------------

# --------------------------1.基本的功能----------------------------

# 1.上一曲


def fun1():
    if model_value % 3 == 2:
        random_play()
    else:
        global Number
        Number = Number+1
        if Number > len(SongPath)-1:
            Number = 0
        pygame.mixer.music.load(SongPath[Number])
        pygame.mixer.music.play(0)

    entry_var.set(SongName[Number])
    pass

# 2.播放/暂停


def fun2():
    global Number
    global Switch
    pygame.mixer.music.set_volume(volume)
    if Switch == True:
        pygame.mixer.music.pause()
        condition.set("播放")
        Switch = False
    else:
        pygame.mixer.music.unpause()
        condition.set("暂停")
        Switch = True
    pass


# 3.下一曲
def fun3():
    if model_value % 3 == 2:
        random_play()
    else:
        global Number
        Number = Number-1
        if Number < 0:
            Number = len(SongPath)-1
        pygame.mixer.music.load(SongPath[Number])

        pygame.mixer.music.play(0)

        entry_var.set(SongName[Number])
        pass


# 4.增大音量
def fun4():
    global volume
    volume += 0.1
    if volume > 1:
        volume = 1
    pygame.mixer.music.set_volume(volume)


# 5.降低音量
def fun5():
    global volume
    volume -= 0.1
    if volume < 0:
        volume = 0
    pygame.mixer.music.set_volume(volume)


# ----------------------------------2.下载功能--------------------------------------

# 1.搜索
def Search():
    txtCon.delete(0.0, tk.END)
    mname = en3.get()
    if mname != "":
        data = search_Music(mname)
        i = 1
        for n in data['data']:
            author = n['author']
            content = "编号:"+str(i)+"歌手:"+author+"\n"
            txtCon.insert(tkinter.INSERT, content)
            i = i+1

# 2.下载


def DownLoad_music():
    mname = en3.get()
    Number = int(en4.get())
    data = search_Music(mname)
    ShowList(data)
    boolean = DownLoad(data, mname, Number)

    if boolean == True:  # 2.验证
        tk.messagebox.showinfo(message="下载成功")  # 弹出提示框
    else:
        tk.messagebox.showerror(message="下载失败")  # 弹出错误框


# ---------------------------3.播放模式---------------------------------


# ---------------一.界面变化------------
def play_model_set():
    global model_value
    model_value = model_value+1

    if model_value % 3 == 0:
        model.set("顺序")
    elif model_value % 3 == 1:
        model.set("单曲")
    elif model_value % 3 == 2:
        model.set("随机")


# --------------二、功能变换----------------


# ---------1.播放模式-----------------------
def sequential_play():
    global Number
    Number = Number+1
    if Number > len(SongPath)-1:
        Number = 0
    pygame.mixer.music.load(SongPath[Number])
    entry_var.set(SongName[Number])
    pygame.mixer.music.play(0)
    pass


def cycle_play():
    global Number
    pygame.mixer.music.load(SongPath[Number])
    entry_var.set(SongName[Number])

    pygame.mixer.music.play(0)
    pass


def random_play():
    global Number
    Number = random.randint(0, len(SongPath)-1)
    pygame.mixer.music.load(SongPath[Number])
    entry_var.set(SongName[Number])

    pygame.mixer.music.play(0)
    pass


# -----------2.模式切换------------------
def play_model():
    global model_value
    if model_value % 3 == 0:
        sequential_play()
    elif model_value % 3 == 1:
        cycle_play()
    elif model_value % 3 == 2:
        random_play()


# ----------3.播放类------------------------------------
class Play_Model(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        pass

    def run(self):
        while 1:
            state = pygame.mixer.music.get_busy()
            if state == 0:
                play_model()
            time.sleep(1)


# ------------------------三、计时器的制作--------------------------


def os(time):
    if time < 10:
        return "0"+str(time)
    else:
        return str(time)


def clock(seconds):
    if seconds >= 60:
        minutes = seconds//60
        seconds = seconds-minutes*60
        return os(minutes)+":"+os(seconds)
    else:
        return "00:"+os(seconds)
# --------------------------------------------------------


# --------------------------3，音乐播放滑条--------------------------------------------------

set_time = 0
Inter_executeCount = 0
Outer_executeCount = 0


class Music_PlaySlide(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        pass

    def run(self):
        global Inter_executeCount
        global Outer_executeCount
        global set_time
        global Get_time

        LastChange_time = 0
        audio = MP3(SongPath[Number])
        Song_length = audio.info.length//1
        while 1:

            Get_time = pygame.mixer.music.get_pos()//1000

            if Inter_executeCount != Outer_executeCount:
                LastChange_time = Get_time
                Inter_executeCount = Outer_executeCount

            if Get_time == 0:
                audio = MP3(SongPath[Number])
                Song_length = audio.info.length//1
                LastChange_time = 0
                set_time = 0
            print("当前时间", Get_time)
            Current_time1 = Get_time+set_time-LastChange_time

            seconds = int(Current_time1)
            current_time = clock(seconds)
            entry_var1.set(current_time)
            print("获取时间", Current_time1)

            rate = (Current_time1/Song_length)
            Current_option = 100*rate
            value.set(str(Current_option))
            time.sleep(1)


# -----------------------三、面板区-----------------------------------------


# ---------------一、窗口---------------------
root = tk.Tk()
root.title('音乐播放器')
# root["height"]=400
# root["width"]=300

root.geometry('300x400')
root.resizable(0, 0)

# 1.文本框
lal = tk.Label(root, text="欢迎使用音乐播放器")  # 在root中创建标签
lal.place(x=50, y=15, width=200, height=50)  # 向root放置标签


# ---------------二、显示正在播放的歌曲--------------------------

entry_var = tk.StringVar()
entry_var.set(SongName[Number])
en1 = tk.Entry(root, textvariable=entry_var, justify=CENTER, state=NORMAL)
en1.place(x=50, y=70, width=200, height=15)

entry_var1 = tk.StringVar()
entry_var1.set('00:00')
en2 = tk.Entry(root, textvariable=entry_var1, justify=CENTER)
en2.place(x=5, y=30, width=80, height=15)


# ---------------三、音量调节----------------------------

b3 = tk.Button(root, text="+", command=fun4)
b3.place(x=50, y=90)

b3 = tk.Button(root, text="-", command=fun5)
b3.place(x=65, y=90)


# ---------------四、切换歌曲|暂停播放----------------------------------
# 1.上一曲按钮
b1 = tk.Button(root, text="上一曲", command=fun1)
b1.place(x=80, y=90)


# 2.播放按钮
condition = tk.StringVar()
condition.set("暂停")

b1 = tk.Button(root, textvariable=condition, command=fun2)  # 定义：按钮名称+按钮功能
b1.place(x=130, y=90)  # 定义：按钮大小+按钮位置


# 3.下一曲按钮
b3 = tk.Button(root, text="下一曲", command=fun3)
b3.place(x=167, y=90)


# 4.播放模式
model = tk.StringVar()
model.set("顺序")
model_value = 0
b4 = tk.Button(root, textvariable=model, command=play_model_set)
b4.place(x=215, y=90)


# --------------五、下载功能------------------------------


# 1.搜索
en3 = tk.Entry(root, justify=CENTER, state=NORMAL)
en3.place(x=50, y=150, width=80, height=30)

b1 = tk.Button(root, text="搜索", command=Search)
b1.place(x=135, y=150)

# ---------------------------------------------------------

# 2.下载
en4 = tk.Entry(root, justify=CENTER, state=NORMAL)
en4.place(x=180, y=150, width=30, height=30)

b1 = tk.Button(root, text="下载", command=DownLoad_music)
b1.place(x=220, y=150)
# -------------------------------------------------


def slide(text):  # 注意，Scale的回调函数需要给定形参，当触发时会将Scale的值传给函数
    global set_time
    global Outer_executeCount
    audio = MP3(SongPath[Number])
    Song_length = audio.info.length//1

    Get_Length = int(float(value.get()))
    rate = Get_Length/100

    set_time = Song_length*rate
    pygame.mixer.music.rewind()
    pygame.mixer.music.set_pos(set_time)

    Outer_executeCount += 1

    print("当前时间", pygame.mixer.music.get_pos()//1000)


value = StringVar()
value.set("0")
Scale(root, from_=0, to=100, orient=HORIZONTAL, length=600, show=0,
      variable=value, resolution=0.01, command=slide).pack()


# ----------------------------------------------------------------

txtCon = tk.scrolledtext.ScrolledText(root, wrap=tk.WORD)
# txtCon.pack(fill=tk.BOTH)
txtCon.place(x=50, y=200, width=210, height=150)

pygame.mixer.init()

pygame.mixer.music.load(SongPath[Number])
pygame.mixer.music.play(0)
play_model()


t1 = Play_Model()
t1.start()


t2 = Music_PlaySlide()
t2.start()


root.mainloop()
pygame.mixer.music.stop()
