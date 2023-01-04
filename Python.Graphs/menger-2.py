'''
Найдите максимальный поток в сети.

Первая строка содержит два числа 2≤v≤50 и 0≤e≤1000 — число вершин 
и число рёбер сети. Следующие ee строк описывают рёбра: 
каждая из них содержит три целых числа через пробел: 0≤u_i<v,
0≤v_i<v,0≤c_i<50 — исходящую и входящую вершины для этого ребра, 
а так же его пропускную способность.

Выведите единственное число — величину максимального потока из вершины 0 в вершину v-1.

Sample Input:
4 5
0 1 3
1 2 1
0 2 1
1 3 1
2 3 3

Sample Output:
3
'''

######################################################################################

def BFS(graph, s, t, parent):

    visited = [False] * len(graph)
    queue = list()
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.pop(0)
        for ind in range(len(graph[u])):
            if visited[ind] is False and graph[u][ind] > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return True if visited[t] else False

def FordFulkerson(graph, source, sink):

    parent = [-1] * (len(graph))
    max_flow = 0

    while BFS(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink

        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink

        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow


v, e = map(int, input().split(' '))
if v == 0 or e == 0:
    print(0)
else:
    graph = [[0]*v for i in range(v)]
    for i in range(e):
        source, sink, capacity = map(int, input().split(' '))
        graph[source][sink] = capacity
    print(FordFulkerson(graph, 0, v-1))

######################################################################################

import networkx as nx
G = nx.DiGraph()
number_vertices, number_edges = map(int, input().split())
for _ in range(number_edges):
    new_edge = list(map(int, input().split()))
    G.add_edge(*new_edge[:2], capacity=new_edge[-1])
try:
    flow_value, flow_dict = nx.maximum_flow(G, 0, number_vertices-1)
    print(flow_value)
except nx.NetworkXError:
    print(0)

######################################################################################

from collections import defaultdict, deque
v, e = map(int, input().split())
C = {}
f = {}
for _ in range(e):
    a, b, c = map(int, input().split())
    if (b,a) in C:
        C[a,-b] = C[-b,b] = c
        f[a,-b] = f[-b,b] = 0 
    else:
        C[a,b] = c
        f[a,b] = 0

while True:
    Gf = defaultdict(set)
    cf = {}
    for a,b in C:
        cf[a,b] = C[a,b] - f[a,b]
        cf[b,a] = f[a,b]
        if cf[a,b]:
            Gf[a].add(b)
        if cf[b,a]:
            Gf[b].add(a)
    D = deque([0])
    visited = {0:0}
    while D:
        a = D.popleft()
        for b in Gf[a]:
            if b not in visited:
                D.append(b)
                visited[b]=a
        if v-1 in visited: break
    else: break
    u = v-1
    cfp = float('inf')
    while u:
        cfp = min(cfp, cf[visited[u],u])
        u = visited[u]
    if cfp == 0: break
    u = v-1
    while u:
        if (visited[u],u) in C:
            f[visited[u],u] += cfp
        else:
            f[u,visited[u]] -= cfp
        u = visited[u]
print(sum(f[0,a] for a in range(v) if (0,a) in C))

######################################################################################

from numpy import inf


def find_maxf(path, minf):
    maxf = 0
    u = path[-1]
    path.append(-1)
    global flow
    for v in graph[u]:
        if v not in path:
            if graph[u][v] > maxf:
                maxf = graph[u][v]
                path[-1] = v
    if path[-1] != -1:
        minf = min(graph[u][path[-1]], minf)
        if path[-1] == t:
            flow += minf
            for i in range(len(path)-1):
                graph[path[i]][path[i+1]] -= minf
                try:
                    graph[path[i+1]][path[i]] += minf
                except(KeyError):
                    graph[path[i+1]][path[i]] = minf
        else:
            find_maxf(path, minf)
    else:
        path.pop()
        graph[path[-2]][path[-1]] = 0
        path.pop()
        if sum([graph[s][i] for i in graph[s]]):
            find_maxf(path, minf)


def find_path(s):
    path = [s]
    minf = inf
    find_maxf(path, minf)


n, m = (int(i) for i in input().split())
graph = {i: {} for i in range(n)}
s, t = 0, n - 1
flow = 0
for _ in range(m):
    u, v, c = input().split()
    if u != v:
        try:
            graph[int(u)][int(v)] += int(c)
        except(KeyError):
            graph[int(u)][int(v)] = int(c)
while sum([graph[s][i] for i in graph[s]]):
    find_path(s)
print(flow)

######################################################################################