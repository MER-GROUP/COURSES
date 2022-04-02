class Counter:
	def __init__(self):
		self.count = 0
		
	def inc(self):
		self.count += 1
		
	def reset(self):
		self.count = 0
		
Counter
x = Counter()
print(x.count)
x.inc()
print(x.count)
Counter.inc(x)
print(x.count)
x.reset()
print(x.count)