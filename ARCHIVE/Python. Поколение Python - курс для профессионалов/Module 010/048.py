'''
Функция around()
Реализуйте генераторную функцию, которая принимает один аргумент:

iterable — итерируемый объект

Функция должна возвращать генератор, порождающий последовательность кортежей, каждый из 
которых содержит очередной элемент итерируемого объекта iterable, а также предыдущий 
и следующий за ним элементы:

(<предыдущий элемент>, <очередной элемент>, <следующий элемент>)

Для первого элемента предыдущим считается значение None, для последнего элемента 
следующим считается так же значение None.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе 
должны располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, 
не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию around(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/673155/tests_3149810.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.7/Module_10.7.23

Sample Input 1:
numbers = [1, 2, 3, 4, 5]
print(*around(numbers))
Sample Output 1:
(None, 1, 2) (1, 2, 3) (2, 3, 4) (3, 4, 5) (4, 5, None)

Sample Input 2:
iterator = iter('hey')
print(*around(iterator))
Sample Output 2:
(None, 'h', 'e') ('h', 'e', 'y') ('e', 'y', None)
'''
from _collections_abc import Generator, Iterable

def around(iterable: Iterable) -> Generator:
    if iterable:
        it = iter(iterable)
        _prev = None
        _cur = next(it, None)
        _next = next(it, None)
        while not _cur is None:
            yield _prev, _cur, _next
            _prev, _cur, _next = _cur, _next, next(it, None)
    else:
        yield from iterable

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    print(*around(numbers))

    iterator = iter('hey')
    print(*around(iterator))