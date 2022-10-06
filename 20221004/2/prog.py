def Pareto(*s):
    ans = []
    for pair in s:
        for p in s:
            if pair[0] <= p[0] and pair[1] <= p[1] and (pair[0] < p[0] or pair[1] < p[1]):
                break
        else:
            ans.append(pair)
    return tuple(ans)
    
    
tpl = eval(input())
print(Pareto(*tpl))
