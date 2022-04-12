class Algo:
	def __init__(self, s):
		print(self.__algo3(s))

	def __algo(self, s):
		text = ''.join(filter(str.isalpha, s))
		for i in set(text):
			if text.count(i) == 1:
				text = text.replace(i, '')
				break
		return text == text[::-1]

	def __algo2(self, s):
		n = [i.lower() for i in s if i.isalpha() == True]
		counter = 0
		flag = False
		# a = []
		# b = []
		while len(n) > 1:
			if n[0] == n[-1]:
				# a.append(n[0])
				# b.append(n[-1])
				del n[0]
				del n[-1]
			else:
				counter += 1
				if n[0] == n[-2]:
					del n[-1]
				elif n[-1] == n[1]:
					del n[0]
			if counter > 1:
				# print(a)
				# print(b)
				return False
		return True
		
	def __algo3(self, s):
		s = [elem for elem in s if elem.isalpha()]
		mistake = 0
		for i in range(len(s)-1):
			if mistake > 1:
				break
			if s[i] != s[-i-1]:
				if s[i] == s[-i-2]:
					s.pop(-i-1)
				else:
					s.pop(i)
				mistake += 1
		return mistake <= 1
		
if __name__ == '__main__':
	Algo(input())
	# 14&*@(a)!(@14112)!@$)!@*$!*a)$*099 
	# True