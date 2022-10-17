l = []
num_g = 0
num_w = 0
s = input()
l.append(list(s))
while s := input():
	l.append(list(s))	
	if '.' in s:
		num_g += len(s) - 2
	if '~' in s:
		num_w += len(s) - 2
	if '##' in s:
		break
ans = [['.' for i in range(0, len(l))] for j in range(0, len(l[0]))]
for i in range(0, len(ans)):
	if i == 0 or i == len(ans) - 1:
		for j in range(0, len(ans[i])):
			ans[i][j] = '#'
	else:
		ans[i][0] = '#'
		ans[i][len(ans[i]) - 1] = '#'
count_w = 0
for i in range(len(ans) - 2, 0, -1):
	if count_w >= num_w:
		break
	for j in range(1, len(ans[i]) - 1):
		ans[i][j] = '~'
		count_w += 1
		if count_w == num_w:
			break
	if ans[i][len(ans[i]) - 2] == '.':
		for j in range(1, len(ans[i]) - 1):
			if ans[i][j] == '.':
				count_w += 1
			ans[i][j] = '~'
for l in ans:
	print(*l, sep = '')
v = (len(ans) - 2) * (len(ans[0]) - 2)
s_g = repr(v - count_w) + '/' + repr(v)
s_w = repr(count_w) + '/' + repr(v)
if v - count_w > count_w:
	max_s = len(s_g)
	prp = round(20 * count_w / (v - count_w))
	d_g = '.' * 20
	d_w = '~' * prp + ' ' * (20 - prp)
else:
	max_s = len(s_w)
	prp = round(20 * (v - count_w) / count_w)
	d_g = '.' * prp + ' ' * (20 - prp)
	d_w = '~' * 20
print(d_g, s_g.rjust(max_s))
print(d_w, s_w.rjust(max_s))















