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
from collections import deque

v, e = map(int, input().split())
g = [[] for i in range(v)]
for i in range(e):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

def bfs(g, start):
    dist = [1000000000 for i in range(len(g))]
    q = deque()
    q.append(start)
    dist[start] = 0
    while q:
        u = q.popleft()
        for x in g[u]:
            if dist[x] == 1000000000:
                q.append(x)
                dist[x] = dist[u] + 1
    return dist

for u in bfs(g, 0):
    print(u, end=' ')