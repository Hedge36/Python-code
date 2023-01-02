#5.26练习题2——税后收入计算
#税后收入=税前收入-(税前收入-对应阈值)*纳税比率-速算扣除数
income=-50000
for i in range(5):
    income=income+100000
    def tax():
        if income <= 36000:
            tax=income*0.03
        elif income <= 144000:
            tax=(income-36000)*0.1+2520
        elif income <= 300000:
            tax=(income-144000)*0.2+16920
        elif income <= 420000:
            tax=(income-300000)*0.25+31920
        elif income <= 660000:
            tax=(income-420000)*0.3+52950
        elif income <= 960000:
            tax=(income-660000)*0.35+85920
        else :
            tax=(income-960000)*0.45+181920
        tax=income-tax
        return tax
    print("当税前年收入为{:.0f}时，税后年收入为{:.0f}。".format(income,tax()))
    
