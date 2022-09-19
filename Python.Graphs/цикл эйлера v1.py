import networkx as nx
import networkx.algorithms as alg

v, e = map(int, input().split())
e_pair = list()
for _ in range(e):
    e_pair.append(tuple(map(int, input().split())))

graph = nx.Graph(e_pair)

try:
    list(alg.eulerian_circuit(graph))
    print(*graph.nodes)
except (nx.exception.NetworkXError):
    print('NONE')