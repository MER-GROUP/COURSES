'''
Функция get_value()
Реализуйте функцию get_value(), которая принимает три аргумента в следующем порядке:

chainmap — объект типа ChainMap, элементами которого являются словари
key — произвольный объект
from_left — булево значение, по умолчанию равное True

Функция должна возвращать значение по ключу key из chainmap, причем:

если from_left имеет значение True, поиск ключа в chainmap должен происходить 
от первого словаря к последнему
если from_left имеет значение False, поиск ключа в chainmap должен происходить 
от последнего словаря к первому
Если ключ key отсутствует в chainmap, функция должна вернуть значение None.

Примечание 1. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию get_value(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/743710/tests_3096396.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_6/Module_6.10/Module_6.10.15

Sample Input 1:
chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
print(get_value(chainmap, 'name'))
Sample Output 1:
Arthur

Sample Input 2:
chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
print(get_value(chainmap, 'name', False))
Sample Output 2:
Timur

Sample Input 3:
chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
print(get_value(chainmap, 'age'))
Sample Output 3:
None
'''
from collections import ChainMap       

def get_value(chainmap: ChainMap, key: str, from_left: bool=True) -> (str | None):
    if key not in chainmap:
        return None
    elif from_left:
        for _dict in chainmap.maps:
            if key in _dict:
                return _dict[key]
    else:
        for _dict in reversed(chainmap.maps):
            if key in _dict:
                return _dict[key]

if __name__ == '__main__':
    chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
    print(get_value(chainmap, 'name'))

    chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
    print(get_value(chainmap, 'name', False))

    chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
    print(get_value(chainmap, 'age'))