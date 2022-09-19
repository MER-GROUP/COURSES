def connected_components(graph):
    def visit(v):
        visited[v] = 1
        for w in graph[v]:
            if not visited[w]:
                visit(w)

    visited = [0 for _ in range(len(graph))]
    cc = 0

    for i in range(len(graph)):
        if not visited[i]:
            visit(i)
            cc += 1

    return cc


def is_eulerian(graph):
    if connected_components(graph) > 1:
        return False

    for w in graph:
        if len(w) % 2 != 0:
            return False

    return True


def eulerial_cycle(graph):
    def remove_edge(i, j):
        graph[i].remove(j)
        graph[j].remove(i)

    def visit(v):
        for w in graph[v]:
            remove_edge(w, v)
            visit(w)
        cycle.append(v + 1)

    cycle = []
    visit(0)
    return cycle[:-1]


v, e = map(int, input().split())
graph = [[] for _ in range(v)]
for _ in range(e):
    x, y = map(int, input().split())
    graph[x - 1].append(y - 1)
    graph[y - 1].append(x - 1)

if is_eulerian(graph):
    print(*eulerial_cycle(graph))
else:
    print('NONE')