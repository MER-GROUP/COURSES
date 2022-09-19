from functools import reduce
import operator as op

n, e = map(int, input().split())
v = [[0] * n for _ in range(n)]

for _ in range(e):
    x, y = map(int, input().split())
    v[x-1][y-1] += 1
    v[y-1][x-1] += 1

exist = True
for x in v:
    pw = reduce(op.add, x)
    if pw == 0 or pw % 2 == 1:
        exist = False
        break
        
if not exist:
    print("NONE")
else:
    cycle = [0]
    i = 0
    while i < len(cycle):
        nex = cycle[i]
        pw = reduce(op.add, v[nex])
        if pw == 0:
            i += 1
            continue
        
        subcycle = []
        while True:
            for j in range(n):
                if v[nex][j] > 0:
                    v[nex][j] -= 1
                    v[j][nex] -= 1
                    nex = j
                    break
            if nex == cycle[i]:
                cycle = cycle[:i+1] + subcycle + [cycle[i]] + cycle[i+1:]
                i = 0
                break
            else:
                subcycle.append(nex)
    print(' '.join([str(x + 1) for x in cycle[:-1]]))