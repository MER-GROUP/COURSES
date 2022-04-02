class MySet:
	def __init__(self, s):
		arr = [i.strip('.,;:-?!') for i in s.lower().split()]
		print(len(set(arr)))
		
if __name__ == '__main__':
	MySet(input())