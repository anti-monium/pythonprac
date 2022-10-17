from fractions import Fraction

def func(s):
	def f(x):
		return Fraction(eval(s, globals(), {'x': x}))
	return f
	
inp = input().split(', ')
s = Fraction(inp[0])
inp.pop(0)
w = Fraction(inp[0])
inp.pop(0)
powA = int(inp[0])
A = inp[1:powA + 2]
powB = int(inp[powA + 2])
B = inp[powA + 3:]

sA = '('
for i in range(0, len(A)):
	A[i] = Fraction(A[i]) 
	if i > 0:
		sA += ' + '
	if powA > 0:
		sA += repr(A[i]) + ' * x ** ' + repr(powA)
	else:
		sA += repr(A[i])
	powA -= 1
sA += ')'
sB = '('
for i in range(0, len(B)):
	B[i] = Fraction(B[i]) 
	if i > 0:
		sB += ' + '
	if powB > 0:
		sB += repr(B[i]) + ' * x ** ' + repr(powB)
	else:
		sB += repr(B[i])
	powB -= 1
sB += ')'
if func(sB)(s) == Fraction('0'):
	print(False)
else:
	f = sA + ' / ' + sB
	print(func(f)(s) == w)
