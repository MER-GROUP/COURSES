'''
Итератор Square
Реализуйте класс Square, порождающий итераторы, конструктор которого принимает один аргумент:

n — натуральное число,

Итератор класса Square должен генерировать последовательность из n чисел, каждое 
из которых является квадратом очередного натурального числа, а затем возбуждать исключение StopIteration.

Примечание 1. Последовательность квадратов натуральных чисел начинается с квадрата числа 1.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс Square.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/669733/tests_2771339.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.4/Module_10.4.9

Sample Input 1:
squares = Square(2)
print(next(squares))
print(next(squares))
Sample Output 1:
1
4

Sample Input 2:
squares = Square(10)
print(list(squares))
Sample Output 2:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Sample Input 3:
squares = Square(1)
print(list(squares))
Sample Output 3:
[1]
'''
class Square:
    def __init__(self, n: int) -> None:
        self.n = n
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        self.count += 1
        if self.count > self.n:
            raise StopIteration
        return self.count**2

if __name__ == '__main__':
    squares = Square(2)
    print(next(squares))
    print(next(squares))

    squares = Square(10)
    print(list(squares))

    squares = Square(1)
    print(list(squares))