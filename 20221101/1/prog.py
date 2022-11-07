class Omnibus:
	_attr_count = {}
	def __getattr__(self, attr):
		if not attr.startswith("_"):
			return len(self._attr_count[attr])
		
	def __setattr__(self, attr, val):
		self.__class__._attr_count[attr] = self.__class__._attr_count.get(attr, set())
		self.__class__._attr_count[attr].add(self)
		
	def __delattr__(self, attr):
		self.__class__._attr_count[attr] = self.__class__._attr_count.get(attr, set())
		self.__class__._attr_count[attr].add(self)
		self.__class__._attr_count[attr].remove(self)
	
import sys
exec(sys.stdin.read())
