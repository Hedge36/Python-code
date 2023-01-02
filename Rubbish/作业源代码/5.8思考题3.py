#思考题3
for a in range(1,5):
       for b in range(1,5):
           for c in range(1,5):
                  if a-b!=0and b-c!=0 and a-c!=0:
                         print(100*a+10*b+c)
input()
