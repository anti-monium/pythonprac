a = input()
if (len(a) <= 2):
	quit()
a = list(a[1:len(a) - 1].split(','))
for i in range (0, len(a)):
	a[i] = int(a[i])
a = sorted(a)
print(*a, sep = ", ", end = '\n')
