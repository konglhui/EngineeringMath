# 牛顿迭代弦割法

import math


def newton_cut_iterator(x1, x0, epsion, k, max_k, f):
    x = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    if abs(x - x1) < epsion:
        return True, x
    if k > max_k:
        return False, x
    return newton_cut_iterator(x, x1, epsion, k + 1, max_k, f)


def fx(x):
    return x * x + 1000 * x - 10000


flag, x = newton_cut_iterator(-100, 100, 0.0001, 0, 500, fx)
print(flag)
print(x)
