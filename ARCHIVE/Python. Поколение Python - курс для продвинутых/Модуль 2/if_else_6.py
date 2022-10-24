class Digit:
	def __init__(self, arr):
		ans = arr.pop()
		# print(arr)
		inx = int()
		res = False
		for i in arr:
			for j in range(len(arr)):
				if inx == j:
					continue
				elif ans == i * arr[j]:
					res = True
					break
			if res: break
			inx += 1
		
		if res: print('ДА')
		else: print('НЕТ')
		
if __name__ == '__main__':
	Digit(list(map(int, [input() for _ in range(int(input()) + 1)])))