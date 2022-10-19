import re

w = int(input())
txt = ''
while s := input():
	txt += s.lower()
d = {}
txt = re.sub(r"[^a-z]", ' ', txt)
txt = txt.split()
for wrd in txt:
	if len(wrd) == w:
		d[wrd] = d.get(wrd, 0) + 1
d = sorted(d.items(), key=lambda x: (-x[1], x[0]))
mx = d[0][1]
print(*[p[0] for p in d if p[1] == mx]) 
