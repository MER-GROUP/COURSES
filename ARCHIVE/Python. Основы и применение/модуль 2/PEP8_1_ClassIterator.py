# итератор и генератор
from random import randint

class RandomIterator:
	def __init__(self, k):
		self.k = k
		self.i = int()
		
	def __iter__(self):
		return self
		
	def __next__(self):
		if self.i < self.k:
			self.i += 1
			return randint(1, 10)
		else:
			raise StopIteration
			
def RangonGenerator(k):
			for i in range(k):
				yield randint(10, 20)
			
ri = RandomIterator(5)
for i in ri:
	print(i)
print('**********')
for i in RangonGenerator(5):
	print(i)