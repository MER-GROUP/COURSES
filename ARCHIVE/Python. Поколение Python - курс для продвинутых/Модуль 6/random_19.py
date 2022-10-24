from random import uniform

class MonteCarlo:
	def __init__(self):
		self.x1 = -1
		self.x2 = 1
		self.x = int()
		self.y1 = -1
		self.y2 = 1
		self.y = int()
		self.n = 10**6
		self.So = (abs(self.x1) + abs(self.x2)) * (abs(self.y1) + abs(self.y2))
		self.r = abs(self.x1)
		print(self.square())
		
	def square(self) -> float:
		k = int()
		for _ in range(self.n):
			self.x = uniform(self.x1, self.x2)
			self.y = uniform(self.y1, self.y2)
			if 1 >= self.x**2 + self.y**2:
				k += 1
		print('k =', k)###
		print('n =', self.n)###
		print('So =', self.So)###
		return (k / self.n) * self.So
		
if __name__ == '__main__':
	MonteCarlo()