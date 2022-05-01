# ввод данных
size = int(input())
w = [[int(i) for i in input()] for j in range(size)]

# матрица с дистанциями до начальной клетки,
#  заполненная большими числами (для начала)
max_dist = 9 * size**2
dist = [[max_dist for i in range(size)] for j in range(size)]
dist[0][0] = w[0][0]

# обход всех клеток с заполнением
#  матрицы минимальных дистанций до начальной клетки
for i in range(size):
    for j in range(size):
        if i + 1 < size and w[i + 1][j] != 0:
            new_dist = dist[i][j] + w[i + 1][j]
            dist[i + 1][j] = min(dist[i + 1][j], new_dist)
        if j + 1 < size and w[i][j + 1] != 0:
            new_dist = dist[i][j] + w[i][j + 1]
            dist[i][j + 1] = min(dist[i][j + 1], new_dist)

# обход в обратном порядке с рисованием пути
#  из двух вариантов выбирается тот,
#  который меньше дистанции к текущей точке на величину веса
impossible = False
answer = [['-' for i in range(size)] for j in range(size)]
answer[-1][-1] = '#'
i, j = size - 1, size - 1
while (i, j) != (0, 0) and not impossible:
    if dist[i - 1][j] == dist[i][j] - w[i][j]:
        i -= 1
        answer[i][j] = '#'
    elif dist[i][j - 1] == dist[i][j] - w[i][j]:
        j -= 1
        answer[i][j] = '#'
    else:
        impossible = True

# вывод ответа
if impossible or w[0][0] == 0:
    print('Impossible')
else:
    [print(*s, sep='') for s in answer]