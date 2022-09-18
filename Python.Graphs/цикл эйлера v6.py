from collections import defaultdict, Counter
import sys
sys.setrecursionlimit(100000000)
 
 
def rek(ar, cur, res):
    for x in ar[cur]:
        if ar[cur][x] > 0:
            ar[cur][x] -= 1
            ar[x][cur] -= 1
            res = rek(ar, x, res)
    return res + [cur]
 
 
n, e = map(int, input().split())
ar = defaultdict(Counter)

for _ in range(e):
    a, b = map(int, input().split())
    ar[a][b] += 1
    ar[b][a] += 1

res = rek(ar, 1, [])
print('NONE' if res[0] != res.pop() or len(set(res)) != n else ' '.join(map(str, res)))