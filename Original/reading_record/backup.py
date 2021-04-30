import os
import os.path
import shutil


def load():
    "读取数据，获取当前文件所在绝对路径，文件列表及文件数目"
    path = os.getcwd()  # 返回当前目录
    filelist = os.listdir(path)
    filelist.remove(os.path.basename(__file__))
    return filelist


def backup(filelist):
    "快速备份当前文件至目标路径"
    path = "D:\\Study\\2019-2020\\Python\\code\\backup\\reading record"    # 目标路径
    for file in filelist:
        filepath = os.path.join(path, file)
        # 如果文件已存在，则删除原文件
        check = os.path.exists(filepath)
        if check:
            os.remove(filepath)
        shutil.copy(file, path)


filelist = load()
backup(filelist)
