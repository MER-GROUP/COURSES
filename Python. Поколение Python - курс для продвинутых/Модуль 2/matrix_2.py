# вывод матрицы
print('##########')
matrix  = [[1, 2, 8, 0],
           [-4, 1, 9, 4],
           [41, 71, 2, -2]]

print(matrix[2][3])

# вывод матрицы
print('##########')
n = 3
a = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
    
# реверс матрицы
print('##########')
n = 3
a = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]

for i in range(n):
    for j in range(n):
        print(a[j][i], end=' ')
    print()
    
# реверс матрицы
print('##########')
n = 3
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

for i in range(n):
    for j in range(n):
        print(a[n - i - 1][n - j - 1], end=' ')
    print()
    
# обработка матрицы
print('##########')
n = 5
a = [[19, 21, 33, 78, 99], 
     [41, 53, 66, 98, 76], 
     [79, 80, 90, 60, 20],
     [33, 11, 45, 67, 90],
     [45, 67, 12, 98, 23]]

maximum = -1
minimum = 100

for i in range(n):
    if a[i][i] > maximum:
        maximum = a[i][i]
    if a[i][n - i - 1] < minimum:
        minimum = a[i][n - i - 1]
print(minimum + maximum)