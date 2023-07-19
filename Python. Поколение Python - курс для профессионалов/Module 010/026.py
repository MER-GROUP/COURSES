'''
Функция reverse()
Реализуйте генераторную функцию reverse(), которая принимает один аргумент:

sequence — последовательность

Функция должна возвращать генератор, порождающий элементы последовательности sequence 
в обратном порядке, а затем возбуждающий исключение StopIteration.

Примечание 1. Последовательностью является коллекция, поддерживающая индексацию и имеющая длину. 
Например, объекты типа list, str, tuple являются последовательностями.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую генераторную 
функцию reverse(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640048/tests_2773011.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.5/Module_10.5.18

Sample Input 1:
print(*reverse([1, 2, 3, 4, 5]))
Sample Output 1:
5 4 3 2 1

Sample Input 2:
generator = reverse('beegeek')
print(type(generator))
print(*generator)
Sample Output 2:
<class 'generator'>
k e e g e e b
'''
from __future__ import annotations
from _collections_abc import Generator, Sequence

def reverse(sequence: Sequence) -> Generator:
    if isinstance(sequence, Sequence):
        index = len(sequence)
        while index:
            index -= 1
            yield sequence[index]
            
if __name__ == '__main__':
    print(*reverse([1, 2, 3, 4, 5]))

    generator = reverse('beegeek')
    print(type(generator))
    print(*generator)