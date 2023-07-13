'''
Итератор Cycle
Реализуйте класс Cycle, порождающий итераторы, конструктор которого принимает один аргумент:

iterable — итерируемый объект

Итератор класса Cycle должен циклично генерировать последовательность элементов 
итерируемого объекта iterable.

Примечание 1. Гарантируется, что итерируемый объект, передаваемый в конструктор класса, 
не является множеством и итератором.

Примечание 2. Элементы итерируемого объекта, генерируемые итератором, должны располагаться 
в своем изначальном порядке.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый класс Cycle.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/669733/tests_2783878.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.4/Module_10.4.14

Sample Input 1:
cycle = Cycle('be')
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
Sample Output 1:
b
e
b
e

Sample Input 2:
cycle = Cycle([1])
print(next(cycle) + next(cycle) + next(cycle))
Sample Output 2:
3

Sample Input 3:
cycle = Cycle(range(100_000_000))
print(next(cycle))
print(next(cycle))
Sample Output 3:
0
1
'''
from _collections_abc import Iterable

class Cycle:
    def __init__(self, iterable: Iterable) -> None:
        self.iterable = iterable
        self.iter = iter(self.iterable)

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            return next(self.iter)
        except StopIteration:
            self.iter = iter(self.iterable)
            return next(self.iter)

if __name__ == '__main__':
    cycle = Cycle('be')
    print(next(cycle))
    print(next(cycle))
    print(next(cycle))
    print(next(cycle))

    cycle = Cycle([1])
    print(next(cycle) + next(cycle) + next(cycle))

    cycle = Cycle(range(100_000_000))
    print(next(cycle))
    print(next(cycle))