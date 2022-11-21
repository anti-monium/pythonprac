alph = list('abcdefghijklmnopqrstuvwxyz')

class Alpha:
	__slots__ = [i for i in alph]
	
	def __init__(self, **kwargs):
		for key in kwargs:
			setattr(self, key, kwargs[key])
	
	def __str__(self):
		s = ''
		for ch in alph:
			try:
				s = s + ch + ': ' + str(getattr(self, ch)) + ', '
			except Exception:
				pass
		return s[:len(s) - 2]

class AlphaQ:
	def __init__(self, **kwargs):
		for key in kwargs:
			if key not in alph:
				raise AttributeError
			setattr(self, key, kwargs[key])
			
	def __setattr__(self, attr, val):
		if attr not in alph:
			raise AttributeError
		self.__dict__[attr] = val
	
	def __str__(self):
		s = ''
		for ch in alph:
			try:
				s = s + ch + ': ' + str(getattr(self, ch)) + ', '
			except Exception:
				pass
		return s[:len(s) - 2]

import sys
exec(sys.stdin.read())
