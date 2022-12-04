from inspect import get_annotations as ann
import types

class check(type):
	def __init__(cls, name, parents, ns, **kwds):
		def check_annotations(self):
			a = ann(self.__class__)
			for key in a:
				try:
					attr = getattr(self, key)
				except Exception:
					return False
				if callable(attr):
					continue
				if type(a[key]) == types.GenericAlias:
					attr_type = a[key].__origin__
				else:
					attr_type = a[key]
				return isinstance(attr, attr_type)
		setattr(cls, check_annotations.__name__, check_annotations)
		return super().__init__(name, parents, ns)
		
		
import sys
exec(sys.stdin.read())
