'''
Найдите эйлеров цикл в графе. 

Формат входных данных:
В первой строке указаны два числа разделенных пробелом: 
v (число вершин) и e (число ребер). 
В следующих ee строках указаны пары вершин, соединенных ребром. 
Выполняются ограничения: 2≤v≤1000, 0≤e≤1000.

Формат выходных данных:
Одно слово: NONE, если в графе нет эйлерова цикла, 
или список вершин в порядке обхода эйлерова цикла, если он есть.
'''
'''
Sample Input 1:
4 2
1 2
3 2

Sample Output 1:
NONE

Sample Input 2:
3 3
1 2
2 3
3 1

Sample Output 2:
1 2 3

Это 5 тест. В последняей строке правильный ответ. Может кому-то пригодится. 
Input:
5 8
1 3
3 1
1 5
4 3
5 1
5 2
2 4
3 5
Output:
1 3 1 5 2 4 3 5
'''
import networkx as nx
import networkx.algorithms as alg

v, e = map(int, input().split())
e_pair = list()
for _ in range(e):
    e_pair.append(tuple(map(int, input().split())))

# test
# print('---test---')
# print(f'{v} {e}')
# print(*e_pair, sep='\n')

# graph = nx.Graph(e_pair)
graph = nx.MultiGraph(e_pair)

# test
# print('---test---')
# print(graph)
# print(graph.nodes)
# print(list(alg.eulerian_circuit(graph)))

try:
    print(list(alg.eulerian_circuit(graph)))
    print(nx.MultiGraph(list(alg.eulerian_circuit(graph))).nodes)
    print(list(alg.eulerian_path(graph)))
    print(nx.MultiGraph(list(alg.eulerian_path(graph))).nodes)
    print(*graph.nodes)
    print('-------------------------------')
    print(list(alg.eulerian_circuit(graph)))
    print([u for u, v in nx.eulerian_circuit(graph)])
    print('-------------------------------')
    print(list(nx.edge_dfs(nx.MultiGraph(e_pair), v)))
except (nx.exception.NetworkXError):
    print('NONE')