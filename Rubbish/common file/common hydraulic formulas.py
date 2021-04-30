# common hydraulic formulas
from sympy import*
import math
def Hesenwillian(Q,l,C,d):
    "海曾——威廉公式：长管水头损失经验公式,其中C为系数"
    hf = 10.67 * Q **1.852 * l / C **1.852 / d**4.87


def hf(λ, l, d, v):
    "短管沿程水头损失"
    hf = λ * l * v**2 / (d * 2 * 9.8)
    return hf


def hj(ζ, v):
    "局部水头损失"
    hj = ζ * v ** 2 / 2 / 9.8
    return hj


def v(Q, d):
    "流速"
    v = 4*Q / math.pi / d ** 2
    return v


def hfl(a, l, Q):
    "长管水头损失"
    hf = a*l*Q**2
    return hf
