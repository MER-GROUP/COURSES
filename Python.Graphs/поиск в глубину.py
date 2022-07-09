from sys import stdin

input = stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for i in range(m):
	u, v = [int(i) - 1 for i in input().split()]
	graph[u].append(v)
	graph[v].append(u)

visited = [False] * n
answer = 0
for i in range(n):
	if visited[i]:
		continue
	answer += 1
	visited[i] = True
	queue = [i]
	while queue:
		v = queue.pop()
		for to in graph[v]:
			if not visited[to]:
				visited[to] = True
				queue.append(to)
print(answer)