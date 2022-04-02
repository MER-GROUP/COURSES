import sys
from random import random

class  RandomIterator:
	'''
	RandomItetator - class for random num
	return int nums
	'''
	def __init__(self, k):
		self.k = k
		self.i = int()
		
	def __next__(self):
		if self.i < self.k:
			self.i += 1
			return int(random() * 6)
		else:
			raise StopIteration
			
	def __iter__(self):
		return self
		
if __name__ == '__main__':
	ri = RandomIterator(10)
	for i in ri:
		print(i, end=' ')
	print()
	print(ri.__doc__)

	print(sys.__doc__)
	print('------------------')
	print(sys.getrefcount.__doc__)