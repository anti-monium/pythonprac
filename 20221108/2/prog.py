class Undead(Exception):
	pass
	
class Skeleton(Undead):
	pass

class Zombie(Undead):
	pass

class Ghoul(Undead):
	pass

def necro(a):
	match a % 3:
		case 0:
			raise Skeleton('Skeleton')
		case 1:
			raise Zombie('Zombie')
		case 2:
			raise Ghoul('Generic Undead')
			
inp = eval(input())
for i in range(inp[0], inp[1]):
	try:
		necro(i)
	except Undead as e:
		print(e)
