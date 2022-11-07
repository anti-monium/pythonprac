class Grange:
	def __init__(self, b0, q, bn):
		i = b0
		self.b0 = b0
		self.q = q
		self.bmax = bn
		self.l = []
		while i < bn:
			self.l.append(i)
			i *= q
	
	def __len__(self):
		return len(self.l)
		
	def __bool__(self):
		return bool(len(self.l))
		
	def __getitem__(self, idx):
		if isinstance(idx, slice):
			if idx.step is None:
				step = self.q
			else:
				step = self.q ** idx.step
			return Grange(idx.start, step, idx.stop)
		else:
			return self.b0 * self.q ** idx
		
	def __iter__(self):
		return iter(self.l)
		
	def __str__(self):
		return f"grange({self.b0}, {self.q}, {self.bmax})"
		
	def __repr__(self):
		return f"grange({self.b0}, {self.q}, {self.bmax})"
		
import sys
exec(sys.stdin.read())
