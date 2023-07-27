'''
Функция flatten()
Реализуйте генераторную функцию flatten(), которая принимает один аргумент:

nested_list — список, элементами которого являются целые числа или списки, 
элементами которых, в свою очередь, также являются либо целые числа, либо списки; 
вложенность может быть произвольной
Функция должна возвращать генератор, порождающий все числа, содержащиеся в nested_list, 
включая все числа из всех вложенных списков, а затем возбуждает исключение StopIteration.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую 
генераторную функцию flatten(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640048/tests_2777688.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.5/Module_10.5.27

Sample Input 1:
generator = flatten([[1, 2], [[3]], [[4], 5]])
print(*generator)
Sample Output 1:
1 2 3 4 5

Sample Input 2:
generator = flatten([1, 2, 3, 4, 5, 6, 7])
print(*generator)
Sample Output 2:
1 2 3 4 5 6 7
'''

from __future__ import annotations
from _collections_abc import Generator

def flatten(nested_list: list) -> Generator:
    for _list in nested_list:
        if isinstance(_list, list):
            yield from flatten(_list)
        else:
            yield _list
            
if __name__ == '__main__':
    generator = flatten([[1, 2], [[3]], [[4], 5]])
    print(*generator)

    generator = flatten([1, 2, 3, 4, 5, 6, 7])
    print(*generator)