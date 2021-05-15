from tkinter import *
from tkinter.colorchooser import *
from tkinter.ttk import Combobox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)    # super()代表的是父类的定义，而不是父类对象
        self.master = master
        # 实例窗口属性
        self.draw = 0
        self.lastdraw = 0
        self.x, self.y = 0, 0
        self.fgcolor = "red"    # 渐变色？
        self.canvasbg = "white"
        self.erasorsize = 4
        # 线型变量
        self.arrow = StringVar()
        self.linecheck = IntVar()
        self.dashcheck = StringVar()
        self.ld = IntVar()
        # 图形变量
        self.gld = IntVar()
        # 选项变量
        self.drawcolor = StringVar()
        # 窗口初始化
        self.pack()
        self.createWidget(master)

    def createContextMenu(self, event):
        """右键菜单栏，正在设计中。"""
        Menu.post(self.drawbox, event.x_root, event.y_root)

    def createWidget(self, master):
        """组件初始化"""
        # 关于画图，完全可以使用matplotlib来实现
        self.drawbox = Canvas(root, width=598, height=498, bg=self.canvasbg,
                              bd=1, relief="solid")

        # 画图的背景设置只能继承类属性？不能使用实例属性？
        self.drawbox.place(x=10, y=30)
        # 右键菜单栏
        self.drawbox.bind("<Button-3>", self.createContextMenu)
        # 功能区
        self.funcbox = Frame(width=270, height=500)
        self.funcbox.place(x=620, y=32)
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
        Label(self.linebox, text="ArrowStyle").place(x=20, y=40)
        self.set_arrow = Combobox(self.linebox, state="readonly",
                                  values=["\\", "<--", "-->", "<->"])
        self.set_arrow.current(0)
        self.set_arrow.place(x=100, y=40, relwidth=0.4)
        # 线型
        Label(self.linebox, text="LineStyle").place(x=20, y=80)
        self.set_style = Combobox(self.linebox, state="readonly",
                                  values=["-", "--"])
        self.set_style.current(0)
        self.set_style.place(x=100, y=80, relwidth=0.4)
        # 模式
        Label(self.linebox, text="PenMode").place(x=20, y=120)
        self.set_mode = Combobox(self.linebox, state="readonly",
                                 values=["Single", "Multiple", "Radial"])
        self.set_mode.current(0)
        self.set_mode.place(x=100, y=120, relwidth=0.4)
        # 线宽
        Label(self.linebox, text="LineWidth").place(x=20, y=160)
        check = self.register(self.numberonly)
        self.set_ld = Entry(self.linebox, highlightcolor="sky blue", highlightthickness=1,
                            textvariable=self.ld,
                            validate="key", validatecommand=(check, '%P'))
        self.set_ld.place(x=100, y=160, relwidth=0.4)
        self.ld.set(1)
        self.ld.trace("w", self.lsketchshow)
        # 预览图
        self.linesketchbox = Frame(
            self.linebox, height=140, bd=1, relief='groove')
        self.linesketchbox.place(y=330, relwidth=1)
        self.linesketch = Canvas(self.linesketchbox, width=98, height=98, bg=self.canvasbg,
                                 bd=1, relief="solid")
        Label(self.linesketchbox, text="效果图").place(x=20, y=60)
        self.linesketch.place(x=120, y=20)
        self.linesketch.create_line(0, 50, 100, 50, width=1)

        # 图形详情栏
        self.graphbox = Frame(self.detailbox, width=269, height=470)
        # 图形类型
        Label(self.graphbox, text="GraphStyle").place(x=20, y=40)
        self.set_gtype = Combobox(self.graphbox, values=["Rectangle", "Oval"],
                                  state="readonly",)
        self.set_gtype.current(0)
        self.set_gtype.place(x=100, y=40, relwidth=0.4)
        # 填充类型
        Label(self.graphbox, text="FillStyle").place(x=20, y=80)
        self.set_fillstyle = Combobox(self.graphbox, state="readonly",
                                      values=["outline", "fill"])
        self.set_fillstyle.current(0)
        self.set_fillstyle.place(x=100, y=80, relwidth=0.4)
        # 颜色
        Label(self.graphbox, text="Color").place(x=20, y=120)
        self.set_gcolor = Combobox(self.graphbox, state="readonly",
                                   values=["red", "blue"])
        self.set_gcolor.current(0)
        self.set_gcolor.place(x=100, y=120, relwidth=0.4)
        # 线宽
        Label(self.graphbox, text="LineWidth").place(x=20, y=160)
        self.set_gld = Entry(self.graphbox, highlightcolor="sky blue",
                             highlightthickness=1, textvariable=self.gld,
                             validate="key", validatecommand=(check, '%P'))
        self.set_gld.place(x=100, y=160, relwidth=0.4)
        self.gld.set(1)
        self.gld.trace("w", self.gsketchshow)
        # 预览图
        self.graphsketchbox = Frame(self.graphbox, height=140, bd=1,
                                    relief='groove')
        self.graphsketchbox.place(y=330, relwidth=1)
        self.graphsketch = Canvas(self.graphsketchbox, width=98, height=98,
                                  bg=self.canvasbg, bd=1, relief="solid")
        Label(self.graphsketchbox, text="效果图").place(x=20, y=60)
        self.graphsketch.place(x=120, y=20)
        self.graphsketch.create_rectangle(12.5, 87.5, 87.5, 12.5, outline="red",
                                          width=1)

        self.penbox = Frame(self.detailbox, width=269, height=470)
        self.erasorbox = Frame(self.detailbox, width=269, height=470)

        # 设置区
        self.optionbox = Frame(self.detailbox, width=269, height=470)
        Label(self.optionbox, text="ColorMode").place(x=20, y=20)
        self.drawcolor.set("#ff0000")
        self.set_colormode = Combobox(self.optionbox, state="readonly",
                                      values=["Ox", "Chooser"])
        self.set_colormode.current(0)
        self.set_colormode.place(x=110, y=20, relwidth=0.4)
        self.oxbox = Frame(self.optionbox, width=269, height=470)
        Label(self.oxbox, text="Colorname").place(x=20, y=10)
        self.oxcolor = Entry(self.oxbox, textvariable=self.drawcolor,
                             highlightcolor="sky blue",
                             highlightthickness=1, width=15)
        self.oxcolor.place(x=110, y=10)
        self.oxshow = Label(self.oxbox, bg='red', bd=1, relief='solid')
        self.oxshow.place(x=230, y=10, width=20, height=20)
        self.oxbox.place(x=0, y=50)
        self.chbox = Frame(self.optionbox, width=269, height=470)
        Label(self.chbox, text="Colorset").place(x=20, y=15)
        self.colorboard = Label(self.chbox, textvariable=self.drawcolor)
        self.colorboard.place(x=110, y=15)
        Button(self.chbox, text="⚙", command=self.setcolor).place(x=200, y=10)

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
        self.set_colormode.bind("<<ComboboxSelected>>", self.colormode)

        # 快捷键设定,此处监听了所有按键
        root.bind("<KeyPress>", self.shortcut)

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
                                                         fill=self.fgcolor, arrow=self.arrow.get(),
                                                         dash=10, width=self.ld.get())
            else:
                self.lastdraw = self.drawbox.create_line(self.x, self.y, event.x, event.y,
                                                         fill=self.fgcolor, arrow=self.arrow.get(),
                                                         width=self.ld.get())
            # arrowshape不会搞，不搞了
            # 旁边增设⚙按钮设置宽度值，暂时懒得弄

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
        self.drawbox.create_rectangle(self.x, self.y, event.x, event.y,
                                      outline=self.fgcolor)
        self.x, self.y = event.x, event.y

    def drawerasor(self, event):
        """通过绘制新的实心矩形覆盖原有图形，但这会存在一个问题，换背景颜色就全部显示出来了。"""
        self.startdraw(event)
        self.drawbox.create_rectangle(event.x-self.erasorsize/2, event.y-self.erasorsize/2,
                                      event.x+self.erasorsize/2, event.y+self.erasorsize/2,
                                      outline=self.canvasbg)
        # 功能栏更换橡皮擦样式
        self.x, self.y = event.x, event.y

    def drawoption(self, event):
        pass

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
        # 也可以通过设置button的accelerate来实现。
        if event.char == "l":
            """快速绘制直线"""
            self.drawbox.bind("<B1-Motion>", self.drawline)
        elif event.char == "c":
            """快速清屏"""
            self.drawbox.delete("all")
        elif event.char == "r":
            """快速选择颜色"""
            c = askcolor(color=self.fgcolor, title="选择画笔颜色")
            self.fgcolor = c[1]

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
                                        fill=self.fgcolor, arrow=self.arrow.get(),
                                        dash=10, width=self.ld.get())
        else:
            self.linesketch.create_line(0, 50, 100, 50,
                                        fill=self.fgcolor, arrow=self.arrow.get(),
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

    # 设置区函数
    def setcolor(self):
        color = askcolor(color=self.drawcolor.get(),
                         title="选择画笔颜色")[1]
        if color != "None":
            self.drawcolor.set(color)
        self.colorboard['fg'] = self.drawcolor.get()
        self.oxshow['bg'] = self.drawcolor.get()

    def colormode(self, event):
        mode = self.set_colormode.get()
        if mode == "Chooser":
            self.chbox.place(x=0, y=50)
            self.oxbox.place_forget()
        else:
            self.oxbox.place(x=0, y=50)
            self.chbox.place_forget()


if __name__ == "__main__":
    root = Tk()
    root.geometry("900x545+200+300")
    root.title("BasicPaint")
    root.resizable(0, 0)  # 锁定长宽大小
    app = Application(master=root)
    root.mainloop()
