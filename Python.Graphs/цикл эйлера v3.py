import networkx as nx
import networkx.algorithms as alg

v, e = map(int, input().split())
e_pair = list()
for _ in range(e):
    e_pair.append(tuple(map(int, input().split())))

graph = nx.MultiGraph(e_pair)

try:
    # list(alg.eulerian_circuit(graph))
    if alg.has_eulerian_path(graph):
        print(*[u for u, v in nx.eulerian_circuit(graph)])
        print(*[u for u, v in alg.eulerian_circuit(graph)])
except (nx.exception.NetworkXError):
    print('NONE')