class Anagram2:
	def __init__(self, s1, s2):
		print(self.__is_anagram_2(self.__dic_fill(s1), self.__dic_fill(s2)))
		
	def __dic_fill(self, s):
		dictor = dict()
		for i in s:
			if i in '.,!?:;- ':
				continue
			else:
				dictor[i] = dictor.get(i, 0) + 1
		return dictor
		
	def __is_anagram_2(self, dic1, dic2):
		return 'YES' if dic1== dic2 else 'NO'
		
if __name__ == '__main__':
	Anagram2(*[input().lower() for i in range(2)])