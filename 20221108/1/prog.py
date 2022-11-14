from collections import UserString

class DivStr(UserString):
	def __init__(self, seq = ''):
		self.data = str(seq)
	
	def __floordiv__(self, n):
		ans = []
		ln = len(self.data) // n
		for i in range(0, n):
			ans.append(DivStr(self.data[ln * i:ln * (i + 1)]))
		return (ans)
	
	def __mod__(self, n):
		return DivStr(self.data[len(self.data) // n * n:])
	
import sys
exec(sys.stdin.read())
