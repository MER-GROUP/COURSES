import re

class Anton:
	def __init__(self, arr):
		virus= 'anton'
		for i in range(len(arr)):
			x = int()
			for j in arr[i]:
				if j == virus[x]:
					x += 1
				if 5 == x:
					print(i + 1, end=' ')
					break
		
if __name__ == '__main__':
	arr = [input() for i in range(int(input()))]
	Anton(arr)