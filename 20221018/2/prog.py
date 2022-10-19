from math import *

def quit(s, a, b):
	print(s.format(a, b))

d = {}
inp = input().split(maxsplit = 1)
sm = 1
while inp[0] != "quit":
	if len(inp) > 1:
		s = [inp[0]]
		s.extend(inp[1].split())
	else:
		s = inp
	if s[0][0] == ':':
		d[s[0].replace(':', '')] = s[1:len(s)]
	else:
		args = d[s[0]][0:len(s) - 1]
		fun = d[s[0]][len(s) - 1]
		vals = {}
		for i in range(0, len(s) - 1):
			if s[i + 1][0] in "\'\"":
				vals[args[i]] = s[i + 1][1:len(s[i + 1]) - 1]
			elif '.' in s[i + 1]:
				vals[args[i]] = float(s[i + 1])
			else:
				vals[args[i]] = int(s[i + 1])
		print(eval(fun, globals(), vals))
	inp = input().split(maxsplit = 1)
	sm += 1
quit(inp[1][1:len(inp[1]) - 1], len(d) + 1, sm) 
