'''
Задача 2. Напишите функцию key_difference(), которая принимает два словаря, 
находит различия между ними, и возвращает словарь с названиями ключей и с 
состоянием каждого ключа в виде его значения при переходе от первого 
словаря ко второму в формате:

added если ключа не было в первом словаре, но он появился во втором.
deleted если ключ был в первом словаре, но его не было во втором.
changed если ключ присутствует в обоих словарях, но значения различаются.
equal если ключ присутствует в обоих словарях и значения совпадают.
Возвращать ключи следует в порядке их появления.

Гарантируется, что ключи и значения представлены исключительно 
в строковом типе данных.
'''
'''
в начале забыл что множество не упорядоченное.. переделал без множества
'''
def key_difference(dict1, dict2):
    list1 = list(dict1.keys())
    list2 = list(dict2.keys())
    res = dict()
    for key in list1:
        if key in list2 and dict1[key] == dict2[key]:
            res[key] = 'equal'
        elif key not in list2:
            res[key] = 'deleted'
        elif key in list2 and not dict1[key] == dict2[key]:
            res[key] = 'changed'
    added = list(set(list2) - set(list1))
    for key in added:
        res[key] = 'added'

    return res

dict1 = {'one': 'eon', 'two': 'two', 'four': 'True'}
dict2 = {'two': 'own', 'zero': '4', 'four': 'True'}
# dict1 = {'one': 'eon', 'two': 'two', 'four': 'True'}
# dict2 = {}
result = key_difference(dict1, dict2)
print(result)