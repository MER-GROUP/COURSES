file = open('file_test.txt', 'r')
'''
x = file.read(5)
print(x)
y = file.read()
print(y)
print(repr(y))
z = y.splitlines()
print(z)
print(type(z))

w = file.readline().rstrip()
#w = w.rstrip()
print(repr(w))
w = file.readline()
print(repr(w))
'''
for line in file:
    line = line.rstrip()
    print(repr(line))
    
x = file.read()
print(repr(x))

file.close()