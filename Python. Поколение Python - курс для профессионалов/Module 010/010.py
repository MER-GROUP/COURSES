'''
Функция is_iterator()
Реализуйте функцию is_iterator(), которая принимает один аргумент:

obj — произвольный объект

Функция должна возвращать True, если объект obj является итератором, 
или False в противном случае. 

Примечание 1. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию is_iterator(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/668595/tests_2768794.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.3/Module_10.3.15

Sample Input 1:
print(is_iterator([1, 2, 3, 4, 5]))
Sample Output 1:
False

Sample Input 2:
beegeek = map(str.upper, 'beegeek')
print(is_iterator(beegeek))
Sample Output 2:
True

Sample Input 3:
beegeek = filter(None, [0, 0, 1, 1, 0, 1])
print(is_iterator(beegeek))
Sample Output 3:
True
'''
from _collections_abc import Iterator
# from collections.abc import Iterator

def is_iterator(obj: object) -> bool:
    return isinstance(obj, Iterator)

if __name__ == '__main__':
    print(is_iterator([1, 2, 3, 4, 5]))

    beegeek = map(str.upper, 'beegeek')
    print(is_iterator(beegeek))

    beegeek = filter(None, [0, 0, 1, 1, 0, 1])
    print(is_iterator(beegeek))