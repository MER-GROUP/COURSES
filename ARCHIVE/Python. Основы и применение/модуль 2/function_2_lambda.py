x = input().split()
xs = (int(i) for i in x)

#even = lambda x: 0 == x % 2

print(list(filter(lambda x: 0 == x % 2, xs)))