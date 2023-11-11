'''
Итератор Fibonacci
Реализуйте класс Fibonacci, порождающий итераторы, конструктор которого 
не принимает никаких аргументов.

Итератор класса Fibonacci должен генерировать бесконечную последовательность 
чисел Фибоначчи, начиная с 1.

Примечание 1. Последовательность Фибоначчи – последовательность натуральных 
чисел, где каждое последующее число является суммой двух предыдущих:

1, 1, 2, 3, 5, 8, 13, 21, 34

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс Fibonacci.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/669733/tests_2771266.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.4/Module_10.4.10

Sample Input 1:
fibonacci = Fibonacci()
print(next(fibonacci))
Sample Output 1:
1

Sample Input 2:
fibonacci = Fibonacci()
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
Sample Output 2:
1
1
2
3
'''
class Fibonacci:
    def __init__(self) -> None:
        self.a = 1
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        fobo = self.a
        self.b, self.a = self.a + self.b, self.b
        return fobo

if __name__ == '__main__':
    fibonacci = Fibonacci()
    print(next(fibonacci))

    fibonacci = Fibonacci()
    print(next(fibonacci))
    print(next(fibonacci))
    print(next(fibonacci))
    print(next(fibonacci))