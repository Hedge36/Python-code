from scipy import optimize
from math import atan, degrees
import numpy as np


def line(x, k, b):
    return k*x+b


p = [100, 200, 300, 400]  # kpa
R = [26.1, 38.7, 52.4, 69.9]  # 0.01mm
c = 1.574
τ = [round(c * i, 2) for i in R]  # kpa
k, C = optimize.curve_fit(line, p, τ)[0]
φ = degrees(atan(k))
τ_the = [round(p * k + C, 2) for p in p]
L = [4 - R / 100 for R in R]
print("R:", R)
print("τ:", τ)
print("τ的理论值", τ_the)
print("C值:%.2f" % C)
print("φ值:%.2f" % φ)
print("剪切位移L", L)
input()
