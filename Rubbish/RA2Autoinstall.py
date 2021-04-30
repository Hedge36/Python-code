# test
import os
import os.path
import shutil
path = os.curdir
fileslist = os.listdir(path)
fileslist.remove('RA2Autoinstall.py')
subpath = os.path.abspath(os.path.join(os.getcwd(), ".."))
print("战役任务自动安装程序:")


def Autoinstall():
    for file in fileslist:
        filepath = os.path.join(subpath, file)
        check = os.path.exists(filepath)
        if check:
            os.remove(filepath)
        else:
            shutil.copy(file, subpath)
    if check:
        print("战役任务已移除！")
    else:
        print("战役任务已加载，赶快开始游戏吧！")
    input("键入回车退出")


Autoinstall()
