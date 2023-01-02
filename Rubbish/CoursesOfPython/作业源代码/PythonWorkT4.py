#PyhthonWorkt4                      19338035黄海俊
year_pres=[1900,2000,2001,2002,2003,2004,2005]
year_pre=input("输入年份,键入回车结束:\n")
while year_pre !="": 
    year_pres.append(eval(year_pre))
    year_pre=input("输入年份,键入回车结束:\n")
print("各年份平闰年如下：")
for year in year_pres:
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{} 是世纪闰年".format(year))#整百年能被400整除的是世纪闰年
            else:
                print("{} 不是闰年".format(year))
        else:
            print("{} 是普通闰年".format(year))    #非整百年能被4整除的为普通闰年
    else:
        print("{} 不是闰年".format(year))
