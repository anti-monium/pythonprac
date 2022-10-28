import itertools as itt

def slide(seq, n):
	i = 0
	while True:
		#print(f"_{i}_{i+n}_", end = '')
		yield from itt.islice(seq, n)
		i += 1
		
def fib():
	cur, next = 1, 1
	while True:
		yield cur
		cur, next = next, cur + next

i = slide(fib(), 3)
s = next(i)
while s <= 22:
	print(s, end=' ')
	s = next(i)
print()
