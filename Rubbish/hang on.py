import time
import pyautogui
import random

__author__ = 'hedge'
__version__ = '2.0'

print("请将鼠标移动到待挂机位置，注意请不要把鼠标停在重要按钮上，3s后开始挂机")
print("键入ctrl+c退出程序")
time.sleep(3)  # 延迟3秒
start = time.perf_counter()


# 主程序
def hang():
    """自动点击屏幕，防止熄屏"""
    # step = random.randint(10, 19) * 60  # 待机间隔/min
    step = 1
    print("正在待机.....")
    while True:
        time.sleep(step)  # 警告，间隔不易过短，否则无法结束程序
        # pyautogui.moveTo(1883, 1024, duration=3)  # 鼠标移动
        pyautogui.click()


def adjust():
    size = pyautogui.position()  # 获取当前鼠标位置
    print(size)


def main():
    try:
        print("开始待机")
        hang()
    except:
        print('共待机', round((time.perf_counter() - start) / 60, 3), 'min')
        print('程序已退出，再次键入回车关闭窗口')
        input()


main()
# adjust()


'''
x, y = 411, 417  # 鼠标需要移动到的位置（需修正）
step_seconds = 3  # 将鼠标移动到指定坐标的间隔时间
size = pyautogui.position() # 获取当前鼠标位置

update notice:
1. About screen sleep:
1) Modify the main program to run every second
2) Threading 
2. About time bar:
Modify time bar to dynamic.
'''
