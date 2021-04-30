# reading record update-data
class Book:
    count = 0
    def __init__(self, data):
        self.number = data[0]
        self.name = data[1]
        self.category = data[2]
        self.overview = data[3]
        self.process = data[4]
        self.assessment = data[5]
        Book.count+= 1    # 实例对象计数

    def __str__(self):
        return("检索序号： %s\n" 
        "书籍名称：《%s》\n" 
        "书籍类别： %s\n" 
        "简要概述： %s\n" 
        "阅读进度： %s\n" 
        "复阅评估： %s\n\n" % (self.number,self.name,self.category,
                      self.overview,self.process,self.assessment))

# 或者采用类的方法或者属性进行打印        
# 如何将数据输入进去？
# 如何多次实例化？exec()执行字符串代码动态生成变量名称---dealed
ls = 1, 'hello word', '未知', '?', '?', '?'
Book1 = Book(ls)
# 挨个传参？
print(Book1)
