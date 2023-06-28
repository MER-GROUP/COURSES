"""
r, c - это текущее положение в матрице, строка (row) и столбец (column). 
dr, dc - единичные приращения по строке и столбцу соотвественно. 
Последние задают одно из 4-х направлений движения по горизонтали и вертикали:

(0, 1) - вправо, (1, 0) - вниз, (0, -1) - влево, (-1, 0) - вверх

По начальным значениям этих переменных можно сделать вывод, 
что движение начинается из верхнего левого угла в направлении вправо.

Обмен значений координат с изменением знака

dr, dc = dc, -dr
на самом деле совершает поворот по часовой стрелке на 90 градусов. 
Это можно проверить взяв начальное направление вправо 
и проделав последовательно обмен координат по формуле 4 раза:

(0, 1) ----------> (1, 0)
   |                  |
   |                  |
   |                  |
   |                  |
   |                  |
(-1, 0)<--------- (0, -1)

получается замкнутый круг, состоящий из 4 поворотов по часовой стрелке.

Проверка

a[(r + dr) % n][(c + dc) % m]

позволяет определить момент когда нужно выполнить поворот. 
Взятие остатка от деления координат на размерности матрицы, 
закольцовывает значения координат (строк и столбцов) в пределах матрицы. 
Если проследить за тем как идет заполнение матрицы спиралью, 
то можно обнаружить интересное свойство: 

на момент проверки, позиция после закальцовывания 
всега будет уже заполнена ненулевым значением, 
потому что уже была посещена ранее.

Действительно, в момент когда спираль упирается в стену 
и пытается двигатся дальше в этом направлении, 
её координата закольцовывется и оказывается с противоположной стороны матрицы 
в том же направлении. Но ведь именно оттуда спираль 
и пришла прежде чем уткнулась в стену! Это свойство гарантирует 
что спираль будет совершать поворот по часовой стрелке, 
каждый раз когда уткнётся в стену. При этом матрицу не обязательно 
заранее заполнять каким либо значением! Последнее может быть особенно 
удобно для языков программирования со статическим типизировнием (С/С++), 
в которых можно  выделять участок памяти под матрицу не тратя 
время на её инициализацию.

Sample Input 1:
4 5
Sample Output 1:
1  2  3  4  5
14 15 16 17 6
13 20 19 18 7
12 11 10 9  8
"""

# 1
def spiral(n: int, m: int) -> list:
    arr = [[0] * m for _ in range(n)]
    row, row_delta, col, col_delta = 0, 0, 0, 1

    for num in range(1, n * m + 1):
        arr[row][col] = num

        if arr[(row + row_delta) % n][(col + col_delta) % m]:
            row_delta, col_delta = col_delta, -row_delta

        row += row_delta
        col += col_delta

    return arr

# 2
def spiral(n: int, m: int) -> list:
    arr = [[0] * m for _ in range(n)]
    num = iter(range(1, n * m + 1))

    def spiral_rec(row: int, col: int) -> None: # spiral
        if (n <= spiral_rec.row or 0 > spiral_rec.row)\
            or (m <= spiral_rec.col or 0 > spiral_rec.col)\
            or arr[row][col]: # exit
            pass
        else:
            while True: # right
                if spiral_rec.col >= m or arr[spiral_rec.row][spiral_rec.col]:
                    spiral_rec.col -= 1
                    spiral_rec.row += 1
                    break
                arr[spiral_rec.row][spiral_rec.col] = next(num)
                spiral_rec.col += 1
                
            while True: # down
                if spiral_rec.row >= n or arr[spiral_rec.row][spiral_rec.col]:
                    spiral_rec.row -= 1
                    spiral_rec.col -= 1
                    break
                arr[spiral_rec.row][spiral_rec.col] = next(num)
                spiral_rec.row += 1
                
            while True: # left
                if spiral_rec.col < 0 or arr[spiral_rec.row][spiral_rec.col]:
                    spiral_rec.col += 1
                    spiral_rec.row -= 1
                    break
                arr[spiral_rec.row][spiral_rec.col] = next(num)
                spiral_rec.col -= 1
                
            while True: # up
                if spiral_rec.row < 0 or arr[spiral_rec.row][spiral_rec.col]:
                    spiral_rec.row += 1
                    spiral_rec.col += 1
                    break
                arr[spiral_rec.row][spiral_rec.col] = next(num)
                spiral_rec.row -= 1
                  
            spiral_rec(spiral_rec.row, spiral_rec.col) # rec

    spiral_rec.row = 0
    spiral_rec.col = 0
    spiral_rec(spiral_rec.row, spiral_rec.col)
    return arr

# 3
def spiral(n: int, m: int) -> list:
    arr = [[0] * m for _ in range(n)]
    col, row = 0, 0
    num, ndim = 1, n * m + 1

    while num < ndim:
        for c in range(col, m-col): # right
            arr[row][c] = num
            num += 1
        if not num < ndim: break # exit if only one row

        for r in range(row+1, n-row): # down
            arr[r][m-col-1] = num
            num += 1
        if not num < ndim: break # exit if only one col

        for c in range(m-col-2, col-1, -1): # left
            arr[n-row-1][c] = num
            num += 1

        for r in range(n-row-2, row, -1): # up
            arr[r][col] = num
            num += 1

        col += 1 # shift col
        row += 1 # shift row

    return arr

if __name__ == '__main__':
    n, m = 5, 5
    # n, m = 4, 5
    # n, m = 1, 1
    # n, m = 1, 5
    # n, m = 2, 5
    # n, m = 3, 5
    # n, m = 5, 1
    # n, m = 5, 2
    # n, m = 5, 3
    for arr in spiral(n, m):
        for el in arr:
            print(str(el).ljust(4), end='')
        print()