A = []
l = list(eval(input()))
A.append(l)
n = len(l)
for i in range(1, n):
	l = list(eval(input()))
	A.append(l)
B = []
for i in range(0, n):
	l = list(eval(input()))
	B.append(l)
C = [[0 for i in range(0, n)] for i in range(0, n)]
for i in range(0, n):
	for j in range(0, n):
		for k in range(0, n):
			C[i][j] += A[i][k] * B[k][j]
for i in range(0, n):
	print(*C[i], sep = ',')
