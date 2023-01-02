# 大物实验5玻尔振动数据分析
"""
Created on Fri Nov 13 08:31:22 2020

@author: Hedge
"""
cmc = __import__("common math calculate")

def experiment1():
    θ = [10*i for i in range(1,9+1)]
    β = [0.0357, 0.0193, 0.0159, 0.0134, 0.0107,
         0.0104, 0.00893, 0.00782, 0.00781]
    k, d = cmc.liner_fitting(θ,β)
    print('阻尼系数与扭摆初始释放角度关系为β = %.5fθ + %.5f'%(k, d))
    cmc.Least_squares(θ,β)
    
def experiment2():
    V = [1, 3, 5, 7, 8]
    β = [0.015, 0.026, 0.048, 0.081,0.112]
    cmc.smooth_curve(V,β,'','V','β')
    
def experiment3():
    pass 
    
#experiment1()
experiment2()
#experiment3()