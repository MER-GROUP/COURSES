class Reshka:
	def __init__(self, s):
		arr = s.split('О')
		print(len(max(arr)))
		
if __name__ == '__main__':
	Reshka(input().strip())