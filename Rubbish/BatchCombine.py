import os
import os.path

'''copyright
__author__ = hedge
__time__ = 2020,Oct.19th
__version__ = 3.2
version_introduction:
    To solve the problem of rank messly, we have no way to restrict its usage to the
combination of m3u8 with special name.
    remove bat file and absulte path to make program use more convenient,and
    can use anywhere,enhanced stability and usability.Besides,improved version 
    information and main usage.
'''


def load():
    "读取数据，获取当前文件所在绝对路径，文件列表及文件数目"
    path = os.getcwd()  # 返回当前目录
    filelist = os.listdir(path)
    filelist.remove('Batch Combine.py')
    number = len(filelist)
    return path, number


def word_processing(path, number):
    "文本处理，输出符合cmd语法的命令语句"
    Synthetic = base = 'Y2hlbmppbmdjb25n'
    for i in range(number - 1):
        temp = [Synthetic, base]  # 临时文本
        Synthetic = str(str(i) + "+").join(temp)
        temp[0] = Synthetic
    Synthetic += str(number - 1)
    text = 'copy /b ' + path + '\\' + Synthetic + ' ' + 'IntegrateFile'
    return text


def main():
    path, number = load()
    with open('combine.bat', 'w', encoding="utf-8") as file:
        file.write(word_processing(path, number))
    os.system(".\\combine.bat")
    os.remove('combine.bat')
    os.system("cls")
    print("%d个文件已合并为\'IntegrateFile\'" % (number))
    # 校检
    #print(word_processing(path, filelist, number))
    input("键入回车以退出程序")


main()

'''version notice:
Update suspended.
'''
