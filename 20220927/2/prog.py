l = list(eval(input()))
for i in range(0, len(l) - 1):
	for j in range(i + 1, len(l)):
		if l[i] ** 2 % 100 > l[j] ** 2 % 100:
			buf = l[i]
			l[i] = l[j]
			l[j] = buf
print(l)
