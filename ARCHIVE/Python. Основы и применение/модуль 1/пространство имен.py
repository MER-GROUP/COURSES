class Namespase:
	def __init__(self) -> None:
		self.__nspace__ = {'global' : {'None' : list()}}
		
	def enter(self, n):
		arr = list()
		for i in range(n):
			tmp = input().split()
			arr.append(tmp.copy())
			tmp.clear()
		return arr
		
	def output(self) -> None:
		print(self.__nspace__)
		
	def create(self, nspace, parent):
		self.__nspace__[nspace] = {parent : list()}
		
	def add(self, nspace, var):
		tmp = self.__nspace__[nspace]
		for v in tmp.values():
			v.append(var)
			
	def get(self, nspace, var):
		for k, v in self.__nspace__[nspace].items():
			if var in v:
				return nspace
			elif 'global' == nspace and var not in v:
				return None
			else:
				return self.get(k, var)
				
	def request(self, arr):
		for i in arr:
			if 'create' == i[0].lower():
				self.create(i[1], i[2])
			elif 'add' == i[0].lower():
				self.add(i[1], i[2])
			else:
				print(self.get(i[1], i[2]))
		
def main() -> None:
	n = int(input())
	namespase = Namespase()
	arr = namespase.enter(n)
	#print(arr)
	namespase.request(arr)
	'''
	namespase.output()
	namespase.create('foo()', 'global')
	namespase.output()
	namespase.create('bar()', 'foo()')
	namespase.output()
	namespase.create('red()', 'global')
	namespase.output()
	namespase.add('global', 'a')
	namespase.output()
	namespase.add('global', 'z')
	namespase.output()
	namespase.add('foo()', 'b')
	namespase.output()
	namespase.add('bar()', 'a')
	namespase.output()
	print(namespase.get('foo()', 'a'))
	print(namespase.get('foo()', 'c'))
	print(namespase.get('bar()', 'a'))
	print(namespase.get('bar()', 'b'))
	'''
	
if __name__ == '__main__':
	main()