# Методы словарей
# Добавление и изменение элементов в словаре
print('####################')
info = {'name': 'Sam',
        'age': 28,
        'job': 'Teacher'}
# изменяем значение по ключу name 
info['name'] = 'Timur'
# добавляем в словарь элемент с ключом email
info['email'] = 'timyr-guev@yandex.ru'
print(info)

# задача - поиск повторяющихся чисел
print('####################')
numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
result = {}
# будет ошибка KeyError
# for num in numbers:
    # result[num] += 1
# все ок
for num in numbers:
    if num not in result:
        result[num] = 1
    else:
        result[num] += 1
print(result)

# Метод get()
print('####################')
info = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}
print(info['name'])
print('####################')
info = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}
# ошибка KeyError
# print(info['salary'])
print('####################')
info = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}
item1 = info.get('salary')
item2 = info.get('salary', 'Информации о зарплате нет')
print(item1)
print(item2)

# задача - поиск повторяющихся чисел
# ревью кода
print('####################')
numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
result = {}
for num in numbers:
    result[num] = result.get(num, 0) + 1
print(result)

# Метод update()
# Метод update() – реализует своеобразную операцию конкатенации для словарей. Он объединяет ключи и значения одного словаря с ключами и значениями другого. При совпадении ключей в итоге сохранится значение словаря, указанного в качестве аргумента метода update()
print('####################')
info1 = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}
info2 = {'age': 30,
        'city': 'New York',
        'email': 'bob@web.com'}
info1.update(info2)
print(info1)

# В Python 3.9 появились операторы | и |= которые реализуют операцию конкатенации словарей.
print('####################')
info1 = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}
info2 = {'age': 30,
        'city': 'New York',
        'email': 'bob@web.com'}
info1 |= info2
print(info1)

# Метод setdefault()
# Метод setdefault() позволяет получить значение из словаря по заданному ключу, автоматически добавляя элемент словаря, если он отсутствует.
# Метод принимает два аргумента:
# key: ключ, значение по которому следует получить, если таковое имеется в словаре, либо создать.
# default: значение, которое будет использовано при добавлении нового элемента в словарь.
print('####################')
info = {'name': 'Bob', 'age': 25}
# параметр default не задан
name1 = info.setdefault('name')
# параметр default задан
name2 = info.setdefault('name', 'Max')
print(name1)
print(type(name1))
print(name2)
print(type(name2))
print('####################')
info = {'name': 'Bob', 'age': 25}
job = info.setdefault('job', 'Dev')
print(info)
print(type(info))
print(job)
print(type(job))
# если значение default не передано в метод, то вставится значение None
print('####################')
info = {'name': 'Bob', 'age': 25}
job = info.setdefault('job')
print(info)
print(job)

# Удаление элементов из словаря
# Оператор del
print('####################')
info = {'name': 'Sam',
        'age': 28,
        'job': 'Teacher',
        'email': 'timyr-guev@yandex.ru'}
# удаляем элемент имеющий ключ email
del info['email']
# удаляем элемент имеющий ключ job
del info['job']
# Если удаляемого ключа в словаре нет, возникнет ошибка KeyError
# del info['job']
print(info)

# Метод pop()
print('####################')
# получение самого значение удаляемого элемента
info = {'name': 'Sam',
        'age': 28,
        'job': 'Teacher',
        'email': 'timyr-guev@yandex.ru'}
# удаляем элемент по ключу email, возвращая его значение
email = info.pop('email')
# удаляем элемент по ключу job, возвращая его значение
job = info.pop('job')
print(email)
print(job)
print(info)
# если удаляемого ключа в словаре нет, возникнет ошибка KeyError.
# ​Чтобы ошибка не появлялась, этому методу можно передать второй аргумент. Он будет возвращен, если указанного ключа в словаре нет. Это позволяет реализовать безопасное удаление элемента из словаря:
# Если ключа surname в словаре нет, то в переменной surname будет храниться значение None.
surname = info.pop('surname', None) 
print(surname)

# Метод popitem()
# Метод popitem() удаляет из словаря последний добавленный элемент и возвращает удаляемый элемент в виде кортежа (ключ, значение).
# В версиях Python ниже 3.6 метод popitem() удалял случайный элемент.
print('####################')
info = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}
info['surname'] = 'Sinclar'
item = info.popitem()
print(item)
print(info)

# Метод clear()
# Метод clear() удаляет все элементы из словаря.
print('####################')
info = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}
info.clear()
print(info)

# Метод copy()
# Метод copy() создает поверхностную копию словаря.
print('####################')
info = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}
info_copy = info.copy()
print(info_copy)
# Не стоит путать копирование словаря (метод copy()) и присвоение новой переменной ссылки на старый словарь
print('####################')
info = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}
new_info = info
new_info['name'] = 'Tim'
print(info)
# Если необходимо изменить один словарь, не изменяя второй, используют метод copy().
print('####################')
info = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}
new_info = info.copy()
new_info['name'] = 'Tim'
print(info)
print(new_info)

# Примечание 1. Словарь можно использовать вместо нескольких вложенных условий, если вам нужно проверить число на равенство.
# Например вместо 
print('####################')
num = 3
if num == 1:
    description = 'One'
elif num == 2:
    description = 'Two'
elif num == 3:
    description = 'Three'
else:
    description = 'Unknown'
print(description)
# можно написать
print('####################')
num = 3
description = {1: 'One', 2: 'Two', 3: 'Three'}
print(description.get(num, 'Unknown'))