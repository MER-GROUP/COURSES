import networkx as nx

v, e = map(int, input().split())
e_pair = list()
for _ in range(e):
    e_pair.append(tuple(map(int, input().split())))

graph = nx.MultiGraph(e_pair)

try:
    if (v==0 or e==0):
        print('NONE')
    else:
        print(*[u for u, v in nx.eulerian_circuit(graph)])
except (nx.exception.NetworkXError):
    print('NONE')