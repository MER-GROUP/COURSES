# модуль для работы с матрицами
import numpy as np

# инициализация матрицы
A = np.matrix([[1, 0], [4, 1]])

# возведение в степень матрицы
A = np.linalg.matrix_power(A, 25)

# вывод в консоль матрицы
print(A)

# вывод в консоль матрицы
print(*[' '.join([f'{el}'  for el in row.tolist()]) for row in A], sep='\n')