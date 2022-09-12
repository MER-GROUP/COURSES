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
result, g, valid, points = {i:0 for i in range(v)}, {i: [] for i in range(v)}, {i:[True, False][min(i, 1)] for i in range(v)}, [0]
def f(ab): g[ab[0]], g[ab[1]] = g[ab[0]]+[ab[1]], g[ab[1]]+[ab[0]]
for i in range(e): f(list(map(int, input().split())))
while points:
    for each in g[points[0]]:
        if not valid[each]: valid[each], result[each], points = True, result[points[0]]+1, points + [each]
    points = points[1:]
print(*list(map(lambda x: result[x], range(v))))