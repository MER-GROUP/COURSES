class Digit:
	def __init__(self):
		pass
		
	@staticmethod
	def algo(n):
		cnt = int()
		for i in range(1, n + 1):
			for j in range(i):
				print(i, end=' ')
				cnt += 1
				if n == cnt:
					exit()
		
def main():
	Digit.algo(int(input()))
	
if __name__ == '__main__':
	main()