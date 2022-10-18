s = input().lower()
uniq = set()
for i in range(0, len(s) - 1):
	if s[i].isalpha() and s[i + 1].isalpha():
		uniq.add(str(s[i]) + str(s[i + 1]))
print(len(uniq))
