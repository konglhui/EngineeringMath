# 二分法代码

import math


def dichotomy(a, b, epsion, f):
    ya = f(a)
    yb = f(b)
    if(ya * yb > 0):
        return False, 0, 0
    if ya * yb == 0:
        if(ya == 0):
            return True, a, ya
        else:
            return True, b, yb
    x0 = (a+b)/2
    y0 = f(x0)
    if(y0 == 0 or abs(b-a) < epsion):
        return True, x0, y0
    elif(ya * y0 < 0):
        return dichotomy(a, x0, epsion, f)
    else:
        return dichotomy(x0, b, epsion, f)


def testFunc(x):
    return math.sin(x) - x * x / 4


flag, x0, y0 = dichotomy(1, 5, 0.0001, testFunc)

print(flag, x0, y0)
