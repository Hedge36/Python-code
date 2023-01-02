from numpy import tanh, pi


def trial(h, k):
    """试算"""
    σ = 2*pi / T
    k_calculate = σ**2 / (g*tanh(k*h))
    if abs(k_calculate - k) < delta:
        c = 2 * σ / (k + k_calculate)
        L = c * T
        print("When the depth was %sm:" % h)
        print("c:%.4fm/s;\nL:%.4fm" % (c, L))
        # print("k:", (k + k_calculate)/2)
    else:
        trial(h, k_calculate)


g = 9.8     # Gravity acceleration(m/s2)
T = 9       # Period(/s)
hs = [10, 30]   # list of depth(/m)
delta = 1e-4    # Accuracy(1)

[trial(h, 1) for h in hs]
input()     # Command suspension
