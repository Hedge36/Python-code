import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import messagebox as msg
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class MainWindow:
    def __init__(self):
        pass

    def setui(self):
        self.root = tk.Tk()
        self.root.geometry("500x460")
        self.root.title("生成RSA密钥对")

        self.path1 = tk.StringVar()
        self.path2 = tk.StringVar()
        self.path3 = tk.StringVar()
        self.path4 = tk.StringVar()
        self.entry1 = tk.StringVar()
        self.entry2 = tk.StringVar()
        self.savepath = tk.StringVar()
        self.keycount = tk.IntVar()
        self.keycount.set(1024)
        self.entry2.set("a"*16)

    def setwidget(self):
        # 参数框
        self.ParaBox = tk.LabelFrame(
            self.root, text="RSA密钥参数设定", width=480, height=70)
        self.ParaBox.place(x=10, y=10)

        tk.Label(self.ParaBox, text="密钥位数").place(x=20, y=10)
        self.count = tk.Entry(self.ParaBox, width=10,
                              textvariable=self.keycount)
        self.count.place(x=80, y=10)
        self.genkey = tk.Button(self.ParaBox, text="生成密钥对",
                                width=10, command=self.genRAS)
        self.genkey.place(x=240, y=10)

        # 生成素数框p
        self.GenBox1 = tk.LabelFrame(
            self.root, text="RSA解密", width=480, height=120)
        self.GenBox1.place(x=10, y=90)

        self.loadpub = tk.Button(self.GenBox1, text="导入私钥",
                                 width=10,  command=lambda: self.openfile("path1"))
        self.loadpub.place(x=20, y=10)
        self.pathshow1 = tk.Entry(self.GenBox1, state="readonly",
                                  textvariable=self.path1)
        self.pathshow1.place(x=105, y=15, width=220)
        self.loadfile = tk.Button(self.GenBox1, text="导入AES文件",
                                  width=10, command=lambda: self.openfile("path2"))
        self.loadfile.place(x=20, y=50)
        self.pathshow2 = tk.Entry(self.GenBox1, state="readonly",
                                  textvariable=self.path2)
        self.pathshow2.place(x=105, y=55, width=220)
        self.decode = tk.Button(self.GenBox1, text="解密", width=10,
                                command=self.decRAS)
        self.decode.place(x=360, y=30)

        # 生成素数框q
        self.GenBox2 = tk.LabelFrame(
            self.root, text="RSA加密", width=480, height=120)
        self.GenBox2.place(x=10, y=210)

        self.loadpri = tk.Button(self.GenBox2, text="导入公钥",
                                 width=10, command=lambda: self.openfile("path3"))
        self.loadpri.place(x=20, y=10)
        self.pathshow3 = tk.Entry(self.GenBox2,
                                  state="readonly", textvariable=self.path3)
        self.pathshow3.place(x=105, y=15, width=220)
        self.infile = tk.Label(self.GenBox2, text="输入AES密钥", width=10)
        self.infile.place(x=20, y=50)
        self.inaes = tk.Entry(self.GenBox2,
                              textvariable=self.entry1)
        self.inaes.place(x=105, y=55, width=220)
        self.encode = tk.Button(self.GenBox2, text="加密", width=10,
                                command=self.encRAS)
        self.encode.place(x=360, y=30)

        # 生成密钥对
        self.GenBox = tk.LabelFrame(
            self.root, text="AES加/解密", width=480, height=120)
        self.GenBox.place(x=10, y=330)

        tk.Label(self.GenBox, text="输入AES密钥").place(x=10, y=15)
        self.inkey = tk.Entry(self.GenBox, width=14, textvariable=self.entry2)
        self.inkey.place(x=90, y=15)
        self.loadfile2 = tk.Button(self.GenBox, text="导入文件",
                                   width=10, command=lambda: self.openfile("path4"))
        self.loadfile2.place(x=200, y=10)
        self.pathshow4 = tk.Entry(self.GenBox,
                                  textvariable=self.path4, state="readonly")
        self.pathshow4.place(x=280, y=15, width=180)
        self.decode2 = tk.Button(self.GenBox, text="加密", width=10,
                                 command=self.encAES)
        self.decode2.place(x=100, y=60)
        self.encode2 = tk.Button(self.GenBox, text="解密", width=10,
                                 command=self.decAES)
        self.encode2.place(x=300, y=60)

    def genRAS(self):
        random_generator = Random.new().read
        rsa = RSA.generate(self.keycount.get(), random_generator)
        private_pem = rsa.exportKey()
        with open("private.pem", "wb") as f:
            f.write(private_pem)
        public_pem = rsa.publickey().exportKey()
        with open("public.pem", "wb") as f:
            f.write(public_pem)
        msg.showinfo(title="提示", message="RSA密钥文件已保存至当前目录下！")

    def decRAS(self):
        if self.path1.get() == "" or self.path2.get() == "":
            msg.showwarning(title="警告", message="请先导入文件！")
        else:
            with open(self.path1.get()) as f:
                key = f.read()
            with open(self.path2.get()) as f:
                enc_aeskey = f.read()
            rsakey = RSA.importKey(key)
            cipher = Cipher_pkcs1_v1_5.new(rsakey)
            text = cipher.decrypt(base64.b64decode(enc_aeskey), "解密失败")
            self.showres(text)

    def encRAS(self):
        print(self.path3.get(), self.entry1.get())
        if self.path3.get() == "" or self.entry1.get() == "":
            msg.showwarning(title="警告", message="请先写入数据！")
        else:
            with open(self.path3.get()) as f:
                key = f.read()

            message = self.entry1.get()
            rsakey = RSA.importKey(key)
            cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 创建用于执行pkcs1_v1_5加密或解密的密码
            cipher_text = base64.b64encode(cipher.encrypt(
                message.encode('utf-8'))).decode('utf-8')
            with open("AESkey", "w") as f:
                f.write(cipher_text)
            msg.showinfo(title="提示", message="加密文件已保存至AESkey!")

    def decAES(self):
        if self.path4.get() == "" or self.entry2.get() == "":
            msg.showwarning(title="警告", message="请先写入数据！")
        else:
            text = open(self.path4.get()).read()
            key = self.entry2.get().encode('utf-8')
            iv = b'qqqqqqqqqqqqqqqq'
            cryptor = AES.new(key, AES.MODE_CBC, iv)
            plain_text = cryptor.decrypt(a2b_hex(text))
            ciphertext = bytes.decode(plain_text).rstrip('\0')
            print(type(ciphertext))
            with open("Decrypt.txt", "w") as f:
                f.write(ciphertext)
            msg.showinfo(title="提示", message="加密文件已保存至Decrypt.txt!")

    def encAES(self):
        if self.path4.get() == "" or self.entry2.get() == "":
            msg.showwarning(title="警告", message="请先写入数据！")
        else:
            text = open(self.path4.get()).read()
            text = self.add_to_16(text)
            key = self.entry2.get().encode('utf-8')
            iv = b'qqqqqqqqqqqqqqqq'
            cryptos = AES.new(key, AES.MODE_CBC, iv)
            cipher_text = cryptos.encrypt(text)
            ciphertext = b2a_hex(cipher_text)
            with open("Cipher.txt", "w") as f:
                f.write(str(ciphertext)[2:-1])
            msg.showinfo(title="提示", message="加密文件已保存至Cipher.txt!")

    def add_to_16(self, text):
        if len(text.encode('utf-8')) % 16:
            add = 16 - (len(text.encode('utf-8')) % 16)
        else:
            add = 0
        text = text + ('\0' * add)
        return text.encode('utf-8')

    def openfile(self, name):
        filename = filedialog.askopenfilename(initialdir=".")
        if filename:
            command = f'self.{name}.set("{filename}")'
            exec(command, locals())

    def mainloop(self):
        self.root.mainloop()

    def showres(self, text):
        temp = tk.Tk()
        temp.geometry("200x200")
        tk.Label(temp, text=text).place(x=10, y=10)
        confirm = tk.Button(temp, text="退出", command=temp.destroy)
        confirm.place(x=60, y=160, width=80)


root = MainWindow()
root.setui()
root.setwidget()
root.mainloop()
