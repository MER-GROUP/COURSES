'''
На вход программе подаётся описание простого связного графа. 
Первая строка содержит два числа: число вершин V≤10000 и число рёбер E≤30000 графа. 
Следующие E строк содержат номера пар вершин, соединенных рёбрами. 
Вершины имеют номера от 0 до V-1. Выведите список из V чисел — расстояний от вершины 0 
до соответствующих вершин графа.

Sample Input:

6 7
0 1
1 2
2 0
3 2
4 3
4 2
5 4
Sample Output:

0 1 1 2 2 3
'''
u, e = map(int, input().split())  # считываем колличество вершин и ребер

l_u = [[] for i in range(u)]  # создаем список пустых списков по колличеству вершин

for i in range(e):  # считываем список ребер по их колличеству
    u1, u2 = (int(i) for i in input().split())
    l_u[u1].append(u2)  # сразу же добовляем смежные вершины в список вершин
    l_u[u2].append(u1)  # список вершин работает быстрее списка ребер

start = 0  # с какой вершины начинать
D = [None] * u  # список расстояний до стартовой вершины
D[start] = 0  # от стартовой до стартовой - 0
Q = [start]  # создали очередь со стартовой вершиной

while len(Q):  # пока есть очередь
    q = Q.pop(0)  # удалили из очереди первый элемент, сохранив его в переменную q
    for v in l_u[q]:  # для вершины из списка вершин
        if D[v] is None:  # если расстояние неизвестно
            D[v] = D[q] + 1  # в список с расстояниями добовляем расстояние от вершины сохраненной как q  + 1
            Q.append(v)  # добовляем v в очередь

print(*D)