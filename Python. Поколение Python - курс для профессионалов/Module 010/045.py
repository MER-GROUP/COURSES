'''
Функция stop_on()
Реализуйте генераторную функцию, которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
obj — произвольный объект

Функция должна возвращать генератор, порождающий последовательность элементов 
итерируемого объекта iterable до тех пор, пока не будет достигнут элемент, 
равный obj. Если итерируемый объект iterable не содержит ни одного элемента, 
равного obj, генератор должен породить все элементы iterable.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе 
должны располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, 
не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию stop_on(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/673155/tests_3149808.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.7/Module_10.7.20

Sample Input 1:
numbers = [1, 2, 3, 4, 5]
print(*stop_on(numbers, 4))
Sample Output 1:
1 2 3

Sample Input 2:
iterator = iter('beegeek')
print(*stop_on(iterator, 'a'))
Sample Output 2:
b e e g e e k
'''
from _collections_abc import Generator, Iterable

def stop_on(iterable: Iterable, obj: object) -> Generator:
    for i in iterable:
        if i == obj:
            break
        yield i

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    print(*stop_on(numbers, 4))

    iterator = iter('beegeek')
    print(*stop_on(iterator, 'a'))