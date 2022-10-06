from math import *

def Calc(s, t, u):
    def func_s(x):
        return eval(s, globals(), {"x": x})
    def func_t(x):
        return eval(t, globals(), {"x": x})
    def func(x):
        return eval(u, globals(), {"x": func_s(x), "y": func_t(x)})
    return func
    
    
l = eval(input())
x = eval(input())
print(Calc(*l)(x))
