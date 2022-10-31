v = {}
for key, value in zip([int(x) for x in input().split()], input().split()):
    v.setdefault(value, []).append(key)
print(max([max(v)-min(v) for v in v.values()]))