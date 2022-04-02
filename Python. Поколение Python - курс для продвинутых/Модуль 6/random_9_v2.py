from random import shuffle
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
          
n, m, lst = len(matrix), len(matrix[0]), sum(matrix, [])
shuffle(lst)
matrix = [[lst.pop(0) for j in range(m)] for i in range(n)]

print(*matrix, sep='\n')