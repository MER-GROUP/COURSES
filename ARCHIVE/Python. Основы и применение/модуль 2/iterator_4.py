from random import random

class RandomIterator:
	def __init__(self, k):
		self.k = k
		self.i = int()
		
	def __iter__(self):
		return self
		
	def __next__(self):
		if self.i < self.k:
			self.i += 1
			return random()
		else:
			raise StopIteration
			
def random_generator(k):
	for i in range(k):
		yield random()
			
for i in RandomIterator(5):
	print(i)
print('--------------------')
print(random_generator(5))
gen = random_generator(5)
print(type(gen))
for i in random_generator(5):
	print(i)