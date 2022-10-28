def fib(m,  n):
	i = 0
	count = 1
	cur, next = 1, 1
	while count <= n:
		if i >= m:
			yield cur
			count += 1
		cur, next = next, cur + next
		i += 1
		
import sys
exec(sys.stdin.read())
