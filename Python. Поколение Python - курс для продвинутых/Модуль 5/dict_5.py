# Перебор элементов словаря
# вывод ключей словаря на отдельной строке
print('####################')
capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
for key in capitals:
    print(key)
    
# вывод значений словаря каждого на отдельной строке
print('####################')
capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
for key in capitals:
    print(capitals[key])
    
# вывод элементов словаря каждого на отдельной строке
print('####################')
capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
for key in capitals:
    print('Столица', key, '- это', capitals[key])
    
# Методы keys(), values(), items()
# Словарный метод keys() возвращает список ключей всех элементов словаря
print('####################')
capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# итерируем по списку ['Россия', 'Франция', 'Чехия']
for key in capitals.keys():
    print(key)
    
# Словарный метод values() возвращает список значений всех элементов словаря
print('####################')
capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# итерируем по списку ['Москва', 'Париж', 'Прага']
for value in capitals.values():
    print(value)
    
# Словарный метод items() возвращает список всех элементов словаря, состоящий из кортежей пар (ключ, значение)
print('####################')
capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
for item in capitals.items():
    print(item)
print('####################')
capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
for key, value in capitals.items():
    print(key, '-', value)
    
# Распаковка ключей словаря
print('####################')
capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
print(*capitals, sep='\n')
print('####################')
print(*capitals.keys(), sep='\n')

# Сортировка словаря
# Сортировка по ключам выполняется с использованием функции sorted()
# Словари не содержат метода sort()
print('####################')
capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}
for key in sorted(capitals):
    print(key)
    
# Для сортировки словаря по значениям можно использовать функцию sorted() вместе с методом items()
print('####################')
capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}
for key, value in sorted(capitals.items(), key = lambda x: x[1]):
    print(value)
    
# Проверка наличия ключа в словаре
print('####################')
capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
if 'Россия' in capitals:
    print('В словаре есть ключ Россия')
    
# Проверка наличия значения в словаре
print('####################')
capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
if 'Париж' in capitals.values():
    print('В словаре есть значение Париж')
    
# Примечание 1. Встроенная функция sorted() имеет опциональный параметр reverse. Если установить этот параметр в значение True, то сортировка будет по убыванию

# Примечание 2. Код для работы со словарями нужно писать таким образом, чтобы он правильно работал при любом порядке обхода с помощью цикла for

# Примечание 3. Словарные методы items(), keys(), values() возвращают не совсем обычные списки. Типы этих списков -  dict_items, dict_keys, dict_values соответственно, в отличие от обычных списков - list. Методы обычных списков недоступны для списков типа dict_items, dict_keys, dict_values. Используйте явное преобразование с помощью функции list() для получения доступа к методам списков