class Model:
	def __init__(self):
		self.__except__ = dict()###
		self.__base_except__ = list()###
		self.__sun__ = str()###
		self.__check__ = True###
		self.__stack__ = list()###
		self.__base__ = dict()###
		self.__base_set__ = dict()###
		self.__sun_check__ = True###
		
		
	def out(self):
		#print(self.__except__)###
		for k, v in self.__except__.items():
			print(k, v)
			
	def out_base(self):
		for k, v in self.__base__.items():
			print(k, v)
			
	def out_base_set(self):
		for k, v in self.__base_set__.items():
			print(k, v)
		
	def add(self, *args):
		self.__except__[args[0].strip()] = list()
		for i in range(1, len(args)):
			self.__except__[args[0].strip()].append(args[i].strip())
	
	def find_father(self, sun):
		#print(self.__stack__)###
		#print(self.__base__)###
		#print(self.__base_set__)###
		if self.__sun_check__:
			self.__sun_check__ = False
			#self.__stack__.clear()
			self.__sun__ = sun
			self.__base__[self.__sun__] = list()
			self.__base_set__[self.__sun__] = set()
		'''
		if 0 == len(self.__except__[sun]) and  self.__check__:
			self.__check__ = False
			self.__base__[self.__sun__].extend([sun])
			for i in self.__base__[self.__sun__]:
				self.__base_set__[self.__sun__].add(i)
			return sun
		'''
		if 0 == len(self.__except__[sun]):
			self.__base__[self.__sun__].extend([sun])
			for i in self.__base__[self.__sun__]:
				self.__base_set__[self.__sun__].add(i)
				#return sun
			if 0 == len(self.__stack__):
				#print('end')
				self.__sun_check__ = True
				return sun
			else:
				first = self.__stack__[0]
				del self.__stack__[0]
				return self.find_father(first)
		else:
			#print('sun =', sun)###
			self.__stack__.extend(self.__except__[sun])
			self.__base__[self.__sun__].extend(self.__except__[sun])
			for i in self.__base__[self.__sun__]:
				self.__base_set__[self.__sun__].add(i)
			#print(self.__stack__)###
			first = self.__stack__[0]
			del self.__stack__[0]
			return self.find_father(first)
			
	def add_except(self, s):
		self.__base_except__.append(s)
	
	def except_error(self):
		#print(self.__base_except__)###
		#print(self.__base_set__.keys())###
		#print(self.__base_set__)###
		i = int()
		for sun in self.__base_except__:
			#print('sun base =', sun)###
			if sun not in self.__base_set__:
				#print('skip sun')###
				continue
			if 1 < self.__base_except__.count(sun):
				sun_next = int()
				for j in range(len(self.__base_except__)):
					if self.__base_except__[j] == sun:
						if i <= j:
							break
						else:
							print(sun)
							break
				continue
			iter = list(self.__base_set__.get(sun))
			#print(iter)###
			for father in iter:
				#print('sun =', sun)###
				#print('father =', father)###
				if sun in self.__base_except__ and father in self.__base_except__:
					if self.__base_except__.index(sun) <= self.__base_except__.index(father):
						continue
					else:
						print(sun)
						break
			i += 1
		
def main():
	model = Model()
	'''
	model.add('1', '2', '3', '4')
	model.add('2', '5', '3', '6', '7', '8', '9')
	model.add('5', '8')
	model.add('3', '4', '9')
	model.add('10', '7')
	model.add('4')
	model.add('6', '3', '4')
	model.add('7', '6')
	model.add('8', '10', '4', '6', '7')
	model.add('9')
	
	model.out()
	print('-----------------------------')
	print(model.find_father('1'))
	print(model.find_father('2'))
	print(model.find_father('5'))
	print(model.find_father('3'))
	print(model.find_father('10'))
	print(model.find_father('4'))
	print(model.find_father('6'))
	print(model.find_father('7'))
	print(model.find_father('8'))
	print(model.find_father('9'))
	
	print('-----------------------------')
	model.out_base()
	print('-----------------------------')
	model.out_base_set()
	
	model.add_except('6')
	model.add_except('9')
	model.add_except('4')
	model.add_except('5')
	model.add_except('10')
	model.add_except('1')
	model.add_except('3')
	model.add_except('2')
	model.add_except('8')
	model.add_except('7')
	
	print('-----------------------------')
	print(model.__base_except__)
	
	print('-----------------------------')
	model.except_error()
	
	print('-----------------------------')
	'''
	
	n_except = int(input())
	for _ in range(n_except):
		arr = input().strip().split(':')
		arr1 = [arr[0].strip()]
		#print(type(arr1))###
		arr2 = list()
		if 1 < len(arr):
			arr2 = str(arr[1]).split()
			#print(type(arr2))###
			arr = arr1 + arr2
		else:
			arr = arr1
		#print('arr', arr)###
		model.add(*arr)
	#model.out()###
	
	for i in model.__except__.keys():
		#print(i)
		model.find_father(i)
		
	n_req = int(input())
	for _ in range(n_req):
		model.add_except(input())
		
	#print('---------------------------')###
		
	model.except_error()
	
if __name__ == '__main__':
	main()