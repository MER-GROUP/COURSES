'''
Вам доступна переменная data, содержащая Counter словарь. 
Дополните приведенный ниже код, чтобы он добавил этому словарю два атрибута:

min_values() — функция, которая возвращает список элементов, имеющих наименьшее значение
max_values() — функция, которая возвращает список элементов, имеющих наибольшее значение

Обе функции не должны принимать никаких аргументов.

Примечание 1. Элементом словаря будем считать кортеж (ключ, значение).

Примечание 2. Элементы словаря в возвращаемых функциями списках должны располагаться 
в своем исходном порядке.

Примечание 3. Функции data.min_values() и data.max_values() должны учитывать содержимое словаря. 
Например, если в словарь data будет добавлена новая пара ключ-значение, то и в возвращаемых 
функциями списках данные ключ и значение должны присутствовать.

Примечание 4. Программа ничего не должна выводить.

Примечание 5. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/635441/tests_3091741.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_6/Module_6.8/Module_6.8.17

Sample Input 1:
print(data.max_values())
Sample Output 1:
[('j', 8), ('q', 8)]

Sample Input 2:
print(data.min_values())
Sample Output 2:
[('t', 1)]
'''
from collections import Counter, defaultdict, namedtuple

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.__dict__['min_values'] = lambda: [
    i for i in data.most_common() if i[1] == min(data.values())
]
data.max_values = lambda: [
    i for i in data.most_common() if i[1] == max(data.values())
]

if __name__ == '__main__':
    # print(data.most_common())
    print(data.max_values())
    print(data.min_values())