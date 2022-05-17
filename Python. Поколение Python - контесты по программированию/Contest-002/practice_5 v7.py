x = list(map(int, input().split()))
dct = dict()
for i, c in enumerate(input().split()):
    if c in dct.keys():
        dct[c].append(x[i])
    else:
        dct[c] = [x[i]]
print(max(max(dct[i]) - min(dct[i]) for i in dct.keys()))