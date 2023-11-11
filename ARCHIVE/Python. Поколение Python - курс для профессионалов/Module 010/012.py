'''
Итератор Repeater
Реализуйте класс Repeater, порождающий итераторы, конструктор которого принимает один аргумент:

obj — произвольный объект

Итератор класса Repeater должен бесконечно генерировать единственное значение — obj.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимый класс Repeater.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/669733/tests_2771340.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.4/Module_10.4.7

class Repeater:
    def __init__(self, ____):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        pass

Sample Input 1:
bee = Repeater('bee')
print(next(bee))
Sample Output 1:
bee

Sample Input 2:
geek = Repeater('geek')
print(next(geek))
print(next(geek))
print(next(geek))
Sample Output 2:
geek
geek
geek
'''
class Repeater:
    def __init__(self, _object: object) -> None:
        self._object = _object
    
    def __iter__(self) -> object:
        return self
    
    def __next__(self) -> object:
        return self._object

if __name__ == '__main__':
    bee = Repeater('bee')
    print(next(bee))

    geek = Repeater('geek')
    print(next(geek))
    print(next(geek))
    print(next(geek))