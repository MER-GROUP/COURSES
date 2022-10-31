# применение алгоритма Дейкстры
n = int(input())
city = [list(map(int,input())) for _ in range(n)]
path_dijkstra = [[9 * n**2] * n for _ in range(n)]
city_path = [['-'] * n for _ in range(n)]
flag = True
   
if city[n-1][n-1] == 0 or city[0][0] == 0:
    print('Impossible')
else:
# СЧИТАЕМ СТОИМОСТЬ ПРОХОДА ДО КАЖДОЙ КЛЕТКИ ПО АЛГОРИТМУ ДЕЙКСТРЫ
    path_dijkstra[0][0] = city[0][0]
    
    for i in range(n):
        for j in range(n):
            if i + 1 < n and city[i + 1][j] != 0:
                new_dist = path_dijkstra[i][j] + city[i + 1][j]
                path_dijkstra[i + 1][j] = min(path_dijkstra[i + 1][j], new_dist)
            if j + 1 < n and city[i][j + 1] != 0:
                new_dist = path_dijkstra[i][j] + city[i][j + 1]
                path_dijkstra[i][j + 1] = min(path_dijkstra[i][j + 1], new_dist)
    if path_dijkstra[n - 1][n - 1] == 9 * n**2:
        print('Impossible')
    else:
#РАЗМЕТКА ПУТИ ОТ КОНЦА К НАЧАЛУ
        i, j = n-1, n-1
        while i >= 0 and j >= 0:
            city_path[i][j] = '#'
            if path_dijkstra[i][j - 1] == 9 * n**2: i -= 1
            elif path_dijkstra[i - 1][j] == 9 * n**2: j -= 1
            elif path_dijkstra[i][j - 1] < path_dijkstra[i - 1][j]: j -= 1
            elif path_dijkstra[i][j - 1] > path_dijkstra[i - 1][j]: i -= 1
            else:
                if path_dijkstra[i][j - 1] - city[i][j - 1] < path_dijkstra[i - 1][j] - city[i - 1][j]: j -= 1
                elif path_dijkstra[i][j - 1] - city[i][j - 1] > path_dijkstra[i - 1][j] - city[i - 1][j]: i -= 1
# ВЫВОД МАРШРУТА
        for row in city_path:
            print(*row, sep='')