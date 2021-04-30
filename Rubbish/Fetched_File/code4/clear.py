import os.path
import os
cpath = os.path.dirname(__file__)
cname = "clear.py"
fileslist = os.listdir(cpath)
fileslist.remove(cname)


def deletefile(filelist):
    for file in fileslist:
        filepath = os.path.join(cpath, file)
        os.remove(filepath)
    print("文件已移除！")


deletefile(cpath)
