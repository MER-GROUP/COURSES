class Square:
	def __init__(self):
		pass
	@staticmethod
	def enter(s):
		if 'треугольник' in s:
			return [float(input()) for _ in range(3)]
		elif 'прямоугольник' in s:
			return [float(input()) for _ in range(2)]
		elif 'круг' in s:
			return float(input())

	@staticmethod
	def square(s):
		if 'треугольник' in s:
			p = (a + b + c) / 2
			return (p * (p - a) * (p - b) * (p - c)) ** 0.5
		elif 'прямоугольник' in s:
			return a * b
		elif 'круг' in s:
			return pi * r ** 2

def glo():
	global a, b, c, r
	a, b, c, r = [None] * 4
	global pi
	pi = 3.14
			
def main():
	global a, b, c, r
	room = input().lower()
	if 'треугольник' in room:
		a, b, c = Square.enter(room)
		print(Square.square(room))
	elif 'прямоугольник' in room:
		a, b = Square.enter(room)
		print(Square.square(room))
	elif 'круг' in room: 
		r = Square.enter(room)
		print(Square.square(room))
	
if __name__ == '__main__':
	glo()
	main()