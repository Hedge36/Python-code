# 战役任务管理工具
'''
设计功能：
1. 检测现已安装的任务
2. 自动给未安装Autoinstall的文件夹复制文件
3. 给所有文档写入一个识别文本
'''


import shutil
import os.path
import os


j = os.path.join
path = os.curdir    # 当前路径
fileslist = os.listdir(path)    # 当前文件夹文件列表
fileslist.remove('RA2Autoinstall.py')
fileslist.remove('RA2Manage tools.py')
subpath = os.path.abspath(j(os.getcwd(), ".."))
# 上一级路径RA2根目录
diretion = j(subpath, 'direction.data')
print("战役任务管理程序:")


def installed_check():
    "已安装战役任务识别"
    if os.path.exists(diretion):
        with open(diretion, 'r', encoding='UTF-8') as f:
            name = f.read()
        print("当前已安装战役任务:", name)
        check = input("是否卸载当前战役任务？Y/N\n")
        if check in ['Y', 'Yes', 'yes']:
            filepath = os.path.abspath(path+'//' + name + '//Autoinstall.py')
            print(filepath)
            os.system(filepath)
        else:
            pass
    else:
        print("当前尚未安装任务外置战役任务！")


def Direction_install():
    "新安装战役任务识别文本写入"
    check = False   # 校检
    for file in fileslist:
        filepath = path+'/'+file+'/direction.data'  # 识别文本路径
        if os.path.exists(filepath):
            pass
        else:
            with open(filepath, 'x', encoding='UTF-8') as f:
                f.write(file)
                check = True
    if check == True:
        print("识别文本已成功写入")
    else:
        print("当前文件均已配置识别文本")


installed_check()
input("键入回车退出程序")
