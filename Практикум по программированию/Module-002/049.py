'''
Координаты соседей
Для клетки с координатами (x, y) в таблице размером M × N 
выведите координаты ее соседей. Соседними называются клетки, имеющие общую сторону.

Входные данные
Даны натуральные числа M, N, x, y (1 ≤ x ≤ M ≤ 10^9, 1 ≤ y ≤ N ≤ 10^9).

Выходные данные
Выведите пары координат соседей этой клетки в порядке слева направо сверху вниз.

Sample Input:
3 3
2 2
Sample Output:
1 2
2 3
2 1
3 2
'''
x_border, y_border = map(int, input().split())
x, y = map(int, input().split())

left, up, down, right = [0] * 4
left = (x - 1, y) if x != 1 else (0, 0)
up = (x, y + 1) if y != y_border else (0, 0)
down = (x, y - 1) if y != 1 else (0, 0)
right = (x + 1, y) if x != x_border else (0, 0)

for line in (left, up, down, right):
    if not 0 in line:
        print(*line)