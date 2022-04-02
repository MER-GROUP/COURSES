x = [1, 2, 3]
print(id(x))
print(id([1, 2, 3]))
y = x
print(id(y))
print(x is y)
print([1,2,3] is x)
x.append(4)
print(x)
print(y)