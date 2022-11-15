my_set = set()
my_set.add('red')
my_set.add('alert')
print(my_set)

print('------------------')

my_tuple = (1, 2, 3)
print(my_tuple)
print(type(my_tuple))
print(str(my_tuple))
print(type(str(my_tuple)))

print('------------------')

arr = [1, 2, 3, 4, 5]
arr_sub = [2, 3]
print(set(arr_sub).issubset(arr))
arr = ['1', '2', '3', '4', '5']
arr_sub = ['2', '3']
print(set(arr_sub).issubset(arr))
arr = ['1', '2', '3', '4', '5']
arr_sub = ['2', '3', '25']
print(set(arr_sub).issubset(arr))
arr = ['1', '2', '3', '4', '5']
arr_sub = ['2', '45', '3']
print(set(arr_sub).issubset(arr))
arr = ['1', '2', '3', '4', '5']
arr_sub = ['2', '45', '3']
print(set(arr_sub).intersection(arr))
arr = ['454']
arr_sub = ['2', '45', '3']
print(set(arr_sub).intersection(arr))

print('------------------')

word = '12345'
for i in range(len(word)-1, -1, -1):
    print(word[i], end='')
print()

print('------------------')

s = [1, 1, 0, 0, 1]
print(s[ : len(s) - s[::-1].index(1)])

print('------------------')

digits = '0123456789'
name = 'max274'
name = name.rstrip(digits)
print(name)