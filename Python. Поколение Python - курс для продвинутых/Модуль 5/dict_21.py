class Anagram:
	def __init__(self, arr):
		print(self.__is_anagram(self.__count_chr(arr[0]), self.__count_chr(arr[1])))
		
	def __is_anagram(self, dic1, dic2):
		return 'YES' if dic1 == dic2 else 'NO'
		
	def __count_chr(self, s):
		dictor = dict()
		for i in s:
			dictor[i] = dictor.get(i, 0) + 1
		return dictor
		
if __name__ == '__main__':
	Anagram([input().strip() for _ in range(2)])