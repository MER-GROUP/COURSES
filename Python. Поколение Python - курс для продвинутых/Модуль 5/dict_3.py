# Функция len()
print('####################')
fruits = {'Apple': 70, 'Grape': 100, 'Banana': 80}
capitals = {'Россия': 'Москва', 'Франция': 'Париж'}
print(len(fruits))
print(len(capitals))

# Оператор принадлежности in
print('####################')
capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
if 'Франция' in capitals:
    print('Столица Франции - это', capitals['Франция'])
# KeyError: 'Англия'
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# print(capitals['Англия'])

# Встроенные функции sum(), min(), max()
# Встроенная функция sum()
print('####################')
my_dict = {10: 'Россия', 20: 'США', 30: 'Франция'}
print('Сумма всех ключей словаря =', sum(my_dict))

# Встроенные функции min() и max()
print('####################')
capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
months = {1: 'Январь', 2: 'Февраль', 3: 'Март'}
print('Минимальный ключ =', min(capitals))
print('Максимальный ключ =', max(months))

# Сравнение словарей
print('####################')
months1 = {1: 'Январь', 2: 'Февраль'}
months2 = {1: 'Январь', 2: 'Февраль', 3: 'Март'}
months3 = {3: 'Март', 1: 'Январь', 2: 'Февраль'}
print(months1 == months2)
print(months2 == months3)
print(months1 != months3)

# Примечание 1. Обращение по индексу и срезы недоступны для словарей.

# Примечание 2. Операция конкатенации + и умножения на число * недоступны для словарей.

'''
Примечание 3. Словари нужно использовать в следующих случаях:

Подсчет числа каких-то объектов. В этом случае нужно завести словарь, в котором ключи — названия объектов, а значения — их количество.
Хранение каких-либо данных, связанных с объектом. Ключи — наименования объектов, значения — связанные с ними данные. Например, если нужно по названию месяца определить его порядковый номер, то это можно сделать при помощи словаря num = {'January': 1, 'February': 2, 'March': 3, ...}.
Установка соответствия между объектами (например, “родитель—потомок”). Ключ — объект, значение — соответствующий ему объект.
Если нужен обычный список, где максимальное значение индекса элемента очень велико, но при этом используются не все возможные индексы (так называемый “разреженный список”), то для экономии памяти можно использовать словарь.
'''