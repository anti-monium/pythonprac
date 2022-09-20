a = int(input())
if a % 2 == 0 and a % 25 == 0:
	print("A + B -", end = " ")
elif a % 2 != 0 and a % 25 == 0:
	print("A - B +", end = " ")
else:
        print("A - B -", end = " ")
if a % 8 == 0:
	print("C +")
else:
	print("C -")
