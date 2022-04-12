# PyInstaller

## Usage

> 文件位置跳转：       cd D:\Study\2019-2020\Python\code\reading_record
>
> 打包程序代码：       pyinstaller -F python-file-path -i icofile-path

## Description

> PyInstaller库是命令行程序，而不是IDLE中的指令，需要使用命令行使用。

**注：命令行唤出：win键+R**

如：pyinstaller -F <文件名.py>

  常用参数：

> -h                        				帮助
>
> --clean                   			清理打包过程中的临时文件(pycache及build)
>
> -D,--onedir               		默认值，生成dist文件夹
>
> **-F,--onefile              		在dist文件夹中只生成独立的打包文件**
>
> -i <图标文件名.ico>      	指定打包程序使用的图标文件且格式必须是.ico格式

ico格式转换网址：https://app.xunjiepdf.com/img2icon/

图形绘制小技巧：上网查找对应的分形几何曲线。

**Tip : About path operation**

> 1. 工作目录从C盘转移到D盘时，先在cmd中输入d:即可跳转至d盘，随后再cd至目标文件夹，不可跨盘直接跳转。
> 2.  **路径名中不能含有空格！**