from functools import wraps

def dec(fun):
	@wraps(fun)
	def print_fun(self, *args, **kwargs):
		print(f'{print_fun.__name__}: {args}, {kwargs}')
		return fun(self, *args, **kwargs)
	return print_fun

class dump(type):
	def __init__(cls, name, parents, ns, **kwds):
		for key in ns:
			if callable(ns[key]):
				setattr(cls, key, dec(ns[key]))
		return super().__init__(name, parents, ns)
        

import sys
exec(sys.stdin.read())
