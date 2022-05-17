a=list(map(int, input().split()))
b=input().split()
s=[i for i in set(b) if b.count(i)>1]
print(max([a[::-1][b[::-1].index(i, 0, -1)]- a[b.index(i, 0, -1)] for i in s]) if len(s) else 0)