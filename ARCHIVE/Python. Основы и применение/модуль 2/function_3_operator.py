import operator as op

print(op.add(4, 5))
print(op.mul(4, 5))
print(op.contains([1, 2, 3], 4))

x = [1, 2, 3]
x = {'123' : 5}
f = op.itemgetter('123')
print(f(x))

#y = [5, 9, 1]
f2 = op.attrgetter('sort')
print(f2([]))
#print(y)
#f2(y)
#print(y)

name = [('max', 'red', 'alert'), ('rich', 'rom'), ('drive', 'thief', 'rock')]
name.sort()
#name.sort(key=lambda x: x[-1])
name.sort(key=op.itemgetter(-1))
print(name)