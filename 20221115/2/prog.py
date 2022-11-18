class Num:
	def __get__(self, obj, clss):
		try:
			return obj.val
		except Exception:
			obj.val = 0
			return obj.val

	def __set__(self, obj, val=0):
		if 'real' in val.__class__.__dict__:
			obj.val = val
		elif '__len__' in val.__class__.__dict__:
			obj.val = len(val)
		
	def __delete__(self, obj):
		obj.val = None
		
import sys
exec(sys.stdin.read())
