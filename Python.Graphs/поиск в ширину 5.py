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
#!/usr/bin/env python3
# coding=utf-8

import sys


def ReadGraph(num_v, num_e, reader):
    graph = {v: [] for v in range(num_v)}

    for _ in range(num_e):
        u, v = next(reader)
        graph[u].append(v)
        graph[v].append(u)

    return graph


def BreadthFirstSearch(graph, source):
    dist = [-1 if i != 0 else 0 for i in range(len(graph))]
    queue = [source]

    while len(queue) > 0:
        cur_v = queue.pop(0)

        for v in graph[cur_v]:
            if dist[v] == -1:
                dist[v] = dist[cur_v] + 1
                queue.append(v)

    return dist


def main():
    SOURCE_NODE = 0
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, m = next(reader)
    graph = ReadGraph(n, m, reader)
    print(" ".join(str(d) for d in BreadthFirstSearch(graph, SOURCE_NODE)))


if __name__ == "__main__":
    main()