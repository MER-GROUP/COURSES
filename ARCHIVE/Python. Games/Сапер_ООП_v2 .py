class Saper:
	def __init__(self):
		pass
		
	@staticmethod
	def hello():
		print('игра сапер.')
		print('введите игровое поле (n x m) и количество мин : ')
		
	@staticmethod
	def enter():
		return [int(i) for i in input().split()]
		
	@staticmethod
	def arr_init(n, m):
		return [[str('0') for _ in range(m)] for _ in range(n)]
		
	@staticmethod
	def arr_out(arr):
		for i in arr:
			for j in i:
				print(j, end=' ' * 2)
			print()
			
	@staticmethod
	def enter_k(k):
		print(f'введите {k} координат x и y : ')
		x, y = list(), list()
		for _ in range(k):
			tmp = input().split()
			x.append(int(tmp[0]))
			y.append(int(tmp[1]))
		return x, y
		
	@staticmethod
	def arr_init_mine(arr, x, y):
		for i in range(len(x)):
			arr[x[i] -1][y[i] -1] = '*'
			
	@staticmethod
	def arr_init_help(arr):
		for i in range(len(arr)):
			for j in range(len(arr[0])):
				if '0' == arr[i][j]:
					for di in range(-1, 2):
						for dj in range(-1, 2):
							if 0 <= i + di < len(arr) and 0 <= j + dj < len(arr[0]) and '*' == arr[i + di][j + dj]:
								arr[i][j] = str(int(arr[i][j]) + 1)
								
	@staticmethod
	def arr_init_dot(arr):
		for i in range(len(arr)):
			for j in range(len(arr[0])):
				if '0' == arr[i][j]:
					arr[i][j] = '.'
		
def main():
	Saper.hello()
	n, m , k = Saper.enter()
	arr = Saper.arr_init(n, m)
	Saper.arr_out(arr)
	x, y = Saper.enter_k(k)
	Saper.arr_init_mine(arr, x, y)
	Saper.arr_out(arr)
	Saper.arr_init_help(arr)
	print('------------------')
	Saper.arr_out(arr)
	print('------------------')
	Saper.arr_init_dot(arr)
	Saper.arr_out(arr)
	
if __name__ == '__main__':
	main()