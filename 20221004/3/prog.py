def sub(a, b):
    if isinstance(a, list) or isinstance(a, tuple):
        res = []
        for obj in a:
            if obj not in b:
                res.append(obj)
    else:
        res = a - b
    if isinstance(a, tuple):
        return tuple(res)
    else:
        return res
        
       
l = eval(input())
print(sub(*l))
