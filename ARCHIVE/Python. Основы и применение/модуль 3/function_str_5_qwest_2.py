class Find:
	def __init__(self):
		pass
		
	def find(self, s, f):
		count, i = int(), int()
		while True:
			i = s.find(f, i) + 1
			if i:
				count += 1
			else:
				break
		'''
		for i in range(len(s)):
			if s[i : ].startswith(f):
				count += 1
		'''
		return count
		
if __name__ == '__main__':
	def main():
		s, f = (input() for i in range(2))
		find = Find()
		print(find.find(s, f))
		
	main()