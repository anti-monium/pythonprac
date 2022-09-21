N = int(input())
i = N
while i <= N + 2:
	j = N
	while j <= N + 2:
		print(i, "*", j, "=", sep = " ", end = " ")
		p = i * j
		s = 0
		while p > 0:
			s = s + p % 10
			p = p // 10
		if s == 6:
			print(":=)", end = "")
		else:
			print(i * j, end = "")
		if j == N + 2:
			print("\n", end = "")
		else:
			print(" ", end = "")
		j += 1
	i += 1
