# Дейкстра с восстановлением пути.
n = int(input())
m = [list(map(int, list(input()))) for i in range(n)]
graf, d, pr = {}, {}, {}
for i in range(n):
    for j in range(n):
        graf[(i,j)] = {}
        d[(i,j)] = 10**6 
        pr[(i,j)] = -1
        if j < n - 1:
            if m[i][j+1] > 0:
                graf[(i,j)][(i,j+1)] = m[i][j+1]
        if i < n - 1:    
            if m[i+1][j] > 0:
                graf[(i,j)][(i+1,j)] = m[i+1][j]
d[(0,0)] = 0
q = d.copy()
while q != {}:
    u = min(q, key=q.get)
    del q[u]
    for el, val in graf[u].items():
        if d[el] > d[u] + val:
            d[el] = d[u] + val
            q[el] = d[el]
            pr[el] = u
if m[0][0] == 0 or m[n-1][n-1] == 0 or d[(n-1,n-1)] == 10**6:
    print('Impossible')
else:
    rez = [list('-'*n) for i in range(n)]
    a = (n-1, n-1)
    rez[0][0] = '#'    
    while a != (0, 0):
        rez[a[0]][a[1]] = '#'
        a = pr[a]
    for i in range(n):
        print(''.join(rez[i]))