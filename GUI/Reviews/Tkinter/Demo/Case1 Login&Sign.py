#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/3/11 19:20
# @Author : Hedge
# @File : Case1 Login&Sign.py
# @Software: PyCharm
import pickle
import tkinter as tk
import tkinter.messagebox


def user_login():
    """账户登陆"""
    user_name = var_user_name.get()
    user_pwd = var_user_pwd.get()
    try:
        with open("user_info.pickle", "rb") as user_file:
            user_info = pickle.load(user_file)
    except FileNotFoundError:
        with open("user_info.pickle", "wb") as user_file:
            user_info = {"admin": "admin"}
            pickle.dump(user_info, user_file)

    if user_name in user_info:
        if user_pwd == user_info[user_name]:
            tk.messagebox.showinfo("Welcome", message="How are you? " + user_name)
        else:
            tk.messagebox.showerror("Error", message="Your password is wrong, please try again!")
    else:
        is_sign_up = tk.messagebox.askyesno("Welcome", message="You haven\'t sign"
                                                               "up yet. Sign up now?")
        if is_sign_up:
            user_sign_up()


def user_sign_up():
    """账户注册"""

    def sign_to_Mofan_Python():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open('user_info.pickle', 'rb') as user_file:
            exist_user_info = pickle.load(user_file)
        if np != npf:
            tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')
        elif nn in exist_user_info:
            tk.messagebox.showerror('Error', 'The user has already signed up!')
        else:
            exist_user_info[nn] = np
            with open('user_info.pickle', 'wb') as user_file:
                pickle.dump(exist_user_info, user_file)
            tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            window_sign_up.destroy()

    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry("350x200")
    window_sign_up.title("Sign up window")

    new_name = tk.StringVar()
    tk.Label(window_sign_up, text="User name:").place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text="Password:").place(x=10, y=50)
    entry_new_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show="*")
    entry_new_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text="Confirm password:").place(x=10, y=90)
    entry_new_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show="*")
    entry_new_pwd_confirm.place(x=150, y=90)

    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Mofan_Python)
    btn_comfirm_sign_up.place(x=150, y=130)

    btn_login = tk.Button(window, text='Login', command=user_login)
    btn_login.place(x=170, y=230)
    btn_sign_up = tk.Button(window, text='Sign up', command=user_sign_up)
    btn_sign_up.place(x=270, y=230)


window = tk.Tk()
window.title("login?")
window.geometry("450x300")

canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file="vs_skin.gif")
image = canvas.create_image(0, 0, anchor="nw", image=image_file)
canvas.pack(side="top")

# user information
tk.Label(window, text="User name:").place(x=50, y=150)
tk.Label(window, text="Password:").place(x=50, y=190)
var_user_name = tk.StringVar()
var_user_name.set("@qq.com")
var_user_pwd = tk.StringVar()

entry_user_name = tk.Entry(window, textvariable=var_user_name)
entry_user_name.place(x=160, y=150)

entry_user_pwd = tk.Entry(window, textvariable=var_user_pwd, show="?")
entry_user_pwd.place(x=160, y=190)
btn_login = tk.Button(window, text="Login", command=user_login)
btn_login.place(x=170, y=230)
btn_sign_up = tk.Button(window, text="Sign up", command=user_sign_up)
btn_sign_up.place(x=270, y=230)

window.mainloop()
