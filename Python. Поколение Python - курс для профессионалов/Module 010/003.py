'''
Функция filterfalse()

Реализуйте функцию filterfalse() с использованием функции filter(), 
которая принимает два аргумента:

predicate — функция-предикат; если имеет значение None, 
то работает аналогично функции bool()
iterable — итерируемый объект

Функция должна работать противоположно функции filter(), 
то есть возвращать итератор, элементами которого являются элементы 
итерируемого объекта iterable, для которых функция predicate вернула значение False.

Примечание 1. Предикат — это функция, которая возвращает 
True или False в зависимости от переданного в качестве аргумента значения.

Примечание 2. Элементы итерируемого объекта в возвращаемом 
функцией итераторе должны располагаться в своем исходном порядке.

Примечание 3. Гарантируется, что итерируемый объект, 
передаваемый в функцию, не является множеством.

Примечание 4. В тестирующую систему сдайте программу, 
содержащую только необходимую функцию filterfalse(), 
но не код, вызывающий ее.

Примечание 5. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640044/tests_2768652.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.2/Module_10.2.20

Sample Input 1:
objects = [0, 1, True, False, 17, []]
print(*filterfalse(None, objects))
Sample Output 1:
0 False []

Sample Input 2:
numbers = (1, 2, 3, 4, 5)
print(*filterfalse(lambda x: x % 2 == 0, numbers))
Sample Output 2:
1 3 5

Sample Input 3:
numbers = [1, 2, 3, 4, 5]
print(*filterfalse(lambda x: x >= 3, numbers))
Sample Output 3:
1 2
'''
def filterfalse(predicate, iterable):
    ...

if __name__ == '__main__':
    objects = [0, 1, True, False, 17, []]
    print(*filterfalse(None, objects))

    numbers = (1, 2, 3, 4, 5)
    print(*filterfalse(lambda x: x % 2 == 0, numbers))

    numbers = [1, 2, 3, 4, 5]
    print(*filterfalse(lambda x: x >= 3, numbers))