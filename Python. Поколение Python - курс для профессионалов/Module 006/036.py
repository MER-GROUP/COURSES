'''
Функция deep_update()
Реализуйте функцию deep_update(), которая принимает три аргумента в следующем порядке:

chainmap — объект типа ChainMap, элементами которого являются словари
key — хешируемый объект
value — произвольный объект

Функция должна изменять все значения по ключу key во всех словарях в chainmap на value. 
Если ключ key отсутствует в chainmap, функция должна добавить пару key: value в первый словарь.

Примечание 1. Функция должна изменять передаваемый объект типа ChainMap и возвращать 
значение None.

Примечание 2. Гарантируется, что передаваемый в функцию объект типа ChainMap содержит 
хотя бы один словарь.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию deep_update(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/743710/tests_3096398.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_6/Module_6.10/Module_6.10.14

Sample Input 1:
chainmap = ChainMap({'city': 'Moscow'}, {'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'name', 'Dima')
print(chainmap)
Sample Output 1:
ChainMap({'city': 'Moscow'}, {'name': 'Dima'}, {'name': 'Dima'})

Sample Input 2:
chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'age', 20)
print(chainmap)
Sample Output 2:
ChainMap({'name': 'Arthur', 'age': 20}, {'name': 'Timur'})
'''
from collections import ChainMap       

pass