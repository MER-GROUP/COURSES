# авторский алгоритм от BEEGIK
def beegeek(a, b):
    result = []
    for i in range(a, b + 1):
        if i % 21 == 0:
            result.append('BeeGeek')
        elif i % 7 == 0:
            result.append('Geek')
        elif i % 3 == 0:
            result.append('Bee')
        else:
            result.append(str(i))
    return ' '.join(result)

print(beegeek(14, 21))
print(beegeek(1, 2))
print(beegeek(10, 50))