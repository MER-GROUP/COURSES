class Anton:
	def __init__(self, arr):
		# print(arr)
		my_list = list()
		for i in range(len(arr)):
			try:
				a = arr[i].index('a')
				n = arr[i].index('n', a + 1)
				t = arr[i].index('t', n + 1)
				o = arr[i].index('o', t + 1)
				n2 = arr[i].index('n', o + 1)
				my_list.append(i + 1)
			except ValueError:
				pass
		print(*my_list, sep=' ')
		
if __name__ == '__main__':
	arr = [input() for i in range(int(input()))]
	Anton(arr)