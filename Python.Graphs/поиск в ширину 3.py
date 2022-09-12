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
v, e = map(int, input().split())
used = [False] * v
graph = [[] for j in range(v)]
distance = [0 for i in range(v)]
q = []

for i in range(e):
    m, n = map(int, input().split())
    graph[m].append(n)
    graph[n].append(m)

q.append(0)
used[0] = True
while q:
    current = q.pop(0)
    for i in graph[current]:
        if not used[i]:
            q.append(i)
            distance[i] = distance[current] + 1
            used[i] = True

print(' '.join([str(i) for i in distance]))