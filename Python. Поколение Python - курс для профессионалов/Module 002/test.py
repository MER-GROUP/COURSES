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