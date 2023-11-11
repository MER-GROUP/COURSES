'''
Функция primes()
Реализуйте генераторную функцию primes(), которая принимает два аргумента в следующем порядке:

left — натуральное число
right — натуральное число

Функция должна возвращать генератор, порождающий последовательность простых чисел 
от left до right включительно, а затем возбуждающий исключение StopIteration.

Примечание 1. Гарантируется, что left <= right.

Примечание 2. Простое число — натуральное число, имеющее ровно два различных натуральных 
делителя — единицу и самого себя. Единица простым числом не является. 

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую 
генераторную функцию primes(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640048/tests_2775846.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.5/Module_10.5.17

Sample Input 1:
generator = primes(1, 15)
print(*generator)
Sample Output 1:
2 3 5 7 11 13

Sample Input 2:
generator = primes(6, 36)
print(next(generator))
print(next(generator))
Sample Output 2:
7
11
'''
from __future__ import annotations
from _collections_abc import Generator

def primes(left: int, right: int) -> Generator:
    def is_prime(num):
        count = 0
        for i in range(1, num + 1):
            if not num % i:
                count += 1
            if 2 < count: 
                break
        return (False, True)[2 == count]
    
    while left <= right:
        if is_prime(left):
            yield left
        left += 1

    return

if __name__ == '__main__':
    generator = primes(1, 15)
    print(*generator)

    generator = primes(6, 36)
    print(next(generator))
    print(next(generator))