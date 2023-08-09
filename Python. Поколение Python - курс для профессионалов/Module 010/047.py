'''
Функция pairwise()
Реализуйте генераторную функцию, которая принимает один аргумент:

iterable — итерируемый объект

Функция должна возвращать генератор, порождающий последовательность кортежей, 
каждый из которых содержит очередной элемент итерируемого объекта iterable, 
а также следующий за ним элемент:

(<очередной элемент>, <следующий элемент>)

Для последнего элемента следующим считается значение None.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе 
должны располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, 
не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию pairwise(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/673155/tests_3149809.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.7/Module_10.7.22

Sample Input 1:
numbers = [1, 2, 3, 4, 5]
print(*pairwise(numbers))
Sample Output 1:
(1, 2) (2, 3) (3, 4) (4, 5) (5, None)

Sample Input 2:
iterator = iter('stepik')
print(*pairwise(iterator))
Sample Output 2:
('s', 't') ('t', 'e') ('e', 'p') ('p', 'i') ('i', 'k') ('k', None)
'''
from _collections_abc import Generator, Iterable

def pairwise(iterable: Iterable) -> Generator:
    try:
        it = iter(iterable)
        _current = next(it)
        _next = next(it)

        for cur in it:
            yield _current, _next
            _next, _current = cur, _next

        yield _current, _next
        _next, _current = cur, _next
        yield _next, None
    
    except StopIteration:
        if not iterable:
            yield from iterable
        else:
            yield _current, None

if __name__ == '__main__':
    # 1
    numbers = [1, 2, 3, 4, 5]
    print(*pairwise(numbers))

    # 2
    iterator = iter('stepik')
    print(*pairwise(iterator))

    # 6
    iterator = pairwise('A')
    print(next(iterator))

    # 8
    print(list(pairwise([])))