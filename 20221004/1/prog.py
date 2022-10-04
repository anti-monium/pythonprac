def binsrch(a, s):
    mb_a_idx = len(s) // 2
    res = False
    if len(s) == 0:
        return res
    if s[mb_a_idx] == a:
        res = True
    elif s[mb_a_idx] > a:
        res = binsrch(a, s[:len(s) // 2])
    else:
        res = binsrch(a, s[len(s) // 2 + 1:])
    return res
    
l = eval(input())
print(binsrch(l[0], l[1]))
