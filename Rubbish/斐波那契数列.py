#斐波那契数列的计算
n = eval(input('输入项数:'))
def f(n):
    if n ==1 or n == 2:
        return 1
    else:
        return f(n-1)+f(n-2)
print('斐波那契数列第{}项为{}。'.format(n,f(n)))
