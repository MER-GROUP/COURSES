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
from collections import defaultdict
from queue import Queue
v, e = map(int,input().split())
E, dist, colors, q = defaultdict(lambda: []), [0]*v, [0]*v, Queue()
for _ in range(e):
    v1, v2 = map(int,input().split())
    E[v1].append(v2)
    E[v2].append(v1)
def bfs(u):
    q.put(u)
    colors[u] = 1
    while not q.empty():
        w = q.get()
        for z in E[w]:
            if not colors[z]:
                colors[z] = 1
                dist[z] = dist[w] + 1
                q.put(z)
        colors[w] = 1
bfs(0)
print(" ".join(map(str,dist)))