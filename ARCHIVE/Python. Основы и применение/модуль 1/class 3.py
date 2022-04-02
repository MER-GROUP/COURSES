class Counter:
	def __init__(self, start = 0):
		self.count = start
		
Counter
x = Counter()
print(x.count)
x.count += 1
print(x.count)

x1 = Counter(10)
print(x1.count)