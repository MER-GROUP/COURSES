'''
Найдите минимальное вершинное покрытие в двудольном графе.

На вход подается описание двудольного графа, в котором доли уже выделены явно. 
Первая строка содержит три натуральных числа: v_1 <100 — число вершин первой доли, 
v_2 <100 — число вершин второй доли, e≤v1∗v2 — число рёбер. Подразумевается, 
что первая доля состоит из вершин с номерами от 0 до v_1-1, вторая — из вершин 
с номерами от v_1 до v_1+v_2-1v−1. Следующие ee строк описывают рёбра: 
каждая из этих строк содержит два числа: 0≤u_i0≤v1 и v_1≤w_i0≤v_1+ v_2, 
что означает, что между вершинами u_i и w_i есть ребро.

Скопируйте описание графа из входа на выход и выведите единственную 
дополнительную строку — список номеров вершин, составляющих минимальное 
вершинное покрытие. Если таких покрытий несколько, выведите любое.
'''

#####################################################################################

"""
Вначале находим максимальное паросочетания с помощью нахождения 
максимального потока в двудольном графе, добавляя вспомогательные 
вершины ss и tt. ss связана с вершинами из левой части двудольного 
графа и ребра направлены от вершины ss. А tt связана с вершинами 
из правой части двудольного графа и все ребра от этих вершин 
направлены в tt. Находим таким образом все паросочетания, а затем 
находим минимальное вершинное покрытие. Для этого строим 
ориентированный граф таким образом:

1. Ребра, выходящие из левой части LL графа, направлены в вершины правой части RR графа.

2. Те ребра, которые присутствуют в максимальном паросочетании ориентируются наоборот из RR в LL 

3. Находим вершины, которые на покрыты максимальным паросочетанием (обозначим как множество UU)

4. Из каждой вершины v \in Uv∈U запускаем поиск в глубину. 
В результате какие-то вершины графа будут помечены, а какие-то нет.

5. Минимальное покрытие получим следующим образом - берем все непосещенные 
вершины из LL и все посещенные вершины из RR, которые покрыты максимальным паросочетанием
"""

#!/usr/bin/env python3
# coding = utf-8

import sys


def build_graph(v_1, v_2, e, reader):
    graph = [[] for _ in range(v_1 + v_2)]
    print(v_1, v_2, e)

    for _ in range(e):
        u, v = next(reader)
        print(u, v)
        graph[u].append(v + 1)
        graph[v].append(u + 1)

    return graph


def build_residual_graph(l_part, graph):
    # + 2 as we add two more vertice S and T
    # S connected with all vertex from L part
    # T connected with all vertex from R part
    g_len = len(graph) + 2
    residual_graph = [[None] * g_len for _ in range(g_len)]
    s = 0
    t = g_len - 1

    for i in range(1, l_part + 1):
        residual_graph[s][i] = 1
        residual_graph[i][s] = 0

    for i in range(l_part + 1, g_len - 1):
        residual_graph[i][t] = 1
        residual_graph[t][i] = 0

    for u in range(l_part):
        for v in graph[u]:
            residual_graph[u + 1][v] = 1
            residual_graph[v][u + 1] = 0

    return residual_graph


def is_forward_path(u, v, graph, l_part):
    return u <= l_part and v in graph[u]


def find_max_match(l_part, graph):
    """
    @graph is the original bipartite graph
    @l_part is the size of left part of BP graph
    """
    _FLOW = 1

    def dfs(s, t):
        """
        Find the path from a source to a sink
        """
        if s == t:
            return [s]

        visited[s] = True
        neighbours = tuple(i for i, w in enumerate(residual_graph[s])
                           if w is not None and w != 0)

        for n in neighbours:
            if not visited[n]:
                if (s < n and _FLOW - residual_graph[s][n] < _FLOW or
                        s > n and residual_graph[s][n] > 0):
                        new_path = dfs(n, t)

                        if new_path:
                            return [s] + new_path

        return None

    def update_residual(path):
        edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]

        for u, v in edges:
            residual_graph[u][v] -= _FLOW
            residual_graph[v][u] += _FLOW

    def get_matching():
        matching = []
        for i in range(1, l_part + 1):
            pair = [i for i, f in enumerate(residual_graph[i][1:-1], 1)
                    if f == 0]

            if pair:
                matching.append((i, pair.pop()))

        return matching

    residual_graph = build_residual_graph(l_part, graph)
    source = 0
    sink = len(residual_graph) - 1

    while True:
        # here while we are able to find a path and increase a flow
        # do it and update residual graph
        visited = [False for _ in range(len(residual_graph))]
        path = dfs(source, sink)

        if not path:
            break
        else:
            update_residual(path)

    return get_matching()


def find_min_cover(v_1, graph, max_match):
    def build_orgraph():
        orgraph = [[] for _ in range(g_len)]

        for i in range(v_1 + 1):
            for n in graph[i]:
                orgraph[i].append(n - 1)

        for u, v in max_match:
            orgraph[v - 1].append(u - 1)
            orgraph[u - 1].remove(v - 1)

        return orgraph

    def dfs(source):
        visited[source] = True

        for n in orgraph[source]:
            if not visited[n]:
                dfs(n)

    g_len = len(graph)
    unmatch_v = tuple(x - 1 for x in range(1, v_1 + 1)
                      if all(x != y[0] for y in max_match))

    orgraph = build_orgraph()
    visited = [False for _ in range(len(graph))]
    min_cover = []

    for v in unmatch_v:
        dfs(v)

    for u, v in max_match:
        if not visited[u - 1]:
            min_cover.append(u - 1)
        if visited[v - 1]:
            min_cover.append(v - 1)

    return sorted(min_cover)


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    v_1, v_2, e = next(reader)
    graph = build_graph(v_1, v_2, e, reader)
    max_match = find_max_match(v_1, graph)
    print(*find_min_cover(v_1, graph, max_match))


if __name__ == "__main__":
    main()

#####################################################################################

def min_covering(graph, v1, v2):

    stack, component, vertices = list(), list(), list()

    graph_copy = graph.copy()

    length = 0
    while length != len(graph_copy):
        length = len(graph_copy)
        for i in graph_copy.keys():
            if len(graph_copy[i][1]) == 1:
                vertex = graph_copy[i][1][0]
                if i not in vertices:
                    vertices.append(vertex)

                while graph_copy[vertex][1]:
                    adj = graph_copy[vertex][1].pop(0)
                    graph_copy[adj][1].remove(vertex)
                    if len(graph_copy[adj][1]) == 0:
                        del graph_copy[adj]

                del graph_copy[vertex]
                if len(graph_copy) == 0:
                    return print(*sorted(vertices))
                break

    if len(graph_copy.keys()) > 0:
        for i in graph_copy.keys():
            stack.insert(0, i)
            graph_copy[i][0] = 1

            while stack:
                finder = stack.pop(0)
                component.append(finder)

                for j in graph_copy[finder][1]:
                    if graph_copy[j][0] == 0:
                        stack.insert(0, j)
                        graph_copy[j][0] = 1
            break

    component1 = [i for i in component if i in v1]
    component2 = [i for i in component if i in v2]

    if len(component1) < len(component2):
        vertices = sorted(list(set(vertices + component1)))
        return print(*vertices)
    else:
        vertices = sorted(list(set(vertices + component2)))
        return print(*sorted(vertices))


x, y, e = map(int, input().split())
print(x, y, e)
v1, v2 = set(), set()

graph = {}

for i in range(e):
    m, n = map(int, input().split())
    print(m, n)
    if m == n: continue
    v1.add(m), v2.add(n)
    if m in graph: graph[m][1].append(n)
    else: graph[m] = [0, [n]]
    if n in graph: graph[n][1].append(m)
    else: graph[n] = [0, [m]]

min_covering(graph, v1, v2)

#####################################################################################

import sys
descr=''
line=sys.stdin.readline()
descr=descr+line
[v1,v2,e]=line.split(' ')
[v1,v2,e]=([int(v1),int(v2),int(e)])
U=[k for k in range(v1)]
V=[k+v1 for k in range(v2)]
E=[]
for line in sys.stdin:
    descr=descr+line
    [v1,v2]=line.split(' ')
    [v1,v2]=([int(v1),int(v2)])
    E.append([v1,v2])
if v1>v2:
    [U,V]=[V,U]
    E=[[e[1],e[0]] for e in E]

def depth_search(E,v0):
    V=[v0]
    while True:
        v_new=[e[1] for e in E if e[0] in V and e[1] not in V]
        if len(v_new)==0:
            break
        V=V+v_new
    return V

def find_path(E,v0,v1):
    if v0==v1:
        return [v0]
    if v1 in depth_search(E,v0):
        for v in [e[1] for e in E if e[0]==v0]:
            Enew=[e for e in E if e[0]!=v0 and e[1]!=v0]
            if v1 in depth_search(Enew,v):
                return [v0]+find_path(Enew,v,v1)
    return None
        
    
def remove_isolated(U,V,E):
    used_u=list(set([e[0] for e in E]))
    used_v=list(set([e[1] for e in E]))
    U_isolated=[u for u in U if u not in used_u]
    V_isolated=[v for v in V if v not in used_v]
    return [used_u,used_v]

def remove_degree1(U,V,E):
    U_new=U
    V_new=V
    E_new=E
    vert=[]
    check=True
    while check==True:
        check=False
        for u in U_new:
            lst=[e for e in E if e[0]==u]
            if len(lst)==1:
                check=True
                e=lst[0]
                v=e[1]
                lst1=[e for e in E if e[1]==v]
                E_new=[e for e in E_new if e not in lst1]
                [U_new,V_new]=remove_isolated(U_new,V_new,E_new)
                vert.append(v)
        for v in V_new:
            lst=[e for e in E if e[1]==v]
            if len(lst)==1:
                check=True
                e=lst[0]
                u=e[0]
                lst1=[e for e in E if e[0]==u]
                E_new=[e for e in E_new if e not in lst1]
                [U_new,V_new]=remove_isolated(U_new,V_new,E_new)
                vert.append(u)
    return [U_new,V_new,E_new,vert]
     
    
            
            
def find_incr_path(U,V,E,pairs_u,pairs_v,u0):
    pairs=[[pairs_v[k],pairs_u[k]] for k in range(len(pairs_u))]
    v_new=[v for v in V if [u0,v] in E and [u0,v] not in pairs]
    if len(v_new)==0:
        return []
    for v in v_new:
        if v not in pairs_v:
            return [u0,v]
        u1=pairs_u[pairs_v.index(v)]
        U_new=[u for u in U if u!=u0]
        V_new=[w for w in V if w!=v]
        s=find_incr_path(U_new,V_new,E,pairs_u,pairs_v,u1)
        if len(s)>0:
            return [u0,v]+s
    return []

def ford_max_pairs(U0,V0,E0):
    E=E0+[['s',u] for u in U]+[[v,'t'] for v in V]
    forward_edges=[]
    backward_edges=[]
    used_u=[]
    used_v=[]
    check=True
    while check:
        check=False
        for e in E0:
            if e[0] not in used_u and e[1] not in used_v:
                forward_edges=forward_edges+[e,['s',e[0]],[e[1],'t']]
                backward_edges.append([e[1],e[0]])
                used_u.append(e[0])
                used_v.append(e[1])
                check=True
    while True:
        path=find_path([e for e in E if e not in forward_edges]+backward_edges,'s','t')
        if path==None:
            break
        for k in range(len(path)-1):
            if [path[k],path[k+1]] not in backward_edges:
                forward_edges.append([path[k],path[k+1]])
                if k>0 and k<len(path)-2:
                    backward_edges.append([path[k+1],path[k]])
            else:
                backward_edges.remove([path[k],path[k+1]])
                forward_edges.remove([path[k+1],path[k]])
    pairs=[e for e in forward_edges if e[0]!='s' and e[1]!='t']
    pairs_u=[e[0] for e in pairs]
    pairs_v=[e[1] for e in pairs]
    return pairs_u,pairs_v
        
    
    
def find_independent_set(U0,V0,E):
    [U,V]=remove_isolated(U0,V0,E)
    [U,V,E,verts1]=remove_degree1(U,V,E)
    [pairs_u,pairs_v]=ford_max_pairs(U,V,E)
    E_orient=[[pairs_v[k],pairs_u[k]] for k in range(len(pairs_u))]
    for e in E:
        if [e[1],e[0]] not in E_orient:
            E_orient.append(e)
    L1=[]
    R1=[]
    for u in U:
        if u not in pairs_u:
            vert=depth_search(E_orient,u)
            L1=list(set(L1)|set([v for v in vert if v in U]))
            R1=list(set(R1)|set([v for v in vert if v in V]))
    return [u for u in U if u not in L1]+R1+verts1

sys.stdout.writelines(descr)
sys.stdout.write('\n')
res0=find_independent_set(U,V,E)
res=[u for u in U if u in res0]+[v for v in V if v in res0]
sys.stdout.write(' '.join([str(r) for r in res]))

#####################################################################################

def maximal_matching(graph, v1):
    def find_vertex_in_matching(v):
        for i in range(len(matching)):
            if matching[i][0] == v:
                return i, 1
            elif matching[i][1] == v:
                return i, 0
        return None

    def find_augmenting_path(i):
        def dfs(v):
            nonlocal augm_path_is_found
            used[v] = 1
            for w in graph[v]:
                if not used[w] and not augm_path_is_found:
                    temp = find_vertex_in_matching(w)
                    if temp is None:
                        augm_path.append(w)
                        augm_path_is_found = True
                    else:
                        j, part = temp[0], temp[1]
                        used[w] = 1
                        dfs(matching[j][part])
                        if augm_path_is_found:
                            augm_path.append(w)
            if augm_path_is_found:
                augm_path.append(v)

        if find_vertex_in_matching(i) is None:
            used = [0 for _ in range(len(graph))]
            augm_path = []
            augm_path_is_found = False
            dfs(i)
            if augm_path_is_found:
                return augm_path[::-1]
            else:
                return None

    matching = []
    for i in range(v1):
        augmenting_path = find_augmenting_path(i)
        if augmenting_path is not None:
            for j in range(len(augmenting_path) - 1):
                mt = sorted([augmenting_path[j], augmenting_path[j + 1]])
                if mt not in matching:
                    matching.append(mt)
                else:
                    matching.remove(mt)

    return matching


def minimal_vertex_cover(graph, v1):
    def dfs(v):
        used[v] = 1
        for w in dgraph[v]:
            if not used[w]:
                dfs(w)

    def in_matching(v):
        for i in range(len(mt)):
            if mt[i][0] == v:
                return True
        return False

    mt = maximal_matching(graph, v1)
    dgraph = [[] for _ in range(len(graph))]

    for i in range(v1):
        for j in range(len(graph[i])):
            edge = [i, graph[i][j]]
            if edge in mt:
                dgraph[edge[1]].append(edge[0])
            else:
                dgraph[edge[0]].append(edge[1])

    used = [0 for _ in range(len(dgraph))]
    for i in range(v1):
        if not in_matching(i):
            dfs(i)

    mvc = []

    for i in range(len(used)):
        if i < v1 and not used[i] or i >= v1 and used[i]:
            mvc.append(i)

    return mvc


v1, v2, e = map(int, input().split())
print(v1, v2, e)
graph = [[] for _ in range(v1 + v2)]
for _ in range(e):
    x, y = map(int, input().split())
    print(x, y)
    graph[x].append(y)
    graph[y].append(x)
    
print(*minimal_vertex_cover(graph, v1))

#####################################################################################