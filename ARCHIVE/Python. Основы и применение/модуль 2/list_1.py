x = [-2, -1, 0, 1, 2]
y = [i * i for i in x]
print(y)
w = [i * i for i in x if 0 < i]
print(w)
z = [(x, y) for x in range(3) for y in range(3) if y >= x]
print(z)

g = ((x, y) for x in range(3) for y in range(3) if y >= x)
print(g)
print(next(g))
print(next(g))

while True:
    try:
        print(next(g))
    except StopIteration:
        break
        
print(list(i + 1 for i in range(4)))
print(type(i + 1 for i in range(4)))

*a, = range(5)[1:]
print(a)