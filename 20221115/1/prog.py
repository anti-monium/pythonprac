def objcount(clss):
	clss.counter = 0
	def i(*x):
		pass
	def d(x):
		pass
	if '__init__' in clss.__dict__:
		i = clss.__init__
	if '__del__' in clss.__dict__:
		d = clss.__del__
	def _init_(self, args = None):
		clss.counter += 1
		try:
			if args == None:
				i(self)
			else:
				i(self, *args)
		except Exception:
			pass
	
	def _del_(self):
		clss.counter -= 1
		try:
			d(self)
		except Exception:
			pass
			
	clss.__init__ = _init_
	clss.__del__ = _del_
			
	return clss
			
import sys
exec(sys.stdin.read())
