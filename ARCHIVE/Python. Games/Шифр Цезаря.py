##########################
class Constants:
	yes = tuple('шр')
	no = tuple('да')
##########################
# static class
class Check:
	
	@staticmethod
	def is_yes(char):
		while True:
			if char in Constants.yes:
				return True
			elif char in Constants.no:
				return False
			else:
				char = input('некоректный ввод : ')

	@staticmethod
	def is_int(digit):
		while True:
			if digit.isdigit():
				return int(digit)
			else:
				digit = input('некоректный ввод : ')
##########################
class CaesarCipher:
	
	def __init__(self):
		self.shifr = None
		self.abc = None
		self.step = None
	
	def request(self):
		self.shifr = input('шифрование или дешифрование ? (ш/д) : ')
		self.shifr = Check.is_yes(self.shifr)
		#print(self.shifr)
		self.abc = input('русский или английский алффвит ? (р/а) : ')
		self.abc = Check.is_yes(self.abc)
		#print(self.abc)
		self.step = input('шаг сдвига : ')
		self.step = Check.is_int(self.step)
		#print(self.step)
		return self.shifr, self.abc, self.step
	
	@staticmethod	
	def shifr_ru(line, step):
		line_shifr = str()
		for i in line:
			j = step
			while 0 < j:
				if ord('А') <= ord(i) <= ord('Я'):
					if 'Я' == i:
						i = 'А'
					else:
						i = chr(ord(i) + 1)
				elif ord('а') <= ord(i) <= ord('я'):
					if 'я' == i:
						i = 'а'
					else:
						i = chr(ord(i) + 1)
				j -= 1
			line_shifr += i
		return line_shifr
		
	@staticmethod	
	def shifr_eng(line, step):
		line_shifr = str()
		for i in line:
			j = step
			while 0 < j:
				if ord('A') <= ord(i) <= ord('Z'):
					if 'Z' == i:
						i = 'A'
					else:
						i = chr(ord(i) + 1)
				elif ord('a') <= ord(i) <= ord('z'):
					if 'z' == i:
						i = 'a'
					else:
						i = chr(ord(i) + 1)
				j -= 1
			line_shifr += i
		return line_shifr
		
	@staticmethod
	def de_shifr_ru(line, step):
		line_shifr = str()
		for i in line:
			j = step
			while 0 < j:
				if ord('А') <= ord(i) <= ord('Я'):
					if 'А' == i:
						i = 'Я'
					else:
						i = chr(ord(i) - 1)
				elif ord('а') <= ord(i) <= ord('я'):
					if 'а' == i:
						i = 'я'
					else:
						i = chr(ord(i) - 1)
				j -= 1
			line_shifr += i
		return line_shifr
		
	@staticmethod
	def de_shifr_eng(line, step):
		line_shifr = str()
		for i in line:
			j = step
			while 0 < j:
				if ord('A') <= ord(i) <= ord('Z'):
					if 'A' == i:
						i = 'Z'
					else:
						i = chr(ord(i) - 1)
				elif ord('a') <= ord(i) <= ord('z'):
					if 'a' == i:
						i = 'z'
					else:
						i = chr(ord(i) - 1)
				j -= 1
			line_shifr += i
		return line_shifr
	
	@staticmethod	
	def caesar(line, shifr, abc, step):
		res = str()
		if shifr:
			if abc:
				res = CaesarCipher.shifr_ru(line, step)
			else:
				res = CaesarCipher.shifr_eng(line, step)
		else:
			if abc:
				res = CaesarCipher.de_shifr_ru(line, step)
			else:
				res = CaesarCipher.de_shifr_eng(line, step)
		return res
		
	@staticmethod
	def de_shifr_eng_all_25(line, shifr, abc, step = 25):
		for i in range(1, step +1):
			print(CaesarCipher.caesar(line, shifr, abc, i))
##########################

def main():
	'''
	#line = input('введи строку для шифрования или дешифрования : ')
	#line = 'Блажен, кто верует, тепло ему на свете!'
	#line = 'To be, or not to be, that is the question!'
	#line = 'Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.'
	#line = 'Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.'
	line = 'Hawnj pk swhg xabkna ukq nqj.'
	caesar = CaesarCipher()
	shifr, abc, step = caesar.request()
	#print(caesar.caesar(line, shifr, abc, step))
	caesar.de_shifr_eng_all_25(line, shifr, abc, step)
	'''
	arr = input().split()
	arr_len = list()
	for i in range(len(arr)):
		temp = str()
		for j in arr[i]:
			if j.isalpha():
				temp += j
		arr_len.append(temp)
	arr_res = [CaesarCipher.shifr_eng(arr[i], len(arr_len[i])) for i in range(len(arr))]
	print(' '.join(arr_res))
	
main()