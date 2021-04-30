from tkinter import *
from tkinter.colorchooser import *


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)    # super()代表的是父类的定义，而不是父类对象
        self.master = master
        self.draw = 0
        self.lastdraw = 0
        self.x,self.y=0,0
        self.fgcolor = "red"    # 渐变色？
        self.bgcolor = "black"
        self.erasorsize = 4
        
        self.pack()
        self.createWidget(master)


        
    def createContextMenu(self, event):
        Menu.post(self.drawbox, event.x_root, event.y_root)
        

    def createWidget(self, master):
        # 关于画图，完全可以使用matplotlib来实现
        self.drawbox = Canvas(root, width=680, height=320, bg=self.bgcolor)
        # 画图的背景设置只能继承类属性？不能使用实例属性？
        self.drawbox.pack(padx=10, pady=10)
        # 右键菜单栏
        self.drawbox.bind("<Button-3>", self.createContextMenu)


        bt_start = Button(master, text="开始", name="start", width=6)
        bt_start.pack(side="left", padx=15)
        bt_pen = Button(master, text="画笔", name="pen", width=6)
        bt_pen.pack(side="left", padx=15)
        bt_rect = Button(master, text="矩形", name="rect", width=6)
        bt_rect.pack(side="left", padx=15)
        bt_clear = Button(master, text="清屏", name="clear", width=6)
        bt_clear.pack(side="left", padx=15)
        bt_erasor = Button(master, text="擦除", name="erasor", width=6)
        bt_erasor.pack(side="left", padx=15)
        bt_line = Button(master, text="直线", name="line", width=6)
        bt_line.pack(side="left", padx=15)
        bt_linearrow = Button(master, text="直线箭头", name="linearrow", width=8)
        bt_linearrow.pack(side="left", padx=15)
        bt_color = Button(master, text="颜色", name="color", width=6)
        bt_color.pack(side="left", padx=15)

        root.bind_class("Button", "<1>", self.eventmanager)
        self.drawbox.bind("<ButtonRelease-1>", self.stopdraw)

        # 快捷键设定
        root.bind("<KeyPress=r>", self.shortcut)

        
    def eventmanager(self, event):
        name = event.widget.winfo_name()
        if name=="line":
            self.drawbox.bind("<B1-Motion>", self.drawline)
        elif name=="linearrow":
            self.drawbox.bind("<B1-Motion>", self.linearrow)
        elif name=="rect":
            self.drawbox.bind("<B1-Motion>", self.drawrect)
        elif name=="pen":
            self.drawbox.bind("<B1-Motion>", self.drawpen)
        elif name=="erasor":
            self.drawbox.bind("<B1-Motion>", self.drawerasor)
        elif name=="clear":
            self.drawbox.delete("all")  # 定向删除?
        elif name=="color":
            c = askcolor(color=self.fgcolor, title="选择画笔颜色")
            self.fgcolor = c[1]

                 
    def startdraw(self, event):
        self.drawbox.delete(self.lastdraw)
        
        if self.draw == 0:
            self.draw = 1
            self.x, self.y = event.x, event.y

            
    def stopdraw(self, event):
        self.draw = 0
        self.lastdraw = 0

        
    def drawline(self, event):
        self.startdraw(event)
        self.lastdraw = self.drawbox.create_line(self.x,
                                            self.y,event.x,event.y, fill=self.fgcolor)


    def linearrow(self, event):
        self.startdraw(event)
        self.lastdraw = self.drawbox.create_line(self.x,self.y,event.x,event.y,
                                                 arrow=LAST,fill=self.fgcolor)

    
    def drawrect(self, event):
        self.startdraw(event)
        self.lastdraw = self.drawbox.create_rectangle(self.x,self.y,event.x,event.y,
                                                 outline=self.fgcolor)


    def drawpen(self, event):
        self.startdraw(event)
        self.drawbox.create_rectangle(self.x,self.y,event.x,event.y,
                                                 outline=self.fgcolor)
        self.x, self.y = event.x, event.y


    def drawerasor(self, event):
        """通过绘制新的实心矩形覆盖原有图形，但这会存在一个问题，换背景颜色就全部显示出来了。"""
        self.startdraw(event)
        self.drawbox.create_rectangle(event.x-self.erasorsize/2,event.y-self.erasorsize/2,
                                      event.x+self.erasorsize/2,event.y+self.erasorsize/2,
                                      outline=self.bgcolor)
        # 功能栏更换橡皮擦样式
        self.x, self.y = event.x, event.y


    def shortcut(self, event):
        if event.char == "l":
            pass
        elif event.char == "c":
            pass
        elif event.char == "r":
            pass
        

if __name__ == "__main__":
    root = Tk()
    root.geometry("700x450+200+300")
    root.title("EasyPaint")
    app = Application(master=root)
    root.mainloop()
