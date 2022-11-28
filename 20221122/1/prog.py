import sys

s = sys.stdin.buffer.read()
N = s[0]
sys.stdout.buffer.write(s[0:1])
s = s[1:]
l = len(s)
s_new = []
for i in range(N):
	s_new.append(s[i * l // N:(1 + i) * l // N])
for b in sorted(s_new):
	sys.stdout.buffer.write(b)
