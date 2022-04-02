a = [1, 5, 'g', 5, 'h']
b = [5, 0, 1, 'u', 'g']
print(a)
print(b)
print(set(a))
print(set(b))
myList = list(set(a) & set(b))
print(myList)