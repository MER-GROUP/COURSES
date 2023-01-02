'''
Найдите все точки сочленения в графе. 

На вход программе подаётся описание графа, 
состоящее не более чем из 100000 строк. 
Каждая строка описывает очередное ребро: 
содержит два номера вершин, которые данное ребро соединяет. 
Номера разделены пробелом. Гарантируется, 
что ребра определяют связный граф, вершины которого 
пронумерованы числами от 0 до некоторого n.

Выведите единственную строку — список номеров 
точек сочленения графа через пробел.

Sample Input:
0 1
1 2
2 0
3 2
4 3
4 2
5 4
Sample Output:
2 4
'''
# import sys
# edges = list(tuple(map(int, line.split())) for line in sys.stdin)
# '''
# В Python по умолчанию максимальная 
# глубина рекурсии не может быть более 1000. 
# Этого не хватает уже на втором тесте. 
# К счастью, увеличить допустимую глубину 
# рекурсии очень просто, и избавляться от рекурсии 
# в алгоритме поиска в глубину не обязательно. 
# Лимита 10000 достаточно для прохождения всех тестов:
# '''
# sys.setrecursionlimit(10000)

############################################################################

from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)


def rek(cur, ar, k, res, pot):
    global nowk
    k[cur] = nowk
    nowk += 1
    lmin = k[cur]
    lmax = 0
    for ch in ar[cur]:
        if k[ch] == 0:
            pot[cur] += 1
            lch = rek(ch, ar, k, res, pot)
            lmin = min(lmin, lch)
            lmax = max(lmax, lch)
        else:
            lmin = min(lmin, k[ch])

    if lmax >= k[cur]:
        res.add(cur)

    return lmin

ar = defaultdict(list)
for x in sys.stdin:
    a, b = map(int, x.split())
    ar[a].append(b)
    ar[b].append(a)

n = len(ar)
k = [0] * n
nowk = 1
pot = [0] * n
res = {0}

rek(0, ar, k, res, pot)

if pot[0] <= 1:
    res.remove(0)

print(' '.join(map(str, res)))

############################################################################

from sys import stdin, setrecursionlimit
from collections import defaultdict


setrecursionlimit(1000000)


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices_count = 0
        self.time = 0

    def add_edge(self, vertex_1, vertex_2):
        self.graph[vertex_1].append(vertex_2)
        self.graph[vertex_2].append(vertex_1)

        self.vertices_count = len(self.graph)

    def get_joint_points(self, vertex, visited, joints, parents, tin, meet_time):
        children_count = 0
        visited[vertex] = True
        meet_time[vertex] = self.time
        tin[vertex] = self.time
        self.time += 1

        for child in self.graph[vertex]:
            if not visited[child]:
                parents[child] = vertex
                children_count += 1

                self.get_joint_points(child, visited, joints, parents, tin, meet_time)

                tin[vertex] = min(tin[vertex], tin[child])
                if parents[vertex] == -1 and children_count > 1:
                    joints[vertex] = True
                elif parents[vertex] != -1 and tin[child] >= meet_time[vertex]:
                    joints[vertex] = True

            elif child != parents[vertex]:
                tin[vertex] = min(tin[vertex], meet_time[child])

    def run(self):
        visited = [False] * self.vertices_count
        joints = [False] * self.vertices_count
        parents = [-1] * self.vertices_count
        tin = [float("Inf")] * self.vertices_count
        meet_time = [float("Inf")] * self.vertices_count

        for vertex in range(self.vertices_count):
            if not visited[vertex]:
                self.get_joint_points(vertex, visited, joints, parents, tin, meet_time)

        for indx, value in enumerate(joints):
            if value:
                print(indx, end=" ")


graph = Graph()
for line in stdin:
    if not line:        
        break
    vertex_from, vertex_to = map(int, line.split())
    graph.add_edge(vertex_from, vertex_to)

graph.run()

############################################################################

import sys


sys.setrecursionlimit(10**5)

def dfs(v, p=-1):
    global time
    used[v] = 1
    d[v] = time
    up[v] = time
    time += 1
    children = 0
    for i in graph[v]:
        to = i
        if to == p:
            continue
        if used[to]:
            up[v] = min(up[v], d[to])
        else:
            dfs(to, v)
            up[v] = min(up[v], up[to])
            if up[to] >= d[v] and p != -1:
                points.add(v)
                children += 1
        if p == -1 and children > 1:
            points.add(v)


graph = {}
points = set()
edges = list(tuple(map(int, line.split())) for line in sys.stdin)
for x, y in edges:
    if x not in graph:
        graph[x] = set()
    graph[x].add(y)
    if y not in graph:
        graph[y] = set()
    graph[y].add(x)
n = len(graph)
used = [0 for _ in range(n)]
up = [0 for _ in range(n)]
d = [0 for _ in range(n)]
time = 1

for i in range(n):
    if not used[i]:
        dfs(i)

print(*sorted(points))

############################################################################

import sys

sys.setrecursionlimit(10000)

class Node:
    def __init__(self, **entries): 
        self.__dict__.update(entries)

def mark(node, p=None):
    # Помечаем вершину в исходном графе посещённым
    nodes[node].visited = True
    # Добавляем узел в остовное дерево
    tree[node] = Node(k = mark.k, l = None, children = [], parent = p, back = None)
    mark.k += 1
    # Для всех вершин связанных в исходном графе с текущей
    for a in nodes[node].linked:
        # Которые ещё не отмечены, как посещённые
        if not nodes[a].visited:
            # Добавляем их в дерево
            tree[node].children.append(a)
            mark(a, node)
    # Здесь мы уже можем создать список обратных рёбер
    tree[node].back = list(set(nodes[node].linked) -
                           set(tree[node].children) -
                           set([tree[node].parent]))
    # А теперь уже и вычислить l(x)
    # Мой первый вариант кода, как оказалось работает с Python 3.5 и не работает
    # с Python 3.3 и не запускается на Stepik. Пришлось переделать менее красиво.
    # tree[node].l = min(tree[node].k, tree[node].k,
    #                    *[tree[a].l for a in tree[node].children],
    #                    *[tree[a].k for a in tree[node].back])
    tree[node].l = min(min(tree[node].k, tree[node].k,
                           *[tree[a].l for a in tree[node].children]),
                       min(tree[node].k, tree[node].k,
                           *[tree[a].k for a in tree[node].back]))
    # print(node, tree[node].k, tree[node].l, tree[node].children, tree[node].back)
    # Проверим не является ли текущий узел точкой сочленения
    if not tree[node].parent:
        # Если текущий узел вершина дерева
        if len(tree[node].children) >= 2:
            # То проверяем сколько у него детей
            cut.append(node)
    else:
        # Если текущий узел не вершина дерева
        if [i for i in tree[node].children if tree[i].l >= tree[node].k]:
            # То сравниваем l(x) для всех детей с k(x) текущего узла и,
            # если хоть один больше или равен (получился непустой список),
            # то текущий узел будет точкой сочленения
            cut.append(node)

edges = list(tuple(map(int, line.split())) for line in sys.stdin)

# На основании списка всех рёбер создаём граф (список вершин и связей между ними)
nodes = {}
for a, b in edges:
    if a not in nodes:
        nodes[a] = Node(visited = False, linked = [b])
    else:
        nodes[a].linked.append(b)
    if b not in nodes:
        nodes[b] = Node(visited = False, linked = [a])
    else:
        nodes[b].linked.append(a)

# Список для хранения точек сочленения
cut = []

# Создаём остовное дерево
tree = {}
mark.k = 1
mark(0)
print(" ".join(map(str, cut)))

############################################################################

from collections import defaultdict
import sys
sys.setrecursionlimit(50000)
G = defaultdict(set)
for s in sys.stdin:
    a, b = map(int, s.strip().split())
    G[a].add(b); G[b].add(a)

used = set()
tin = dict()
fup = dict()
cutpoint = set()
timer = 1
stack=[(0,-1)]
def dfs(v, p=-1):
    global timer
    used.add(v)
    tin[v] = fup[v] = timer
    timer += 1
    child = 0
    for to in G[v]:
        if to == p: continue
        if to in used:
            fup[v] = min(fup[v], tin[to])
        else:
            dfs(to, v)
            fup[v] = min(fup[v], fup[to])
            if fup[to] >= tin[v] and p != -1:
                cutpoint.add(v)
            child += 1
    if p == -1 and child > 1:
        cutpoint.add(v)

dfs(0)
print(*sorted(cutpoint)) 

############################################################################

import sys
sys.setrecursionlimit(10**6)


d = {}
num = []
ans = set()
tree = {}
back = {}
pl = {}


def dfs(x):
    d[x][0] = True
    num.append(x)
    pl[x] = len(num)-1
    for i in d[x][2]:
        if d[i][0]:
            if len(num) - 1 - pl[i] > 1:
                back[x].add(i)
        else:
            tree[x].add(i)
            dfs(i)


def l(p):
    m = p
    for j in tree[num[p]]:
        ind = pl[j]
        y = l(ind)
        if y < m:
            m = y
    for t in back[num[p]]:
        ind = pl[t]
        if ind < m:
            m = ind
    d[num[p]][1] = m
    return m


edges = list(tuple(map(int, line.split())) for line in sys.stdin)
for i in edges:
    if i[0] in d.keys():
        d[i[0]][2].add(i[1])
    else:
        d[i[0]] = [False, 0, set()]
        tree[i[0]] = set()
        back[i[0]] = set()
        d[i[0]][2].add(i[1])
    if i[1] in d.keys():
        d[i[1]][2].add(i[0])
    else:
        d[i[1]] = [False, 0, set()]
        tree[i[1]] = set()
        back[i[1]] = set()
        d[i[1]][2].add(i[0])
dfs(0)
l(0)
if len(tree[0]) > 1:
    ans.add(str(0))
for i in range(1, len(num)):
    for j in tree[num[i]]:
        if d[j][1] >= i:
            ans.add(str(num[i]))
print(' '.join(ans))

############################################################################

import sys
from collections import defaultdict
sys.setrecursionlimit(8000)
E,v = defaultdict(lambda: []),0
for line in sys.stdin:
    v1, v2 = map(int, line.split())
    E[v1].append(v2)
    E[v2].append(v1)
    v = max(v - 1, max(v1,v2)) + 1
visited, up, tin, time, cutpoint = [0]*v, [0]*v, [0]*v, 0, set()
def dfs(w, p):
    global time
    time += 1
    up[w] = tin[w] = time
    visited[w],count = 1,0
    for u in E[w]:
        if visited[u]:
            up[w] = min(up[w], tin[u])
        else:
            dfs(u, w)
            count += 1
            up[w] = min(up[w], up[u])
            if p != -1 and up[u] >= tin[w]:
                cutpoint.add(w)
        if p == -1 and count >= 2:
            cutpoint.add(w)
for i in range(v):
    if not visited[i]:
        dfs(i, -1)
print(*cutpoint)

############################################################################

from sys import stdin
from collections import defaultdict

def cut_points(edges):
    adj = defaultdict(set)
    nv = 0
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
        nv = max(nv, a+1, b+1)
    cuts = set()
    visited = [False] * nv

    for root in adj.keys():
        if visited[root]:
            continue
        cur_val = 0
        k_val = [None] * nv
        l_val = [None] * nv

        root_degree = 0
        visited[root] = True
        k_val[root] = l_val[root] = cur_val
        cur_val += 1
        stack = [(None, root, iter(adj[root]))]

        while stack:
            grand, parent, children = stack[-1]
            for child in children:
                if visited[child]:
                    if k_val[child] < k_val[parent]:  # back edge
                        l_val[parent] = min(l_val[parent], k_val[child])
                    continue
                visited[child] = True
                if parent == root:
                    root_degree += 1
                k_val[child] = l_val[child] = cur_val
                cur_val += 1
                stack.append((parent, child, iter(adj[child])))
                break
            else:
                stack.pop()
                if grand is not None and grand != root:
                    l_val[grand] = min(l_val[grand], l_val[parent])
                    if l_val[parent] >= k_val[grand] and grand != root:
                        cuts.add(grand)
        if root_degree > 1:
            cuts.add(root)
    return sorted(cuts)

print(*cut_points(map(int, s.split()) for s in stdin))

############################################################################

from collections import defaultdict
import sys
    
def cut_vertices(I, root=0):
    i = root_deg = 0
    stack, tree_nums, tree_children = [root], [0]*len(I), [[]]
    V, cuts = set([root]), set()
    while True:
        last = stack[-1]
        S = I[last] - V
        if S:
            if (len(stack) == 1):
                root_deg += 1
            i += 1
            child = S.pop()
            stack.append(child)
            tree_nums[child] = i
            V.add(child)
            tree_children[-1].append(child)
            tree_children.append([])
        elif len(stack) > 1:
            stack.pop()
            new_min = tree_nums[last]
            for ancestor in (set(stack[:-1]) & I[last]):
                if tree_nums[ancestor] < new_min:
                    new_min = tree_nums[ancestor] 
            for child in tree_children[-1]:
                if tree_nums[child] >= tree_nums[last]:
                    cuts.add(last)
                elif tree_nums[child] < new_min:
                    new_min = tree_nums[child] 
            tree_nums[last] = new_min
            tree_children.pop()
        else:
            break
    if root_deg > 1:
        cuts.add(root)
    return cuts

if __name__ == '__main__':
    reader = (map(int, s.split()) for s in sys.stdin)
    I = defaultdict(set)
    for i, j in reader:
        I[i].add(j)
        I[j].add(i)
    print(*cut_vertices(I))

############################################################################

import sys

sys.setrecursionlimit(10**5)

def find_cut_points(graph):
    def visit(v):
        used[v] = 1
        nonlocal order
        k[v] = order
        l[v] = k[v]
        order += 1

        for i in range(len(graph[v])):
            w = graph[v][i][0]
            if not used[w]:
                graph[v][i][1] = 1
                j = graph[w].index([v, 0])
                graph[w][j][1] = 1
                visit(w)

        if v == 0:
            c = 0
            for w in graph[v]:
                if w[1] == 1:
                    c += 1
            if c > 1:
                cut_points.append(v)
        else:
            for w in graph[v]:
                if w[1] == 1 and k[w[0]] > k[v]:
                    l[v] = min(l[v], l[w[0]])
                    if k[v] <= l[w[0]] and v not in cut_points:
                        cut_points.append(v)
                elif w[1] == 0:
                    l[v] = min(l[v], k[w[0]])

    v = len(graph)
    order = 1
    k = [0 for _ in range(v)]
    l = [0 for _ in range(v)]
    used = [0 for _ in range(v)]
    cut_points = []

    visit(0)
    return cut_points[::-1]


graph = [[]]

for edge in sys.stdin:
    x, y = map(int, edge.split())
    if x >= len(graph):
        graph.extend([] for _ in range(x - len(graph) + 1))
    if y >= len(graph):
        graph.extend([] for _ in range(y - len(graph) + 1))
    graph[x].append([y, 0])
    graph[y].append([x, 0])

print(*find_cut_points(graph))

############################################################################