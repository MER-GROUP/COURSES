class Model:
	def __init__(self):
		self.__except__ = dict()
		self.__father__ = str()
		self.__sun__ = str()
		self.__check__ = True
		self.__stack__ = list()
		
	def out(self):
		print(self.__except__)
		
	def add(self, *args):
		if 1 == len(args):
			self.__except__[args[0].strip()] = str()
		else:
			self.__except__[args[0].strip()] = args[1].strip()
			
	def add_model(self, n):
		for _ in range(n):
			arr = [i.strip() for i in input().strip().split(':')]
			self.add(*arr)
			
	def is_model(self, e):
		if 0 == len(self.__except__[e]) and self.__check__:
			return False
		elif 0 == len(self.__except__[e]):
			self.__check__ = True
			if self.__stack__.index(self.__sun__) < self.__stack__.index(e):
				return False
			else:
				return True
		else:
			if self.__check__:
				self.__sun__ = e
				self.__check__ = False
			self.__father__ = self.__except__[e]
			return self.is_model(self.__father__)
	
	def model(self, n):
		for _ in range(n):
			self.__stack__.append(input().strip())
		for i in self.__stack__:
				if self.is_model(i):
					print(i)
		
def main():
	model = Model()
	n_except = int(input())
	'''
	model.add('ArithmeticError')
	model.add('ZeroDivisionError', 'ArithmeticError')
	model.add('OSError')
	model.add('FileNotFoundError', 'OSError')
	'''
	model.add_model(n_except)
	#model.out()
	n_req = int(input())
	model.model(n_req)
	
	'''
	model.out()
	model.__stack__.extend(['ZeroDivisionError', 'OSError', 'ArithmeticError', 'FileNotFoundError'])
	print(model.__stack__)
	print(model.is_model('ZeroDivisionError'))
	print(model.is_model('OSError'))
	print(model.is_model('ArithmeticError'))
	print(model.is_model('FileNotFoundError'))
	'''
	
if __name__ == '__main__':
	main()