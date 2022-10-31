# авторский алгоритм от BEEGIK
class Algo:
	def __init__(self, s1, s2):
		self.__algo(s1, s2)
		
	# Способ 1. Используем встроенную функцию sorted().
	def __algo(self, s11, s22):
		s1 = sorted(s11)
		s2 = sorted(s22)
		i, n = 0, len(s1)
		while i < n and s1[i] == s2[i]:
			i += 1
		return s2[i]

	# Способ 2. Используем словари (тип dict).
	def __algo2(self, s1, s2):
		dict1, dict2 = {}, {}
		for char in s1:
			dict1[char] = dict1.get(char, 0) + 1
		for char in s2:
			dict2[char] = dict2.get(char, 0) + 1
		for char in dict2:
			if char not in dict1 or dict1[char] != dict2[char]:
				return char

	# Способ 3. Используем тип данных Counter, импортируемый из collections.
	def __algo3(self, s1, s2):
		from collections import Counter
		dict1 = Counter(input())
		dict2 = Counter(input())
		dict2.subtract(dict1)
		return dict2.most_common(1)[0][0]
		
if __name__ == '__main__':
	Algo(input(), input())