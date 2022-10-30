import itertools as it

arr = [10, 20, 30]
arr = [1, 2, 3, 4, 6]
arr = [5, 8, 9]
arr = [4, 6]
arr = [4, 2, 5, 2, 7, 3, 9, 3, 6, 2, 3, 43, 1, 44, 123, 1]

for el in it.permutations(arr):
    print(el)
    i = 1
    check = False
    for _ in el:
        print(el[ : i])
        print(el[i : ])
        x = sum(el[ : i])
        y = sum(el[i : ])
        print('x =', x)
        print('y =', y)
        if (x == y):
            check = True
            print('True')
            break
        i += 1
    if check: break    
else:
    print('False')