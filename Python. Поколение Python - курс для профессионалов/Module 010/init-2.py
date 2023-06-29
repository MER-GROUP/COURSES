print('------------------')

numbers = [-3, 6, 1, -90, 34, -25, 23, -21]

# создаем объект итератора
positive_numbers = map(abs, numbers)     

# обходим итератор циклом for
for num in positive_numbers:             
    print(num)

print('------------------')

numbers = [-3, 6, 1, -90, 34, -25, 23, -21]

# создаем объект итератора
positive_numbers = map(abs, numbers)     

# обходим итератор циклом for
for num in positive_numbers:             
    print(num)

# обходим пустой итератор, тело цикла выполнено не будет
for num in positive_numbers:             
    print(num)

print('------------------')

# numbers = [-3, 6, 1, -90, 34, -25, 23, -21]

# # создаем объект итератора
# positive_numbers = map(abs, numbers)     

# # обходим итератор циклом for
# for num in positive_numbers:             
#     print(num)

# # пытаемся получить элемент из пустого итератора
# print(next(positive_numbers))            

print('------------------')

numbers = [-3, 6, 1, -90, 34, -25, 23, -21]

# создаем объект итератора
positive_numbers = map(abs, numbers)       
# преобразуем итератор в список          
positive_numbers_list = list(positive_numbers)       

print(positive_numbers_list)

print('------------------')

numbers = [-3, 6, 1, -90, 34, -25, 23, -21]

# создаем объект итератора
positive_numbers = map(abs, numbers)  

# преобразуем итератор в список
positive_numbers_list1 = list(positive_numbers)  
# преобразуем пустой итератор в список     
positive_numbers_list2 = list(positive_numbers)       

print(positive_numbers_list1)
print(positive_numbers_list2)

print('------------------')

numbers = [4, 8, 15, 16, 23, 42]

# создаем итератор на основе списка
iterator = iter(numbers)              

print(15 in iterator)

print('------------------')

numbers = [4, 8, 15, 16, 23, 42]

# создаем итератор на основе списка
iterator = iter(numbers)              

print(15 in iterator)
print(15 in iterator)

print('------------------')

numbers = [4, 8, 15, 16, 23, 42]

# создаем итератор на основе списка
iterator = iter(numbers)              

print(15 in iterator)
print(23 in iterator)

print('------------------')

numbers = [4, 8, 15, 16, 23, 42]

# создаем итератор на основе списка
iterator = iter(numbers)              

print(*iterator)
print(list(iterator))

print('------------------')

people = {'name': 'Timur', 'age': 29, 'gender': 'male', 'profession': 'teacher'}

for key in people:
    print(key)

print('------------------')

people = {'name': 'Timur', 'age': 29, 'gender': 'male', 'profession': 'teacher'}

print(*people)

print('------------------')

numbers = [4, 8, 15, 16, 23, 42]

print(15 in numbers)
print(8 in numbers)
print(15 in numbers)
print(42 in numbers)

print('------------------')

numbers = [4, 8, 15, 16, 23, 42]

# создаем итератор на основе списка
iterator = iter(numbers)              

print(15 in iterator)
print(8 in iterator)
print(15 in iterator)
print(42 in iterator)

print('------------------')

non_zero = filter(None, [-2, -1, 0, 1, 2])
positive = map(abs, non_zero)

# print(list(non_zero))
# print(list(positive))
# print(list(non_zero))
print(next(positive))
print(next(non_zero))
print(next(positive))
print(next(non_zero))

print('------------------')