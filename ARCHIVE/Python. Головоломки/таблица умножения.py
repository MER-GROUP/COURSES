class Table:
	def __init__(self):
		pass
	@staticmethod
	def enter():
		return [int(input()) for _ in range(4)]
	@staticmethod
	def mult(a, b, c, d):
		print('', end='\t')
		for i in range(c, d + 1):
			print(i, end='\t')
		print()
		for i in range(a, b + 1):
			print(i, end='\t')
			for j in range(c, d + 1):
				print(i * j, end='\t')
			print()
		
def main():
	a, b, c, d = Table.enter()
	Table.mult(a, b, c, d)
	
if __name__ == '__main__':
	main()