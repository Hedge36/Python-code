from tkinter import *
from tkinter.colorchooser import *
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)    # super()代表的是父类的定义，而不是父类对象
        self.master = master
        # 实例窗口属性
        self.draw = 0
        self.lastdraw = 0
        self.x, self.y = 0, 0
        self.canvasbg = "white"
        self.img = None
        # 线型变量
        self.arrow = StringVar()
        self.linecheck = IntVar()
        self.dashcheck = StringVar()
        self.ld = IntVar()
        # 图形变量
        self.gld = IntVar()
        # 画笔变量
        self.pld = IntVar()
        # 橡皮变量
        self.esize = IntVar()
        # 选项变量
        self.drawcolor = StringVar()
        self.oxflash = StringVar()  # 颜色缓冲值
        # 窗口初始化
        self.pack()
        self.createWidget(master)

    def createContextMenu(self, event):
        """右键菜单栏，正在设计中。"""
        self.rightmenu.post(event.x_root, event.y_root)

    def createWidget(self, master):
        """组件初始化"""
        # 关于画图，完全可以使用matplotlib来实现
        self.drawbox = Canvas(root, width=598, height=498, bg=self.canvasbg,
                              bd=1, relief="solid")
        self.drawbox.place(x=10, y=20)

        # 右键菜单栏
        self.drawbox.bind("<Button-3>", self.createContextMenu)

        # 功能区
        self.funcbox = Frame(width=270, height=500)
        self.funcbox.place(x=620, y=22)
        # 操作栏
        self.operatebox = Frame(self.funcbox, width=269, height=25)
        self.operatebox.place(x=0, y=0)
        # 详情栏
        self.detailbox = LabelFrame(self.funcbox, width=269, height=470)
        self.detailbox.place(x=0, y=30)

        # 操作标签
        self.bt_line = Label(self.operatebox, text="直线", name="line",
                             bd=1, relief="raised")
        self.bt_line.place(x=0, relwidth=0.2, relheight=1)
        self.bt_graph = Label(self.operatebox, text="图形", name="graph",
                              bd=1, relief="raised")
        self.bt_graph.place(relx=0.2*1, relwidth=0.2, relheight=1)
        self.bt_pen = Label(self.operatebox, text="画笔", name="pen",
                            bd=1, relief="raised")
        self.bt_pen.place(relx=0.2*2, relwidth=0.2, relheight=1)
        self.bt_erasor = Label(self.operatebox, text="橡皮", name="erasor",
                               bd=1, relief="raised")
        self.bt_erasor.place(relx=0.2*3, relwidth=0.2, relheight=1)
        self.bt_option = Label(self.operatebox, text="设置", name="option",
                               bd=1, relief="raised")
        self.bt_option.place(relx=0.2*4, relwidth=0.2, relheight=1)

        # 直线详情框
        self.linebox = Frame(self.detailbox, width=269, height=470)
        # 箭头类型
        Label(self.linebox, text="ArrowStyle").place(x=30, y=40)
        self.set_arrow = Combobox(self.linebox, state="readonly",
                                  values=["\\", "<--", "-->", "<->"])
        self.set_arrow.current(0)
        self.set_arrow.place(x=110, y=40, relwidth=0.4)
        # 线型
        Label(self.linebox, text="LineStyle").place(x=30, y=80)
        self.set_style = Combobox(self.linebox, state="readonly",
                                  values=["-", "--"])
        self.set_style.current(0)
        self.set_style.place(x=110, y=80, relwidth=0.4)
        # 模式
        Label(self.linebox, text="PenMode").place(x=30, y=120)
        self.set_mode = Combobox(self.linebox, state="readonly",
                                 values=["Single", "Multiple", "Radial"])
        self.set_mode.current(0)
        self.set_mode.place(x=110, y=120, relwidth=0.4)
        # 线宽
        Label(self.linebox, text="LineWidth").place(x=30, y=160)
        check = self.register(self.numberonly)
        self.set_ld = Entry(self.linebox, highlightcolor="sky blue", highlightthickness=1,
                            textvariable=self.ld,
                            validate="key", validatecommand=(check, '%P'))
        self.set_ld.place(x=110, y=160, relwidth=0.4)
        self.ld.set(1)
        self.ld.trace("w", self.lsketchshow)
        # 预览图
        self.linesketchbox = Frame(
            self.linebox, height=140, bd=1, relief='groove')
        self.linesketchbox.place(y=330, relwidth=1)
        self.linesketch = Canvas(self.linesketchbox, width=98, height=98, bg=self.canvasbg,
                                 bd=1, relief="solid")
        Label(self.linesketchbox, text="效果图").place(x=30, y=60)
        self.linesketch.place(x=110, y=20)
        self.linesketch.create_line(0, 50, 100, 50, width=1)

        # 图形详情栏
        self.graphbox = Frame(self.detailbox, width=269, height=470)
        # 图形类型
        Label(self.graphbox, text="GraphStyle").place(x=30, y=40)
        self.set_gtype = Combobox(self.graphbox, values=["Rectangle", "Oval"],
                                  state="readonly",)
        self.set_gtype.current(0)
        self.set_gtype.place(x=110, y=40, relwidth=0.4)
        # 填充类型
        Label(self.graphbox, text="FillStyle").place(x=30, y=80)
        self.set_fillstyle = Combobox(self.graphbox, state="readonly",
                                      values=["outline", "fill"])
        self.set_fillstyle.current(0)
        self.set_fillstyle.place(x=110, y=80, relwidth=0.4)
        # 颜色
        Label(self.graphbox, text="Color").place(x=30, y=120)
        self.set_gcolor = Combobox(self.graphbox, state="readonly",
                                   values=["red", "blue"])
        self.set_gcolor.current(0)
        self.set_gcolor.place(x=110, y=120, relwidth=0.4)
        # 线宽
        Label(self.graphbox, text="LineWidth").place(x=30, y=160)
        self.set_gld = Entry(self.graphbox, highlightcolor="sky blue",
                             highlightthickness=1, textvariable=self.gld,
                             validate="key", validatecommand=(check, '%P'))
        self.set_gld.place(x=110, y=160, relwidth=0.4)
        self.gld.set(1)
        self.gld.trace("w", self.gsketchshow)
        # 预览图
        self.graphsketchbox = Frame(self.graphbox, height=140, bd=1,
                                    relief='groove')
        self.graphsketchbox.place(y=330, relwidth=1)
        self.graphsketch = Canvas(self.graphsketchbox, width=98, height=98,
                                  bg=self.canvasbg, bd=1, relief="solid")
        Label(self.graphsketchbox, text="效果图").place(x=30, y=60)
        self.graphsketch.place(x=110, y=20)
        self.graphsketch.create_rectangle(12.5, 87.5, 87.5, 12.5, outline="red",
                                          width=1)

        # 画笔区
        self.penbox = Frame(self.detailbox, width=269, height=470)
        Label(self.penbox, text="PenWidth").place(x=30, y=40)
        self.set_pld = Entry(self.penbox, highlightcolor="sky blue",
                             highlightthickness=1, textvariable=self.pld,
                             validate="key", validatecommand=(check, '%P'))
        self.set_pld.place(x=110, y=40, relwidth=0.4)
        self.pld.set(1)

        # 橡皮详情区
        self.erasorbox = Frame(self.detailbox, width=269, height=470)
        # 橡皮类型
        Label(self.erasorbox, text="Erasortype").place(x=30, y=40)
        self.set_etype = Combobox(self.erasorbox, values=["Rectangle", "Oval"],
                                  state="readonly",)
        self.set_etype.current(0)
        self.set_etype.place(x=110, y=40, relwidth=0.4)
        # 橡皮大小
        Label(self.erasorbox, text="ErasorSize").place(x=30, y=80)
        self.esize.set(4)
        self.set_eld = Entry(self.erasorbox, highlightcolor="sky blue",
                             highlightthickness=1, textvariable=self.esize,
                             validate="key", validatecommand=(check, '%P'))
        self.set_eld.place(x=110, y=80, relwidth=0.4)
        self.esize.trace("w", self.esketchshow)
        # 预览图
        self.esketchbox = Frame(self.erasorbox, height=140, bd=1,
                                relief='groove')
        self.esketchbox.place(y=330, relwidth=1)
        self.esketch = Canvas(self.esketchbox, width=98, height=98,
                              bg=self.canvasbg, bd=1, relief="solid")
        Label(self.esketchbox, text="效果图\n(颜色仅供参考)").place(x=30, y=60)
        self.esketch.place(x=120, y=20)
        self.esketch.create_rectangle(46, 46, 54, 54, outline="violet",
                                      width=1)

        # 设置区
        self.optionbox = Frame(self.detailbox, width=269, height=470)
        Label(self.optionbox, text="ColorMode").place(x=30, y=40)
        self.drawcolor.set("#ff0000")
        self.set_colormode = Combobox(self.optionbox, state="readonly",
                                      values=["Ox", "Chooser"])
        self.set_colormode.current(0)
        self.set_colormode.place(x=120, y=40, relwidth=0.4)
        self.oxbox = Frame(self.optionbox, width=269, height=470)
        self.oxbox.place(x=0, y=75)
        Label(self.oxbox, text="Colorname").place(x=30, y=0)
        self.oxcolor = Entry(self.oxbox, highlightcolor="sky blue",
                             textvariable=self.oxflash,
                             highlightthickness=1, width=15)
        self.oxflash.set('#ff0000')
        self.oxcolor.place(x=120, y=0)
        self.oxshow = Label(self.oxbox, bg='red', bd=1, relief='solid')
        self.oxshow.place(x=240, y=0, width=20, height=20)
        self.oxtip = Label(self.oxbox)
        self.oxtip.place(x=30, y=25, relwidth=0.95)
        self.oxflash.trace('w', self.oxsetcolor)
        self.chbox = Frame(self.optionbox, width=269, height=470)
        Label(self.chbox, text="Colorset").place(x=30, y=0)
        self.colorboard = Label(self.chbox)
        self.colorboard['text'] = '#ff0000'
        self.colorboard.place(x=120, y=0)
        Button(self.chbox, text="⚙", command=self.setcolor).place(x=210, y=0)

        # 按钮效果通过边框样式的改变实现->sunken
        self.bt_line.bind("<Button-1>", self.eventmanager)
        self.bt_graph.bind("<Button-1>", self.eventmanager)
        self.bt_pen.bind("<Button-1>", self.eventmanager)
        self.bt_erasor.bind("<Button-1>", self.eventmanager)
        self.bt_option.bind("<Button-1>", self.eventmanager)

        self.set_arrow.bind("<<ComboboxSelected>>", self.lsketchshow)
        self.set_style.bind("<<ComboboxSelected>>", self.lsketchshow)
        self.set_mode.bind("<<ComboboxSelected>>", self.lsketchshow)
        self.set_gtype.bind("<<ComboboxSelected>>", self.gsketchshow)
        self.set_gcolor.bind("<<ComboboxSelected>>", self.gsketchshow)
        self.set_fillstyle.bind("<<ComboboxSelected>>", self.gsketchshow)
        self.set_etype.bind("<<ComboboxSelected>>", self.esketchshow)
        self.set_colormode.bind("<<ComboboxSelected>>", self.colormode)

        # 快捷键设定,此处监听了所有按键
        master.bind("<KeyPress>", self.shortcut)

        # Top Menubar
        menubar = Menu(master)
        filemenu = Menu(menubar, tearoff=0)  # tearoff是否可以拖撰单独显示
        helpmenu = Menu(menubar, tearoff=0)  # tearoff是否可以拖撰单独显示
        operationmenu = Menu(menubar, tearoff=0)  # tearoff是否可以拖撰单独显示

        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Operation", menu=operationmenu)
        menubar.add_cascade(label="Help", menu=helpmenu)
        # 分割线
        filemenu.add_command(
            label="Load", accelerator="Ctrl+O", command=self.loadfig)
        filemenu.add_command(
            label="Save", accelerator="Ctrl+S", command=self.savefig)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=master.quit)

        modemenu = Menu(master, tearoff=0)
        operationmenu.add_command(
            label='Clear', accelerator="Ctrl+C", command=self.clearfig)
        helpmenu.add_command(label="About us")
        master.config(menu=menubar)

        # self.rightmenu
        self.rightmenu = Menu(master, tearoff=0)
        self.rightmenu.add_command(
            label='Clear', accelerator="Ctrl+C", command=self.clearfig)
        self.rightmenu.add_command(label="Load", command=self.loadfig)
        self.rightmenu.add_command(label="Save", command=self.savefig)
        self.rightmenu.add_separator()
        self.rightmenu.add_command(label="Exit", command=master.quit)

        self.rightmenu.add_command(label="About us")

    def eventmanager(self, event):
        """事件管理，包括展示动画效果及响应"""
        name = event.widget.winfo_name()
        self.labelshow(name)
        self.frameshow(name)
        if name == "line":
            self.drawbox.bind("<B1-Motion>", self.drawline)
            self.drawbox.bind("<ButtonRelease-1>", self.stopdraw)
        elif name == "graph":
            self.drawbox.bind("<B1-Motion>", self.drawgraph)
            self.drawbox.bind("<ButtonRelease-1>", self.gstopdraw)
        elif name == "pen":
            self.drawbox.bind("<B1-Motion>", self.drawpen)
        elif name == "erasor":
            self.drawbox.bind("<B1-Motion>", self.drawerasor)
        elif name == "option":
            self.drawbox.bind("<B1-Motion>", self.drawoption)

    # 功能区操作函数区
    def drawline(self, event):
        """按住左键，作为起点与终点，绘制一条直线。"""

        def draw():
            if self.dashcheck.get() == 'True':
                self.lastdraw = self.drawbox.create_line(self.x, self.y, event.x, event.y,
                                                         fill=self.drawcolor.get(), arrow=self.arrow.get(),
                                                         dash=10, width=self.ld.get())
            else:
                self.lastdraw = self.drawbox.create_line(self.x, self.y, event.x, event.y,
                                                         fill=self.drawcolor.get(), arrow=self.arrow.get(),
                                                         width=self.ld.get())
            # arrowshape不会搞，不搞了

        self.linedataflash()
        # 正式绘制
        if self.linecheck.get() != 0:
            self.drawbox.delete(self.lastdraw)
        self.startdraw(event)
        draw()

    def drawgraph(self, event):
        """按住左键，作为起点与终点，绘制一个矩形。"""
        self.gstartdraw(event)
        if self.set_gtype.get() == 'Rectangle':
            cmd = 'self.lastdraw=self.drawbox.create_rectangle(self.x, self.y, event.x, event.y,%s="%s",width=%s)' % (self.set_fillstyle.get(),
                                                                                                                      self.set_gcolor.get(), self.gld.get())
        else:
            cmd = 'self.lastdraw=self.drawbox.create_oval(self.x, self.y,event.x, event.y,%s="%s",width=%s)' % (self.set_fillstyle.get(),
                                                                                                                self.set_gcolor.get(), self.gld.get())
        exec(cmd)

    def drawpen(self, event):
        """画笔，按住左键后，沿鼠标轨迹绘制图形。"""
        self.startdraw(event)
        self.drawbox.create_line(self.x, self.y, event.x, event.y, width=self.pld.get(),
                                 fill=self.drawcolor.get())
        self.x, self.y = event.x, event.y

    def drawerasor(self, event):
        """通过绘制新的实心矩形覆盖原有图形，但这会存在一个问题，换背景颜色就全部显示出来了。"""
        self.startdraw(event)
        size = self.esize.get()
        if self.set_etype.get() == 'Rectangle':
            print(size)
            self.drawbox.create_rectangle(event.x-size/2, event.y-size/2,
                                          event.x + size / 2, event.y + size / 2,
                                          fill=self.canvasbg, outline=self.canvasbg)
        else:
            self.drawbox.create_oval(event.x-size/2, event.y-size/2,
                                     event.x + size / 2, event.y + size / 2,
                                     fill=self.canvasbg, outline=self.canvasbg)
        self.x, self.y = event.x, event.y

    def drawoption(self, event):
        pass

    def savefig(self):
        figname = asksaveasfilename(defaultextension='.png',
                                    filetypes=[('图像', 'png')], initialdir='.',
                                    title='Choose a path to save.')
        pass

    def loadfig(self):
        imgpath = askopenfilename(defaultextension='.png',
                                  filetypes=[('图像', 'png'), ('图像', '.jpg'),
                                             ('图像', '.gif')], initialdir='.',
                                  title='Choose an image to load.')
        img = Image.open(imgpath)
        img = img.resize((598, 498), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(img)
        self.drawbox.create_image(0, 0, anchor='nw', image=self.img)

    def clearfig(self):
        self.drawbox.delete("all")
    # 操作区显示函数区

    def labelshow(self, target, *agrs):
        """功能栏操作框现实效果"""
        # Label显示效果设置
        labels = ["line", "graph", "pen", "erasor", "option"]
        exec("self.bt_%s['relief']='groove'" % target)
        labels.remove(target)
        for tag in labels:
            cmd = "self.bt_%s['relief']='raised'" % tag
            exec(cmd)

    def frameshow(self, target):
        """放置对应的详情展开栏"""
        # Label显示效果设置
        target = target+"box"
        boxes = ["linebox", "graphbox", "penbox", "erasorbox", "optionbox"]
        exec("self.%s.place(x=0,y=0)" % target)
        boxes.remove(target)
        for box in boxes:
            cmd = "self.%s.place_forget()" % box
            exec(cmd)

    # 快捷键设置
    def shortcut(self, event):
        """快捷键的绑定"""
        # 超级键绑定暂存问题！
        print(event.keycode)
        if event.char == "l":
            """快速绘制直线"""
            self.drawbox.bind("<B1-Motion>", self.drawline)
            self.drawbox.bind("<ButtonRelease-1>", self.stopdraw)
        elif event.char in ["Control-C", "Control-c"]:
            """快速清屏"""
            self.drawbox.delete("all")
        elif event.char == "r":
            """快速选择颜色"""
            c = askcolor(color=self.drawcolor, title="选择画笔颜色")
            self.drawcolor = c[1]
        elif event.keycode == 83:
            self.savefig()
        elif event.char in ["<Control_O>", "<Control_o>"]:
            self.loadfig()
        elif event.char in ["P", "p"]:
            self.drawbox.bind("<B1-Motion>", self.drawpen)

            # Entry 数字校验区
    def numberonly(self, content):
        "输入文本验证，过滤非数字类型"
        return_variable = False  # 设置默认返回值为False
        list1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]  # 设置默认检测数列

        L_content = list(content)
        if len(content) > 1:
            del L_content[-1]

        for i in list1:  # for循环来检测最新输入的字符是否满足要求
            # 这两个条件不可以调换顺序，否则当输入框内无内容时content[-1]索引无效报错
            if content == "" or content[-1] == i:
                return_variable = True
                break
        return return_variable  # 返回值

    # line函数区

    def lsketchshow(self, *args):
        self.linesketch.delete("all")
        self.linedataflash()
        if self.dashcheck.get() == 'True':
            self.linesketch.create_line(0, 50, 100, 50,
                                        fill=self.drawcolor.get(), arrow=self.arrow.get(),
                                        dash=10, width=self.ld.get())
        else:
            self.linesketch.create_line(0, 50, 100, 50,
                                        fill=self.drawcolor.get(), arrow=self.arrow.get(),
                                        width=self.ld.get())

    def startdraw(self, event):
        if self.draw == 0:
            self.draw = 1
            if self.linecheck.get() != 1:
                self.x, self.y = event.x, event.y

    def stopdraw(self, event):
        self.draw = 0
        self.lastdraw = 0
        if self.linecheck.get() == 1:
            self.x, self.y = event.x, event.y

    def linedataflash(self, *args):
        """线型刷新数据"""
        arrowtag = {"\\": "none", "<--": "first", "-->": "last", "<->": "both"}
        linestyle = {"-": "False", "--": "True"}
        checktag = {"Radial": 0, "Multiple": 1, "Single": 2}

        self.arrow.set(arrowtag[self.set_arrow.get()])
        self.dashcheck.set(linestyle[self.set_style.get()])
        self.ld.set(int(self.set_ld.get()))
        self.linecheck.set(checktag[self.set_mode.get()])

    # 图形函数区

    def gsketchshow(self, *args):
        self.graphsketch.delete("all")
        if self.set_gtype.get() == 'Rectangle':
            cmd = 'self.graphsketch.create_rectangle(12.5, 87.5, 87.5, 12.5,\
                    %s="%s", width=%s)' % (self.set_fillstyle.get(),
                                           self.set_gcolor.get(), self.gld.get())
        else:
            cmd = 'self.graphsketch.create_oval(12.5, 87.5, 87.5, 12.5,%s="%s",\
            width=%s)' % (self.set_fillstyle.get(), self.set_gcolor.get(),
                          self.gld.get())
        exec(cmd)

    def gstartdraw(self, event):
        self.drawbox.delete(self.lastdraw)
        if self.draw == 0:
            self.draw = 1
            self.x, self.y = event.x, event.y

    def gstopdraw(self, event):
        self.draw = 0
        self.lastdraw = 0
        self.x, self.y = event.x, event.y

    # 橡皮函数区

    def esketchshow(self, *args):
        self.esketch.delete("all")
        size = self.esize.get()
        if self.set_etype.get() == 'Rectangle':
            self.esketch.create_rectangle(50-size/2, 50-size/2,
                                          50 + size / 2, 50 + size / 2,
                                          fill='violet', outline='violet')
        else:
            self.esketch.create_oval(50-size/2, 50-size/2,
                                     50 + size / 2, 50 + size / 2,
                                     fill='violet', outline='violet')

    # 设置区函数

    def setcolor(self):
        color = askcolor(color=self.drawcolor.get(),
                         title="选择画笔颜色")[1]
        if color != None:
            print(color)
            self.oxflash.set(color)
            self.colorboard['fg'] = color
            self.colorboard['text'] = color
            self.oxshow['bg'] = color
            self.drawcolor.set(color)

    def oxsetcolor(self, *args):
        try:
            color = self.oxcolor.get()
            self.colorboard['fg'] = color
            self.oxshow['bg'] = color
            self.oxtip['fg'] = 'green'
            self.oxtip['text'] = 'Color value Valid'
        except:
            self.oxtip['text'] = "This's not a valid ox value!"
            self.oxtip['fg'] = 'red'
        else:
            self.drawcolor.set(color)

    def colormode(self, event):
        mode = self.set_colormode.get()
        if mode == "Chooser":
            self.chbox.place(x=0, y=75)
            self.oxbox.place_forget()
        else:
            self.oxbox.place(x=0, y=75)
            self.chbox.place_forget()


if __name__ == "__main__":
    root = Tk()
    root.update()
    x_max, y_max = root.maxsize()
    x, y = int(x_max/2-450), int(y_max/2-545/2)
    root.geometry("900x545+%s+%s" % (x, y))
    root.title("BasicPaint")
    root.resizable(0, 0)  # 锁定长宽大小
    app = Application(master=root)
    root.mainloop()
