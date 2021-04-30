# 战役任务管理工具
'''
设计功能：
1. 检测现已安装的任务
2. 自动给未安装Autoinstall的文件夹复制文件
3. 给所有文档写入一个识别文本
4. 恢复战役任务存档
'''


import shutil
import os.path
import os


__author__ = 'hedge'
__date__ = '2021.1.1'


j = os.path.join
path = os.curdir    # 当前路径
fileslist = os.listdir(path)    # 当前文件夹文件列表
fileslist.remove('Autoinstall.py')
fileslist.remove('Manage tools.py')
subpath = os.path.abspath(j(os.getcwd(), ".."))
# 上一级路径RA2根目录
diretion = j(subpath, 'direction.data')


def installed_check():
    "已安装战役任务识别"
    if os.path.exists(diretion):
        with open(diretion, 'r', encoding='UTF-8') as f:
            name = f.read()
        print("当前已安装战役任务:", name)
        check = input("是否卸载当前战役任务？Y/N\n")
        if check in ['Y', 'Yes', 'yes', 'y']:
            filepath = os.path.abspath(path+'//' + name)
            os.chdir(filepath)
            os.system('python Autoinstall.py')
        else:
            pass
    else:
        print("当前尚未安装任何外置战役任务！")


def Direction_install():
    "新安装战役任务识别文本及安装程序写入"
    check = False   # 校检
    for file in fileslist:
        filepath = j(path, file)  # 子文件路径
        if os.path.exists(j(filepath, 'direction.data')):
            pass
        else:
            with open(j(filepath, 'diretion.data'), 'w', encoding='UTF-8') as f:
                f.write(file)
                check = True
            shutil.copy('Autoinstall.py', filepath)
    if check == True:
        print("基础配置文件已成功写入")
    else:
        print("当前文件均已配置完毕")


def Autoinstall_update():
    "更新Autoinstall.py文件"
    for file in fileslist:
        filepath = j(path, file)  # 子文件路径
        if os.path.exists(j(filepath, 'Autoinstall.py')):
            os.remove(j(filepath, 'Autoinstall.py'))
        shutil.copy('Autoinstall.py', filepath)
    print("Autoinstall.py更新完毕")


def main():
    print("欢迎使用战役任务管理程序")
    print("现开放功能：")
    print("1. 检测当前战役任务安装情况；\n2. 对最新下载的战役任务进行配置；\
            \n3. 更新所有子文件夹中的Autoinstall.py文件；\n")
    number = input("选择要执行的功能：\n")
    if number == '1':
        installed_check()
    elif number == '2':
        Direction_install()
    elif number == '3':
        Autoinstall_update()
    else:
        print('无效的输入，请重新启动程序')
    input("键入回车退出程序")


main()
