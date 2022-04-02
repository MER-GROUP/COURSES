import numpy as np

# создаем матрицу
class Matrix:
	def __init__(self, n, m):
		self.arr = [list(map(int, input().split())) for _ in range(n)]
		
if __name__ == '__main__':
	# создаем матрицу n * m
	x = Matrix(*list(map(int, input().split())))
	y = Matrix(*list(map(int, input().split())))
	# конвертииуем в numpy
	x_np = np.matrix(x.arr)
	y_np = np.matrix(y.arr)
	# выводи numpy матрицы
	print(x_np)
	print(y_np)
	# сложить две numpy матрицы
	sum = x_np + y_np
	# вывод результата сложения numpy матрицы
	print(sum)
	# вывод результата сложения матрицы
	for i in sum.tolist():
		print(*i)