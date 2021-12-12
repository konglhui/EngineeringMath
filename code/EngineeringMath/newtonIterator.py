# 牛顿迭代法

import math

def newton_iterator(x0, epsion, f, df,k,maxk):
    df_x = df(x0)
    if(df_x == 0):
        return False, 0
    x1 = x0 - f(x0)/df_x
    if(abs(x1 - x0) < epsion):
        return True, x1
    if(k > maxk):
        return False,0
    return newton_iterator(x1, epsion, f, df,k+1,maxk)

def fx(x):
    return x * x + 1000 * x +10000
def dfx(x):
    return 2 * x +1000

flag,val = newton_iterator(10000,0.000001,fx,dfx,1,100)
print(flag)
print(val)

 
