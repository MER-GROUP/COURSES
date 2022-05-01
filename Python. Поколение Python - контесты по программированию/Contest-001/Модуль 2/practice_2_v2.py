def beegeek(a, b):
	return ' '.join(('Bee' * (i % 3 == 0) + 'Geek' * (i % 7 == 0) or str(i)) for i in range(a, b + 1))

def beegeek2(a, b):
    result = [i for i in range(a, b + 1)]
    result = map(lambda x: 'BeeGeek' if x % 3 == 0 and x % 7 == 0 else x, result)
    result = map(lambda x: 'Bee' if isinstance(x, int) and x % 3 == 0 else x, result)
    result = map(lambda x: 'Geek' if isinstance(x, int) and x % 7 == 0 else x, result)
    return ' '.join(list(map(str, result)))

print(beegeek(14, 21))
print(beegeek(1, 2))
print(beegeek(10, 50))