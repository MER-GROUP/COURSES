'''
Итератор BoundedRepeater
Реализуйте класс BoundedRepeater, порождающий итераторы, конструктор которого принимает 
два аргумента в следующем порядке:

obj — произвольный объект
times — натуральное число

Итератор класса BoundedRepeater должен генерировать значение obj times раз, а затем возбуждать 
исключение StopIteration.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимый 
класс BoundedRepeater.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/669733/tests_2771336.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.4/Module_10.4.8

class BoundedRepeater:
    def __init__(self, ____, ____):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        pass
   
Sample Input 1:
bee = BoundedRepeater('bee', 2)
print(next(bee))
print(next(bee))
Sample Output 1:
bee
bee

Sample Input 2:
geek = BoundedRepeater('geek', 3)
print(next(geek))
print(next(geek))
print(next(geek))
try:
    print(next(geek))
except StopIteration:
    print('Error')
Sample Output 2:
geek
geek
geek
Error
'''
class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.times:
            raise StopIteration
        self.count += 1
        return self.obj

if __name__ == '__main__':
    bee = BoundedRepeater('bee', 2)
    print(next(bee))
    print(next(bee))

    geek = BoundedRepeater('geek', 3)
    print(next(geek))
    print(next(geek))
    print(next(geek))
    try:
        print(next(geek))
    except StopIteration:
        print('Error')