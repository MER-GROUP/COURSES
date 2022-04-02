x = [1, 2, 3]
x.append(4)
x += [5]
x += list([6])
print(x)
top = x.pop()
print(x)
print(top)
top = x.pop()
print(x)
print(top)