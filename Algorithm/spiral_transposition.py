'''
Функция spiral_transposition() 😈
Реализуйте функцию spiral_transposition(), которая принимает в качестве 
аргумента матрицу (двумерный список) и возвращает одномерный список со 
значениями исходной матрицы, расположенными по спирали 
(начиная с верхнего левого угла).

Примечание 1. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию spiral_transposition(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/1020135/tests_4218040.zip

Sample Input 1:
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]] 
print(spiral_transposition(matrix))
Sample Output 1:
[1, 2, 3, 6, 9, 8, 7, 4, 5]

Sample Input 2:
matrix = [['a', 'b', 'c', 'd', 'e'],
          ['f', 'g', 'h', 'i', 'j'],
          ['k', 'l', 'm', 'n', 'o']]     
print(spiral_transposition(matrix))
Sample Output 2:
['a', 'b', 'c', 'd', 'e', 'j', 'o', 'n', 'm', 'l', 'k', 'f', 'g', 'h', 'i']

Sample Input 3:
matrix = [[1, 2, 3, 4, 5, 6]]     
print(spiral_transposition(matrix))
Sample Output 3:
[1, 2, 3, 4, 5, 6]

Sample Input 4:
matrix = [[1],
          [2],
          [3],
          [4]]        
print(spiral_transposition(matrix))
Sample Output 4:
[1, 2, 3, 4]

Sample Input 5:
matrix = [[1]]      
print(spiral_transposition(matrix))
Sample Output 5:
[1]

Sample Input 6:
matrix = [[]]
         
print(spiral_transposition(matrix))
Sample Output 6:
[]

Sample Input 7:
matrix = [[6, 4, 6, 5, 4, 9, 6, 1, 8],
          [1, 4, 8, 0, 3, 1, 5, 9, 2],
          [0, 9, 3, 4, 3, 4, 4, 5, 4],
          [4, 3, 1, 6, 0, 4, 8, 3, 8],
          [5, 1, 2, 1, 1, 6, 6, 9, 4],
          [0, 0, 3, 9, 5, 9, 9, 4, 9],
          [1, 0, 0, 4, 7, 1, 6, 1, 2],
          [2, 1, 6, 7, 2, 5, 8, 0, 6],
          [0, 4, 5, 1, 7, 4, 0, 2, 6]]      
print(spiral_transposition(matrix))
Sample Output 7:
[6, 4, 6, 5, 4, 9, 6, 1, 8, 2, 4, 8, 4, 9, 2, 6, 6, 2, 0, 4, 7, 1, 5, 4, 0, 2, 1, 0, 5, 4, 0, 1, 4, 8, 0, 3, 1, 5, 9, 5, 3, 9, 4, 1, 0, 8, 5, 2, 7, 6, 1, 0, 0, 1, 3, 9, 3, 4, 3, 4, 4, 8, 6, 9, 6, 1, 7, 4, 0, 3, 2, 1, 6, 0, 4, 6, 9, 5, 9, 1, 1]

Sample Input 8:
matrix = [[5, 9, 2, 7],
          [5, 5, 0, 6],
          [3, 4, 7, 7],
          [3, 7, 7, 6],
          [7, 7, 7, 1],
          [4, 8, 0, 9],
          [7, 1, 2, 7],
          [7, 7, 7, 9],
          [1, 5, 1, 4],
          [6, 4, 9, 2],
          [3, 2, 8, 4],
          [4, 2, 6, 7],
          [0, 8, 6, 4],
          [7, 2, 6, 5],
          [5, 7, 1, 0]] 
print(spiral_transposition(matrix))
Sample Output 8:
[5, 9, 2, 7, 6, 7, 6, 1, 9, 7, 9, 4, 2, 4, 7, 4, 5, 0, 1, 7, 5, 7, 0, 4, 3, 6, 1, 7, 7, 4, 7, 3, 3, 5, 5, 0, 7, 7, 7, 0, 2, 7, 1, 9, 8, 6, 6, 6, 2, 8, 2, 2, 4, 5, 7, 1, 8, 7, 7, 4]
'''

def spiral_transposition(array: list) -> list:
    _arr = list()

    def spiral(n: int, m: int) -> None:
        arr = [[0] * m for _ in range(n)]
        row, row_delta, col, col_delta = 0, 0, 0, 1

        for num in range(1, n * m + 1):
            arr[row][col] = num
            _arr.append(array[row][col])

            if arr[(row + row_delta) % n][(col + col_delta) % m]:
                row_delta, col_delta = col_delta, -row_delta

            row += row_delta
            col += col_delta
    
    spiral(len(array), len(array[0]))
    return _arr

if __name__ == '__main__':
    matrix = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]] 
    print(spiral_transposition(matrix))