import sys

def readGraph(num_vert, num_edges, reader):
    graph = {i: [] for i in range(1, num_vert + 1)}

    for _ in range(num_edges):
        u, v = next(reader)
        graph[u].append(v)
        graph[v].append(u)

    return graph

def findEulerCicle(graph, s):
    for v in graph:
        if not len(graph[v]) or (len(graph[v]) % 2):
            return "NONE"
    circle = []
    stack = [s]
    g = graph.copy()

    while stack:
        x = stack[len(stack) - 1]
        if g[x]:
            v = g[x].pop(0)
            g[v].pop(g[v].index(x))
            stack.append(v)
        else:
            x = stack.pop()
            circle.append(x)
    circle.pop()
    for v in graph:
        if v not in circle:
            return "NONE"
    circle = " ".join(map(str, circle))
    return circle

def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, m = next(reader)
    graph = readGraph(n, m, reader)
    print(findEulerCicle(graph, 1))

if __name__ == "__main__":
    main()