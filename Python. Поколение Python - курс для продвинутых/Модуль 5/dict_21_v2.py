class Anagram:
	def __init__(self, arr):
		print(self.__is_anagram(self.__count_chr(arr)))
		
	def __is_anagram(self, dictor):
		return 'YES' if not set(dictor) else 'NO'
		
	def __count_chr(self, arr):
		dictor = dict()
		for i in arr[0]:
			dictor[i] = dictor.get(i, 0) + 1
		for i in arr[0]:
			dictor[i] = dictor.get(i, 0) - 1
		return dictor
		
if __name__ == '__main__':
	Anagram([input().strip() for _ in range(2)])