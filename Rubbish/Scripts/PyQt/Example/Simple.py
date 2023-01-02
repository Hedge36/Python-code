import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x400")
root.title("标题")

tk.Label(text="标签").pack()
tk.Radiobutton(text="单选按钮").pack()
tk.Entry(text="文本框").pack()
tk.Checkbutton(text="复选框").pack()
ttk.Combobox(values=("下拉列表框")).pack()
ttk.Labelframe(text="标签框", width=100, height=100).pack()
tab = ttk.Notebook(root, width=100, height=100)
tab.pack()
tab.add(tk.Label(text="选项卡"), text="tab1")
tab.add(tk.Label(text="选项卡"), text="tab2")

root.mainloop()
