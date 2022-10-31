houses = list(map(int, input().split()))
colors = input().split()

d = {}
for i, n in enumerate(colors):  # создаем словарь, где ключи - цвета, а 
    d.setdefault(n, list()).append(houses[i])  # значения - списки координат
    
res = 0                         # в res лежит 0
for v in d.values():            # перебираем по значениям.
    if max(v) - min(v) > res:   # если разница между max и min > res
        res = max(v) - min(v)   # заносим разницу в res
print(res)