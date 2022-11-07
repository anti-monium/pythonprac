def inter(a1, a2, a3, a4):
	z = (a4[1] - a3[1])*(a2[0] - a1[0]) - (a4[0] - a3[0])*(a2[1] - a1[1])
	if not z:
		return False
	ch1 = (a4[0] - a3[0])*(a1[1] - a3[1]) - (a4[1] - a3[1])*(a1[0] - a3[0])
	ch2 = (a2[0] - a1[0])*(a1[1] - a3[1]) - (a2[1] - a1[1])*(a1[0] - a3[0])
	u1 = ch1 / z
	u2 = ch2 / z
	if u1 >= 0 and u1 <= 1 and u2 >= 0 and u2 <= 1:
		return True
	return False
	
def inside(dot, tr):
	ans1 = ((tr[0][0] - dot[0]) * (tr[1][1] - tr[0][1]) - (tr[1][0] - tr[0][0]) * (tr[0][1] - dot[1]))
	ans2 = ((tr[1][0] - dot[0]) * (tr[2][1] - tr[1][1]) - (tr[2][0] - tr[1][0]) * (tr[1][1] - dot[1]))
	ans3 = ((tr[2][0] - dot[0]) * (tr[0][1] - tr[2][1]) - (tr[0][0] - tr[2][0]) * (tr[2][1] - dot[1]))
	if ans1 > 0 and ans2 > 0 and ans3 > 0:
		return True
	if ans1 < 0 and ans2 < 0 and ans3 < 0:
		return True
	if not ans1 * ans2 * ans3:
		return True
	return False

class Triangle:
	def __init__(self, a, b, c):
		self.tr = (a, b, c)
		self.ab = (abs((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)) ** 0.5
		self.bc = (abs((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2)) ** 0.5
		self.ac = (abs((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2)) ** 0.5
		
	def __abs__(self):
		if self.ab >= self.ac + self.bc:
			return 0
		elif self.ac >= self.ab + self.bc:
			return 0
		elif self.bc >= self.ac + self.ab:
			return 0
		else:
			return 0.5 * abs(((self.tr[1][0] - self.tr[0][0]) * (self.tr[2][1] - self.tr[0][1]) - 
				(self.tr[2][0] - self.tr[0][0]) * (self.tr[1][1] - self.tr[0][1])))
				
	def __bool__(self):
		return bool(abs(self))
	
	def __lt__(self, other):
		return abs(self) < abs(other)
		
	def __contains__(self, other):
		if not abs(other):
			return True
		return inside(other.tr[0], self.tr) and inside(other.tr[1], self.tr) and inside(other.tr[2], self.tr)
		
	def __and__(self, other):
		if not abs(self) or not abs(other):
			return False
		if self in other or other in self:
			return True
		if inter(self.tr[0], self.tr[1], other.tr[0], other.tr[1]):
			return True
		if inter(self.tr[0], self.tr[1], other.tr[0], other.tr[2]):
			return True
		if inter(self.tr[0], self.tr[1], other.tr[1], other.tr[2]):
			return True
		if inter(self.tr[0], self.tr[2], other.tr[0], other.tr[1]):
			return True
		if inter(self.tr[0], self.tr[2], other.tr[0], other.tr[2]):
			return True
		if inter(self.tr[0], self.tr[2], other.tr[2], other.tr[1]):
			return True
		if inter(self.tr[2], self.tr[1], other.tr[0], other.tr[1]):
			return True
		if inter(self.tr[2], self.tr[1], other.tr[0], other.tr[2]):
			return True
		if inter(self.tr[2], self.tr[1], other.tr[1], other.tr[2]):
			return True
		return False
			
import sys
exec(sys.stdin.read())
	
	
	

	
	
	
