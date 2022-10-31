'''
Берете первую половину слова, по буквам в цикле сравниваете с развернутой второй половиной слова. Считаете сколько раз не совпало. Если ровно одно несовпадение, то это почтиполиндром.
'''

from string import ascii_lowercase

class Algo:
	def __init__(self, s):
		if 1000 > len(s):
			print(self.__algo_slow(s))
		else:
			print(self.__algo_fast(s))
		
	def __algo_fast(self, s):
		arr = [i for i in s if i in ascii_lowercase]
		check = int()
		i = int()
		j = len(arr) - 1
		while i <= j:
			if not arr[i] == arr[j]:
				check += 1
				if 1 < check:
					return False
			i += 1
			j -= 1
		return True
		
	def __algo_slow(self, s):
		arr = [i for i in s if i in ascii_lowercase]
		for i in range(len(arr)):
			tmp = arr.copy()
			del tmp[i]
			if tmp == tmp[: : -1]:
				return True
		return False
		
if __name__ == '__main__':
	Algo(input())