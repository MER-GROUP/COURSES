#from accessify import private

#############################
class Digit:
	
	__sys16_10 = {'A' : '10', 'B' : '11', 'C' : '12', 'D' : '13', 'E' : '14', 'F' : '15'}	
	__sys10_16 = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
	#__sys = list('ABCDEF')
	
	def __init__(self):
		self.digit = None
		self.base = None
	
	@staticmethod
	#@private
	def __info_digit_pow__(digit):
		arr = list()
		for i in range(len(digit) -1, 0, -1):
			arr.append(i)
			#print(i)
		arr.append(0)
		return arr
		
	#@staticmethod
	#@private
	def __info_digit_base__(self, digit):
		res = list()
		for i in digit:
			if i.isdigit():
				res.append(i)
				continue
			else:
				res.append(self.__sys16_10.get(i.upper()))
		return res
		
	#@staticmethod
	#@private
	def __info_digit_base_10_16__(self, digit):
		res = list()
		for i in digit:
			if not i in (range(10, 17)):
				res.append(i)
				continue
			else:
				res.append(self.__sys10_16.get(i))
		return res
	
	def request(self):
		self.base = input('введите основание системы счисления : ')
		self.digit = input(f'введи число по основанию {self.base} : ')
		return self.base, self.digit
	
	#@staticmethod
	def digit_convert_to_10(self, digit, base):
		res = int()
		arr_digit = self.__info_digit_base__(digit)
		arr_pow = self.__info_digit_pow__(digit)
		for i in range(len(arr_digit)):
			res += int(arr_digit[i]) * int(base) ** arr_pow[i]
			#print('res =', res)
		#print(arr_digit)
		#print(arr_pow)
		#print('base =', base)
		return res
		
	#@staticmethod
	def digit_10_convert_to_all(self, digit, base):
		digit, base = int(digit), int(base)
		res = list()
		while True:
			otv = digit // base
			if 0 >= otv: 
				res.append(digit)
				break
			znach = otv * base
			res.append(digit - znach)
			digit = otv
		res.reverse()
		res = self.__info_digit_base_10_16__(res)
		res = [str(i) for i in res]
		return ''.join(res)
#############################
def main():
	class_digit = Digit()
	
	# test 1
	'''
	base, digit = class_digit.request()
	#print(Digit.__info_digit_pow__(digit))
	print(class_digit.digit_convert_to_10(digit, base))
	#print(int('1011', 2))
	'''
	# test 2
	'''
	sad = str(88)
	aplle = str(32)
	grusha = str(22)
	sliva = str(16)
	vishnja = str(17)
	base = 17
	#print(aplle + grusha + sliva + vishnja)
	for i in range(base):
		x = class_digit.digit_convert_to_10(sad, str(i))
		y = class_digit.digit_convert_to_10(aplle, str(i))
		z = class_digit.digit_convert_to_10(grusha, str(i))
		w = class_digit.digit_convert_to_10(sliva, str(i))
		v = class_digit.digit_convert_to_10(vishnja, str(i))
		if x == y + z + w + v:
			print('base =', i)
			print(f'{x} = {y} + {z} + {w} + {v}')
			print(f'{x} = {y + z + w + v}')
			break
	'''
	# test 3
	'''
	print(class_digit.digit_10_convert_to_all(428, 16))
	print(class_digit.digit_10_convert_to_all(125, 8))
	print(class_digit.digit_10_convert_to_all(25, 2))
	print(class_digit.digit_10_convert_to_all(1000, 16))
	print(hex(1000))
	print(class_digit.digit_10_convert_to_all(513, 2))
	'''
	# test 4
	digit = input()
	print(class_digit.digit_10_convert_to_all(digit, 2))
	print(class_digit.digit_10_convert_to_all(digit, 8))
	print(class_digit.digit_10_convert_to_all(digit, 16))

if __name__ == '__main__':
	main()
#############################