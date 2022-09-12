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
from queue import deque

nv, ne = map(int, input().split())
adj = [set() for _ in range(nv)]
for v, w in (map(int, input().split()) for _ in range(ne)):
    adj[v].add(w)
    adj[w].add(v)

depth = [0] * nv
queue = deque([0])
verts = set([0])

while queue:
    v = queue.pop()
    for w in (w for w in adj[v] if w not in verts):
        depth[w] = depth[v] + 1
        verts.add(w)
        queue.appendleft(w)

print(' '.join(map(str, depth)))