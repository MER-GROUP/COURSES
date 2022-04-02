class Replace:
	def __init__(self):
		pass
		
	def replace(self, s, a, b):
		count = int()
		while True:
			s1 = s.replace(a, b)
			#print(s1)
			count += 1
			if a not in s:
				return 0
			elif a not in s1:
				return 'Impossible' if 1000 < count else count
			elif 1000 < count:
				return 'Impossible'
			s = s1

if __name__ == '__main__':
	def main():
		s, a, b = (input() for i in range(3))
		#print(s.replace.__doc__)
		rep = Replace()
		count = rep.replace(s, a, b)
		print(count)
	main()