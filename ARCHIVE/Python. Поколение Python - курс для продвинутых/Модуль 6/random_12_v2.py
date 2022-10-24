from random import sample

class Bingo:
	def __init__(self):
		self.bingo = list()
		self.my_range = [i for i in range(1, 76)]
		self.bingo_fill()
		self.print_bingo()
		
	def print_bingo(self):
		for i in self.bingo:
			for j in i:
				print(str(j).ljust(3), end='')
			print()
			
	def bingo_fill(self):
		arr = sample(self.my_range, 25)
		self.bingo = [arr[i : i + 5] for i in range(0, 21, 5)]
		self.bingo[2][2] = 0
		
if __name__ == '__main__':
	Bingo()