'''
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

﻿Эквивалент на Python:

class A:
    pass

class B(A, C):
    pass

class C(A):
    pass

Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.
'''
import json

class OOP:
	def __init__(self):
		self.__dict_opp__ = dict()
		self.__dict_rev_oop__ = dict()
		
	# конвертируем словарь в вид ключ - родитель , значение дети
	def convert_and_reverse(self, arr_dict):
		for my_dict in arr_dict:
			if my_dict['name'] not in self.__dict_rev_oop__:
				self.__dict_rev_oop__[my_dict['name']] = [my_dict['name']]
			else:
				self.__dict_rev_oop__[my_dict['name']] += [my_dict['name']]
			for i in my_dict['parents']:
				if i not in self.__dict_rev_oop__:
					self.__dict_rev_oop__[i] = [my_dict['name']]
				else:
					self.__dict_rev_oop__[i] += [my_dict['name']]
		return self.__dict_rev_oop__
	
	# конвертируем словарь в вид ключ - ребенок , значение родители	
	def covert_list_to_dict_oop(self, arr_dict):
		for my_dict in arr_dict:
			self.__dict_opp__[my_dict['name']] = my_dict['parents']
		return self.__dict_opp__
	
	# Depth-First Search — Поиск вглубину (граф)	
	def dfs(self, graph, start):
	    visited, stack = [], [start]
	    while stack:
	        vertex = stack.pop()
	        if vertex not in visited:
	            visited.append(vertex)
	            stack.extend(set(graph[vertex]) - set(visited))
	    return visited

if __name__ == '__main__':
	#data_json = input()
	#data_json = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'
	#data_json = '[{"name": "A", "parents": ["B", "C", "D"]},{"name": "E", "parents": ["F", "G"]},{"name": "I", "parents": ["E", "F", "Y", "D", "G"]},{"name": "B", "parents": ["I", "Y", "D", "G"]},{"name": "F", "parents": ["D", "Z"]},{"name": "C", "parents": ["Y", "G", "Z"]},{"name": "Y", "parents": []},{"name": "D", "parents": []},{"name": "G", "parents": ["Y", "D"]},{"name": "Z", "parents": ["D", "G"]}]'
	data_json = '[{"name": "G", "parents": ["ZZZ"]}, {"name": "TH", "parents": ["ZZZ"]}, {"name": "G", "parents": ["ZY"]}, {"name": "G", "parents": ["F"]}, {"name": "A", "parents": []}, {"name": "B", "parents": ["A"]}, {"name": "C", "parents": ["A"]}, {"name": "D", "parents": ["B", "C"]}, {"name": "E", "parents": ["D"]}, {"name": "F", "parents": ["D"]}, {"name": "X", "parents": []}, {"name": "Y", "parents": ["X", "A"]}, {"name": "Z", "parents": ["X"]}, {"name": "V", "parents": ["Z", "Y"]}, {"name": "W", "parents": ["V"]}]'
	#console_out = json.dumps(data_json, indent=4, sort_keys=True)
	#print(console_out)
	#print(type(console_out))
	
	console_arr = json.loads(data_json)
	'''
	print(console_arr)
	print('--------------------------')
	print(type(console_arr))
	print(console_arr[0]["name"])
	print('--------------------------')
	'''
	oop = OOP()
	'''
	my_dict = oop.covert_list_to_dict_oop(console_arr)
	print(my_dict)
	print(oop.__dict_ans__)
	print('--------------------------')
	print(oop.dfs(my_dict, 'B'))
	print('--------------------------')
	'''
	my_dict_rev = oop.convert_and_reverse(console_arr)
	'''
	print(my_dict_rev)
	print('--------------------------')
	print(oop.dfs(my_dict_rev, 'B'))
	print('--------------------------')
	'''
	arr = [i for i in my_dict_rev.keys()]
	arr.sort()
	'''
	for i in my_dict_rev:
		size = oop.dfs(my_dict_rev, i)
		print(i, size)
		#print(f'{i} : {len(size)}')
	print('--------------------------')
	'''
	for i in arr:
		size = oop.dfs(my_dict_rev, i)
		#print(i, size)
		print(f'{i} : {len(size)}')