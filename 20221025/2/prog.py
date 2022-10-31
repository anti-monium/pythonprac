import itertools as itt

def slide(seq, n):
	i = 0
	while True:
		seq, new = itt.tee(seq)
		ans = itt.islice(new, i, n + i)
		ch, ans = itt.tee(ans)
		if len(list(ch)) > 0:
			i += 1
			yield from ans
		else:
			break
		

import sys
exec(sys.stdin.read())
