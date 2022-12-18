class InvalidInput(Exception):
	pass
	
class BadTriangle(Exception):
	pass

def triangleSquare(x):
	try:
		(x1, y1), (x2, y2), (x3, y3) = eval(x)
	except Exception:
		raise InvalidInput('Invalid input')
	else:
		try:
			ab = (abs((x1 - x2) ** 2 + (y1 - y2) ** 2)) ** 0.5
			bc = (abs((x3 - x2) ** 2 + (y3 - y2) ** 2)) ** 0.5
			ac = (abs((x1 - x3) ** 2 + (y1 - y3) ** 2)) ** 0.5
		except Exception:
			raise BadTriangle('Not a triangle')
		else:
			if ab >= ac + bc:
				raise BadTriangle('Not a triangle')
			elif ac >= ab + bc:
				raise BadTriangle('Not a triangle')
			elif bc >= ac + ab:
				raise BadTriangle('Not a triangle')
			else:
				s = 0.5 * abs(((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)))
				if s > 0:
					return 0.5 * abs(((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)))
				else:
					raise BadTriangle('Not a triangle')

while True:
	try:
		print('%.2f' % triangleSquare(input()))
	except (InvalidInput, BadTriangle) as e:
		print(e)
	else:
		break
