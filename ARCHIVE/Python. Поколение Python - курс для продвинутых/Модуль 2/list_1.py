# объединение списков
list1 = ['a', 'b', 'c', 'd']
list2 = ['e', 'f', 'g']
list3 = list()

# вызов документации
print(list3.extend.__doc__)
#list3 = list1.extend(list2)

# не возвращает новый список
list1.extend(list2)
print(list1)

# возвращает новый список
list3 = list1 + list2
print(list3)