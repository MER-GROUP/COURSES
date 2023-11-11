'''
Функция unique()
Реализуйте генераторную функцию, которая принимает один аргумент:

iterable — итерируемый объект

Функция должна возвращать генератор, порождающий последовательность элементов 
итерируемого объекта iterable без дубликатов.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе 
должны располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, 
не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию unique(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/673155/tests_3149807.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.7/Module_10.7.19

Sample Input 1:
numbers = [1, 2, 2, 3, 4, 5, 5, 5]
print(*unique(numbers))
Sample Output 1:
1 2 3 4 5

Sample Input 2:
iterator = iter('111222333')
uniques = unique(iterator)
print(next(uniques))
print(next(uniques))
print(next(uniques))
Sample Output 2:
1
2
3
'''
from _collections_abc import Generator, Iterable

def unique(iterable: Iterable) -> Generator:
    repeats = set()
    for i in iterable:
        if not i in repeats:
            yield i
            repeats.add(i)

if __name__ == '__main__':
    numbers = [1, 2, 2, 3, 4, 5, 5, 5]
    print(*unique(numbers))

    iterator = iter('111222333')
    uniques = unique(iterator)
    print(next(uniques))
    print(next(uniques))
    print(next(uniques))