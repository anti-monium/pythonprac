s = 0
while a := input():
	a = int(a)
	if a > 0:
		s += a
	else:
		print(a)
		break
	if s > 21:
		print(s)
		break
