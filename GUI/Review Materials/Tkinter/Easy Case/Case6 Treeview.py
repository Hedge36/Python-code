import tkinter as tk
from tkinter import ttk


def treeview_sort(col):
    global reverseFlag
    lst = [(tree.set(st, col), st) for st in tree.get_children("")]
    lst.sort()
    for index, item in enumerate(lst):
        tree.move(item[1], "", index)
    reverseFlag = not reverseFlag


root = tk.Tk()
root.title("treeview")
reverseFlag = False

mystate = {"Illinois", "California", "Texas", "Fujian", "Guangdong", "Washington",
           "Tianjin", "Beijing", "Hunan", "Shandong", "Dongguan"}
tree = ttk.Treeview(root, columns=("states"), show="headings")
yscrollbar = tk.Scrollbar(root)
yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.pack()
yscrollbar.config(command=tree.yview)
tree.configure(yscrollcommand=yscrollbar.set)
tree.heading("states", text="State")
for state in mystate:
    tree.insert("", tk.END, values=(state,))
tree.heading("#1", text="State", command=lambda c="states": treeview_sort(c))

root.mainloop()
