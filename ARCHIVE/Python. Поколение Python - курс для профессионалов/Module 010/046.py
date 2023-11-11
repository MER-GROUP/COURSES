'''
Функция with_previous()
Реализуйте генераторную функцию, которая принимает один аргумент:

iterable — итерируемый объект

Функция должна возвращать генератор, порождающий последовательность кортежей, 
каждый из которых содержит очередной элемент итерируемого объекта iterable, 
а также предшествующий ему элемент:

(<очередной элемент>, <предыдущий элемент>)

Для первого элемента предыдущим считается значение None.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе 
должны располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, 
не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию with_previous(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/673155/tests_3149804.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.7/Module_10.7.21

Sample Input 1:
numbers = [1, 2, 3, 4, 5]
print(*with_previous(numbers))
Sample Output 1:
(1, None) (2, 1) (3, 2) (4, 3) (5, 4)

Sample Input 2:
iterator = iter('stepik')
print(*with_previous(iterator))
Sample Output 2:
('s', None) ('t', 's') ('e', 't') ('p', 'e') ('i', 'p') ('k', 'i')
'''
from _collections_abc import Generator, Iterable

def with_previous(iterable: Iterable) -> Generator:
    prev = None

    for i in iterable:
        yield from [(i, prev)]
        prev = i

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    print(*with_previous(numbers))

    iterator = iter('stepik')
    print(*with_previous(iterator))