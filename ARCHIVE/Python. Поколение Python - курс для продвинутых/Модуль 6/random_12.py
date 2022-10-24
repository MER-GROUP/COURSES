from random import sample

class Bingo:
	def __init__(self):
		self.bingo = [[0 for _ in range(5)] for _ in range(5)]
		self.my_range = [i for i in range(1, 76)]
		self.bingo_fill()
		self.print_bingo()
		
	def print_bingo(self):
		for i in self.bingo:
			for j in i:
				print(str(j).ljust(3), end='')
			print()
			
	def bingo_fill(self):
		arr = sample(self.my_range, 24)
		for i in range(len(self.bingo)):
			for j in range(len(self.bingo[0])):
				if 2 == i == j:
					continue
				self.bingo[i][j] = arr.pop(0)
		
if __name__ == '__main__':
	Bingo()