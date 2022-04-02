# испрльзование метода супер класса и перегрузка метода супер класса
class EvenLenghtMixin():
	def even_len(self):
		return 0 == len(self) % 2

class MyList(list, EvenLenghtMixin):
	def pop(self):
		x = super(MyList, self).pop()
		print('Last value is', x)
		return x
	
	def sort(self):
		print('overload')
		
x = MyList()
print(x)
print(x.even_len())
x.extend([1, 2, 3, 4, 5])
print(x)
print(x.even_len())
x.append(6)
print(x)
print(x.even_len())
print('--------------------')
y = x.pop()
print(y)
print(x)
x.sort()