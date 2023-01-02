#5.26练习题1
for a in range(1,5):
       for b in range(1,5):
              for c in range(1,5):
                     if a-b!=0and b-c!=0 and a-c!=0:
                            d=100*a+10*b+c
                            print(d)
input()
