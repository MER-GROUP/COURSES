class MyList(list):
	def even_len(self):
		return 0 == len(self) % 2
		
x = MyList()
print(x)
print(x.even_len())
x.extend([1, 2, 3, 4, 5])
print(x)
print(x.even_len())
x.append(6)
print(x)
print(x.even_len())