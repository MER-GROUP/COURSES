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
import networkx as nx

g = nx.Graph()
nodes_numb, edges_numb = map(int, input().split())
for i in range(nodes_numb):
    g.add_node(i)
for _ in range(edges_numb):
    node1, node2 = map(int, input().split())
    g.add_edge(node1, node2)
node_from = 0
for node_to in g.nodes():
    print(len(nx.shortest_path(g, node_from, node_to))-1, end=' ')