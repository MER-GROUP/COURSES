# авторское решение
# Решение. Для каждого цвета в словаре храним координату первого вхождения. 
# Если текущий ключ есть в словаре, значит там лежит первая координата 
# и можно попробовать обновить максимум, если же ключа нет в словаре, 
# то нужно добавить этот ключ со значением соответствующей координаты.
houses = [int(i) for i in input().split()]
colors = [i for i in input().split()]
distance = {}
maxi = 0

for key in range(len(colors)):
    if colors[key] not in distance:
        distance[colors[key]] = houses[key]
    else:
        maxi = max(maxi, houses[key] - distance[colors[key]])
print(maxi)