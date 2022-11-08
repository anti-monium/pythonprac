from collections import UserString

class DivStr(UserString):
	def __init__(self, seq = ''):
		self.data = str(seq)
		
	
