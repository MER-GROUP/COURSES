a=input()
b=sorted([a.count(i) for i in set(a) if a.count(i)%2!=0])
print(sum([a.count(i) for i in set(a) if a.count(i)%2==0])+ sum([i-1 for i in b[:-1]])+ b[-1])