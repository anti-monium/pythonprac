def fib(m,  n):
	i = 0	
	cur, next = 1, 1
	while i <= n:
		if i >= m:
			yield cur
		cur, next = next, cur + next
		i += 1
		
import sys
exec(sys.stdin.read())
