class Digit:
	def __init__(self):
		pass
		
	@staticmethod
	def matrix_enter():
		arr = list()
		while True:
			s = input().split()
			if 'end' == s[0].lower():
				return arr
			arr.append(s)
			
	@staticmethod
	def matrix_out(arr):
		for i in range(len(arr)):
			for j in range(len(arr[0])):
				print(arr[i][j], end=' ')
			print()
			
	@staticmethod
	def algo(arr):
		res, line = [list() for i in range(2)]
		for i in range(len(arr)):
			for j in range(len(arr[0])):
				down = i - 1 if 0 < i else len(arr) - 1
				up = i + 1 if i < len(arr) - 1 else 0
				left = j - 1 if 0 < j else len(arr[0]) - 1
				right = j + 1 if j < len(arr[0]) - 1 else 0
				sum = int(arr[down][j]) + int(arr[up][j]) + int(arr[i][left]) + int(arr[i][right])
				line.append(sum)
			res.append(line.copy())
			line.clear()
		return res
		
def main():
	arr = Digit.matrix_enter()
	#Digit.matrix_out(arr)
	#print('---------------------------')
	Digit.matrix_out(Digit.algo(arr))
	
if __name__ == '__main__':
	main()