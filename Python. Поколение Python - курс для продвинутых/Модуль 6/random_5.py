from random import randint

class Lot:
	def __init__(self):
		lot = set()
		while 7 > len(lot):
			lot.add(randint(1, 49))
		print(*sorted(lot))
		
if __name__ == '__main__':
	Lot()