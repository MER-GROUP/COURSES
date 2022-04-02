# Вложенные словари
# Создание вложенных словарей
print('####################')
info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}
print(info)

# Создание вложенных словарей
print('####################')
info = dict(emp1 = {'name': 'Timur', 'job': 'Teacher'},
            emp2 = {'name': 'Ruslan', 'job': 'Developer'},
            emp3 = {'name': 'Rustam', 'job': 'Tester'})
print(info)

# Создание вложенных словарей
print('####################')
ids = ['emp1', 'emp2', 'emp3']
emp_info = [{'name': 'Timur', 'job': 'Teacher'},
            {'name': 'Ruslan', 'job': 'Developer'},
            {'name': 'Rustam', 'job': 'Tester'}]
info = dict(zip(ids, emp_info))
print(info)

# Обращение к элементам вложенного словаря
print('####################')
info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}
print(info['emp1']['name'])
print(info['emp2']['job'])

# Изменение вложенных словарей
print('####################')
info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}

info['emp1']['job'] = 'Manager'
print(info['emp1'])

# Итерация по вложенным словарям
print('####################')
info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}
for emp in info:
    print('Employee ID:', emp)
    for key in info[emp]:
        print(key + ':', info[emp][key])
    print()
    
# Итерация по вложенным словарям
print('####################')
info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}
for emp, inf in info.items():
    print('Employee ID:', emp)
    for key in inf:
        print(key + ':', inf[key])
    print()
    
# Генераторы словарей
print('####################')
squares = {}
squares[0] = 0
squares[1] = 1
squares[2] = 4
squares[3] = 9
squares[4] = 16
squares[5] = 25
print(squares)

# Генераторы словарей
print('####################')
squares = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares)

# Генераторы словарей
print('####################')
squares = {}
for i in range(6):
    squares[i] = i**2
print(squares)

# Генераторы словарей
print('####################')
squares = {i: i**2 for i in range(6)}
print(squares)

# Примеры использования генератора словарей
# Генератор словаря при итерировании по строке
print('####################')
dct = {c: c * 3 for c in 'ORANGE'}
print(dct)

# Для вычисления ключа и значения в генераторе словаря могут быть использованы выражения
print('####################')
lst = ['ReD', 'GrEeN', 'BlUe']
dct = {c.lower(): c.upper() for c in lst}
print(dct)

# Извлечение из словаря элементов с определенными ключами
print('####################')
dict1 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
selected_keys = [0, 2, 5]
dict2 = {k: dict1[k] for k in selected_keys}
print(dict2)

# Условия в генераторе словарей
print('####################')
squares = {}
for i in range(10):
    if i % 2 == 0:
        squares[i] = i**2
print(squares)

# Условия в генераторе словарей
print('####################')
squares = {i: i**2 for i in range(10) if i % 2 == 0}
print(squares)

# Условия в генераторе словарей
print('####################')
squares = {i: i**2 for i in range(0, 10, 2)}
print(squares)

# Генераторы вложенных словарей
print('####################')
squares = {i: {j: j**2 for j in range(i + 1)} for i in range(5)}
for value in squares.values():
    print(value)