class Genom:
	def __init__(self):
		pass
		
	@staticmethod
	def file_read():
		s = str()
		with open('genom.txt') as f:
			s = f.read()
		return s.strip()
		
	@staticmethod
	def deshifr(s):
		i = int()
		res, abc, digit = [str()] * 3
		while True:
			if i == len(s):
				break
			elif s[i].isalpha(): 
				abc = s[i]
			else:
				if not i + 1 == len(s) and s[i + 1].isdigit():
					digit += s[i]
				else:
					digit += s[i]
					res += abc * int(digit)
					digit = str()
			i += 1
		return res
		
	@staticmethod
	def file_write(deshifr):
		with open('genom_deshifr.txt', 'w') as f:
				f.write(deshifr)
				
		
def main():
	print('hello')
	s = Genom.file_read()
	print(s)
	deshifr = Genom.deshifr(s)
	print(deshifr)
	Genom.file_write(deshifr)
	
	
if __name__ == '__main__':
	main()