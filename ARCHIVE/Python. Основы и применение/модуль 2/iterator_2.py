from random import random

class RandomIterator:
	def __init__(self, k):
		self.k = k
		self.i = int()
	
	def __next__(self):
		if self.i < self.k:
			self.i += 1
			return random()
		else:
			raise StopIteration
			
	def __iter__(self):
		return self
	
x = RandomIterator(2)
print(next(x))
print(next(x))
#print(next(x))

print(iter(x))
print('--------------------------')
for i in RandomIterator(10):
	print(i)