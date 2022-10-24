import re

class Anton:
	def __init__(self, arr):
		# print(arr)
		my_list = list()
		pattern = r'.*a.*n.*t.*o.*n.*'
		#pattern = r'\w*a\w*n\w*t\w*o\w*n\w*'
		for i in range(len(arr)):
			if re.search(pattern, arr[i]):
				my_list.append(i + 1)
		print(*my_list, sep=' ')
		
if __name__ == '__main__':
	arr = [input() for i in range(int(input()))]
	Anton(arr)