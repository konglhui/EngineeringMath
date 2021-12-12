# 简单迭代法

def easy_iterator(x0, epsion, g):
    x1 = g(x0)
    x2 = g(x1)
    if(abs(x2 - x1) < epsion):
        return True, x1
    if(abs(x2 - x1) > abs(x1 - x0)):
        return False, 0
    return easy_iterator(x1, epsion, g)


def test_func(x):
    return pow(x+1, 1/3)

flag,x0  = easy_iterator(1000,0.000001,test_func)
print(flag)
print(x0)