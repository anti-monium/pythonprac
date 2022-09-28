M, N = eval(input())
print ([x for x in range(M, N) if x != 1 and all([x % i != 0 for i in range(2, int(x ** 0.5) + 1)])])
