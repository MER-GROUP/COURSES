coords = list(map(int, input().split()))
colors = input().split()

d = dict()
for i in range(len(colors)):
    d[colors[i]] = d.get(colors[i], []) + [coords[i]]

res = max(map(lambda x: max(x) - min(x), d.values()))
print(res)