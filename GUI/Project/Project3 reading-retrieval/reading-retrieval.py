# reading_retrieval
import os
import traceback
import xlwt

"""
---------------------------------------------------------------------------------
Author =  Hedge

last modified time = Mar. 17th, 2021

Version = 2.4.5

Version introduction:
    1. Separate editing and retrieval functions, add the write and modify function in editor mode;
    2. Improve the function description;
    3. Perfect the response when the document is empty or empty line.

Main introduction:
    Record the books that ha been read, which is convenient for rereading and 
    arranging the reading plan as a whole. 
    
Update notice:
    Perfect editor mode, perfect the function that return to the previous directory, cancel operation,
    change another book, and realize the modifying and duplicate checking functions of books. Please
    look forward to the update time.
---------------------------------------------------------------------------------
"""


def read_file():
    "文本读取，提取文本信息"
    with open("阅读记录.data", "r", encoding='UTF-8') as f:
        file_lists = f.readlines()
        file_lists = [i for i in file_lists if i not in ["", "\n"]]
        # 除去空的行
        return file_lists


def get_data(file_lists):
    "数据读取，将文本信息中的书籍数据提取出来"
    data_lists = []
    if len(file_lists) != 0:
        for i in file_lists:
            data_lists.append(i.split('|'))
            data_lists[-1][0] = int(data_lists[-1][0])
            data_lists[-1][-1] = data_lists[-1][-1].strip()
    return data_lists   # 书目清单


def list_print(target_list):
    "结果打印，将查询的结果打印出来"
    print("检索序号： %s" % (target_list[0]))
    print("书籍名称：《%s》" % (target_list[1]))
    # a: 双标签
    print("书籍类别： %s" % (target_list[2]))
    print("简要概述： %s" % (target_list[3]))
    print("阅读进度： %s" % (target_list[4]))
    print("复阅评估： %s" % (target_list[5]), end="\n\n")


def retrieval(data_lists, mode=0, command=None):
    """mode = 0时为retrieval模式，包含序号检索、名称检索、类别检索、复阅检索、进度检索、全部检索功能；
    不为零时为editor模式执行对应辅助功能。"""

    def mode_input(word, mode=0):
        "调整输入模式，若为editor模式，则直接读取data，若为retrieval模式，则由用户输入。"
        if mode == 0:
            return input(word)
        else:
            return command

    def mode_print(text, end='\n'):
        "调整输出模式，若为editor模式，仅读取数据，若为retrieval模式，则打印结果"
        if mode == 0:
            print(text, end=end)
        else:
            pass

    a = 0   # 计数
    if mode == 0:
        print("现支持检索条件：1.序号检索 2.名称检索 3.类别检索 4.复阅检索 5.进度检索 6.全部检索")
        condition = int(input("请输入检索条件对应序号:"))
    else:
        condition = mode
    try:
        if condition == 1:  # 序号检索
            mode_print("————————————————————————————————")
            serial_number = int(mode_input("请输入需要检索的序号:", mode))  # 检索序号
            mode_print("————————————————————————————————")
            if_find = False  # 是否有检索结果
            os.system("cls")

            for i in data_lists:
                if serial_number == i[0]:
                    mode_print("检索结果如下：")
                    list_print(i)
                    if_find = True
                    break

            if not if_find:
                mode_print("未找到对应序号为%s的阅读记录" % (serial_number))
                # a：如果空，给出一个相近的搜索结果
            mode_print("————————————————————————————————")

        elif condition == 2:    # 名称检索
            mode_print("————————————————————————————————")
            name_book = mode_input("请输入需要检索的书籍名称:", mode)
            mode_print("————————————————————————————————")

            if_find = False
            os.system("cls")
            for i in data_lists:
                if name_book == i[1]:
                    mode_print("检索结果如下：")
                    list_print(i)
                    if_find = True
                    break

            if not if_find:
                mode_print("未找到书籍名称为《%s》的阅读记录" % (name_book))
            mode_print("————————————————————————————————")

        elif condition == 3:    # 类别检索
            os.system("cls")
            mode_print("————————————————————————————————")
            mode_print("现可供检索的类别：")
            temp_list = []  # 现有类别临时列表
            for i in data_lists:
                if i[2] not in temp_list:
                    temp_list.append(i[2])
                    mode_print(i[2], end=",")
            mode_print("\n————————————————————————————————")

            category_book = mode_input("请输入需要检索的书籍类别：", mode).split("，")
            mode_print("————————————————————————————————")
            os.system("cls")
            if_find = False

            for i in data_lists:
                if i[2] in category_book:
                    if not if_find:
                        print("检索结果如下：")
                        if_find = True
                    list_print(i)
                    a += 1
            mode_print("共检索到%d条阅读记录" % (a))

            if not if_find:
                mode_print("未找到书籍类别为%s的阅读记录" % (category_book))

            mode_print("————————————————————————————————")

        elif condition == 4:    # 复阅评估检索
            os.system("cls")
            if mode == 0:
                mode_print("————————————————————————————————")
                mode_print("提示：可供检索的复阅类型\n是（推荐复阅），否（不推荐复阅），可选（可供选择复阅），待评估")
            evaluation_book = mode_input("\n请输入需要检索的复阅类型：", mode).split("，")
            mode_print("————————————————————————————————")

            if_find = False

            if evaluation_book in ["是", "否", '待评估', "可选"]:
                for i in data_lists:
                    if i[5] in evaluation_book:
                        if not if_find:
                            print("检索结果如下：")
                            if_find = True
                        list_print(i)
                        a += 1
                mode_print("共检索到%d条阅读记录" % (a))

            else:
                mode_print("输入格式有误")

            if not if_find:
                mode_print("未找到复阅类型为%s的书籍" % (evaluation_book))

            mode_print("————————————————————————————————")

        elif condition == 6:    # 全部检索
            os.system("cls")
            print("————————————————————————————————")
            print("检索结果如下：")
            if len(data_lists) == 0:
                print("当前没有读书记录")
                if_find = False
            else:
                for i in data_lists:
                    list_print(i)
                    a += 1
                print("共检索到%d条阅读记录" % (a))
                if_find = True
            print("————————————————————————————————")

        elif condition == 5:    # 阅读进度检索
            process = ['已完成', '进行中', '待安排', '暂搁置', '初完成']
            os.system("cls")
            mode_print("阅读进度类型选择：已完成，进行中，待安排，暂搁置，初完成")
            demand = str(mode_input("输入阅读进度检索类型:", mode)).split("，")
            check_demand = True
            if_find = False

            for word in demand:
                if word in process:
                    pass
                else:
                    check_demand = False

            if check_demand:
                for i in data_lists:
                    if i[4] in demand:
                        if not if_find:
                            mode_print("检索结果如下：")
                            if_find = True
                        list_print(i)
                        a += 1
                mode_print("共检索到%d条阅读记录" % (a))

                if not if_find:
                    mode_print("未找到书籍类别为%s的记录" % (demand))
                mode_print("————————————————————————————————")
            else:
                mode_print("输入格式有误")
    except ValueError:
        print("输入格式有误")
    return if_find


def editor_writing(data_lists):
    "editor模式——写入模式，能够将新书籍写入文本中，无参数。"
    def check_input(mode, instruction):
        '检查输入书目是否已存在'
        information = input(instruction)
        if retrieval(data_lists, 2, information):
            print("该书籍已存在，可通过名称检索对应信息。")
        else:
            return information

    number = str(len(data_lists) + 1)  # 检索序号
    name = check_input(2, "请输入书籍名称(无需书名号):\n")  # 书名
    category = input("请输入书籍所属类别:\n")
    introduction = input("请输入书籍简介:\n")
    condition = False

    while not condition:
        check = input("请输入书籍当前阅读进度(已完成/待安排/进行中/暂搁置/初完成):\n")
        if check in ['已完成', '待安排', '进行中', "暂搁置", "初完成"]:
            process = check     # 阅读进度
            condition = True
        else:
            print("输入格式有误，请检查后重新输入！")

    condition = False
    while not condition:
        check = input("请输入书籍复阅评估(是/待评估/否/可选):\n")
        if check in ['是', '待评估', '否', '可选']:
            assessment = check     # 复阅评估
            if process != '已完成' or check != '待评估':
                condition = True
            else:
                print("已完成书籍复阅评估不应该为待评估，请重新输入！")
        else:
            print("输入格式有误，请检查后重新输入！")
    # 完整信息流处理
    information = '|'.join(
        [number, name, category, introduction, process, assessment])
    # 信息写入
    with open("阅读记录.data", "a", encoding='UTF-8') as f:
        f.write('\n'+information)
    print("索引序号为{}的《{}》已成功写入!".format(number, name))


def editor_modify(data_lists, mode=0):
    "editor模式——修订模式，能够修改现存书籍信息，现仅支持序号检索修正，其他修正模式敬请期待，无参数。"
    def num_correct():
        "序号检索修正"
        cnum = int(input("待修改书籍序号:"))    # 书籍索引序号
        list_print(data_lists[cnum - 1])
        return cnum
        # a:换一本书！

    def modify():
        "修正后的信息流写入"
        with open("阅读记录.data", "w", encoding='UTF-8') as f:
            for line in data_lists:
                line[0] = str(line[0])
                f.write("|".join(line)+'\n')
        print("信息已修正！")
    if mode == 0:
        cnum = num_correct()

    cat = input("请输入想要修改的信息类型或删除该条目(输入d或D)：")  # 处理类型
    # a:取消操作！
    key = {"书籍名称": 1, "书籍类别": 2, "简要概述": 3,
           "阅读进度": 4, "复阅评估": 5, 'd': 0, 'D': 0}
    # a: 完善信息提示(不同操作不同提示内容)
    bnum = key.get(cat)  # 输入信号对应操作序号
    if bnum:
        correct = input("修改后的信息:")
        data_lists[cnum - 1][key.get(cat)] = correct
    else:
        data_lists.remove(data_lists[cnum - 1])
        for i in range(len(data_lists)):
            data_lists[i][0] = i+1    # 修正删除条目后的序号
    modify()


def loadxls():
    """读取excel文件，获取书籍"""
    pass


def savefile(data_lists):
    """保存为excel文件"""
    file = xlwt.Workbook()
    size = len(data_lists)
    sheet1 = file.add_sheet(u"书籍记录", cell_overwrite_ok=True)
    basic_info = ["检索序号", "书籍名称", "书籍类别", "简要概述", "阅读进度", "复阅评估"]
    for m in range(6):
        sheet1.write(0, m, basic_info[m])   # 表头
    for i in range(1, size+1):
        for j in range(6):
            sheet1.write(i, j, data_lists[i][j])    # 详细信息
    file.save("Book_record.xls")


def main():
    file_lists = read_file()
    data_lists = get_data(file_lists)
    if len(data_lists) != 0:
        modechoose1 = input("请选择使用模式: 0检索模式；1编辑模式\n")    # 模式选择
        os.system("cls")
        if modechoose1 == '0':
            retrieval(data_lists)
            modifycheck = input("是否进入修订模式？（y/n）")
            if modifycheck in ["y", "Y", "yes", "Yes"]:
                editor_modify(data_lists)
            # a: 检索后进入修正模式!未完成！
        elif modechoose1 == '1':
            modechoose2 = input("编辑模式：0添加模式；1修订模式\n")
            # a: 返回上一级！
            if modechoose2 == '0':
                editor_writing(data_lists)
            elif modechoose2 == '1':
                editor_modify(data_lists)
            else:
                print("怠惰的程序员没有设计异常处理程序，因此当你乱输只能乖乖重启")
        else:
            print("怠惰的程序员没有设计异常处理程序，因此当你乱输只能乖乖重启")
    else:
        modechoose1 = input("当前阅读计划为空，是否进入editor-添加模式(y/n)：\n")
        if modechoose1 in ["y", "Y", "yes", "Yes"]:
            editor_writing(data_lists)


if __name__ == "__main__":
    try:
        repeat = True   # 重复运行检查
        while repeat:
            main()
            repeat_check = input("键入回车以退出程序或输入任意键重启程序")
            os.system("cls")
            if repeat_check == '':
                repeat = False
    except:
        traceback.format_exc()
