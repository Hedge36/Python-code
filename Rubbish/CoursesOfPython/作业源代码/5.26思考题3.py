#5.26练习题3——税前收入计算
#税前收入=(税后收入-对应阈值*纳税比率+速算扣除数)/(1-纳税比率)
after=-50000
for i in range(5):
    after=after+100000
    def income():
        if after <= 34920:
            income=after/0.97
        elif after <= 130680:
            income=(after+2520-36000*0.1)/0.9
        elif after <= 251880:
            income=(after+16920-144000*0.2)/0.8
        elif after <= 358080:
            income=(after+31920-300000*0.25)/0.75
        elif after <= 535050:
            income=(after+52950-420000*0.3)/0.7
        elif after <= 769080:
            income=(after+85920-660000*0.35)/0.65
        else :
            income=(after+181920-960000*0.45)/0.55
        return income
    print("当税后年收入为{:.0f}时，税前年收入为{:.0f}。".format(after,income()))
    
