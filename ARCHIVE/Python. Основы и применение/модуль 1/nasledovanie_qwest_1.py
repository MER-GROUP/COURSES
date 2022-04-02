class Model:
	def __init__(self) -> None:
		self.__base__ = dict()
		self.__stack__ = list()
		self.__check__ = True
		#self.__father__ = str()
		#self.__sun__ = str()
		
	def add(self, k , *v):
		if 0 == len(v):
			self.__base__[k] = list()
		else:
			self.__base__[k] = [v[0]]
		for i in v:
			if v[0] == i: continue
			self.__base__[k] += [i]
			
	def struct(self, n):
			key, val = [list()] * 2
			for i in range(n):
				key = input().strip().split(':')
				#print('key', key)
				if 1 < len(key):
					val = key[1].strip().split()
				#print('val', val)
				self.add(key[0].strip(), *val)
				key.clear()
				val.clear()
			
	def out(self):
		print(self.__base__)
		
	def predok(self, father, sun):
		if father == sun and sun in self.__base__.keys():
			return 'Yes'
		elif sun in self.__base__.keys():
			if self.__check__:
				#self.__father__ = father
				#self.__sun__ = sun
				self.__check__ = False
			if father in self.__base__[sun]:
				self.__check__ = True
				self.__stack__.clear()
				return 'Yes'
			else:
				self.__stack__.extend(self.__base__[sun])
				#print(self.__stack__)###
				if 0 == len(self.__stack__):
					self.__check__ = True
					self.__stack__.clear()
					return 'No'
				first = self.__stack__[0]
				del self.__stack__[0]
				return self.predok(father, first)
		else:
			return 'No'
				
	def req(self, n):
		res = list()
		for _ in range(n):
			arr = input().strip().split()
			res.append(self.predok(arr[0], arr[1]))
		print(*res, sep='\n')
		
def main() -> None:
	n_class = int(input())
	model = Model()
	'''
	model.add('g', 'f') #
	model.add('a') #
	model.add('b', 'a') #
	model.add('c', 'a') #
	model.add('d', 'b', 'c') #
	model.add('e', 'd') #
	model.add('f', 'd') #
	model.add('x') #
	model.add('y', 'x', 'a') #
	model.add('z', 'x') #
	model.add('v', 'z', 'y') #
	model.add('w', 'v') #
	'''
	model.struct(n_class)
	#model.out()
	#print(model.__base__)
	'''
	print(model.predok('a', 'g')) # yes +
	print(model.predok('a', 'z')) # no +
	print(model.predok('a', 'w')) # yes +
	print(model.predok('x', 'w')) # yes +
	print(model.predok('x', 'qwe')) # no +
	print(model.predok('a', 'x')) # no +
	print(model.predok('x', 'x')) # yes +
	print(model.predok('1', '1')) # no +
	'''
	n_req = int(input())
	model.req(n_req)
	
	#print(model.predok('a', 'b'))
	'''
	for _ in range(n_req):
		arr = input().strip().split()
		print(model.predok(arr[0].strip(), arr[1].strip()))
	'''
	
if __name__ == '__main__':
	main()