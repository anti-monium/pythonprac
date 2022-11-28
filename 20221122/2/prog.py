s = input()
while inp := input():
	s += '\n' + inp
s_new = s.encode('latin1', errors='replace').decode('cp1251', errors='replace')
print(s_new)
