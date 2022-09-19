import networkx as nx

g = nx.MultiGraph()
nodes_numb, edges_numb = map(int, input().split())
g.add_nodes_from([_ for _ in range(1, nodes_numb+1)])
g.add_edges_from([list(map(int, input().split())) for _ in range(edges_numb)])
print(' '.join(map(str, [u for u, v in nx.eulerian_circuit(g)])) if nx.is_eulerian(g) else 'NONE' )