'''
Функция is_prime()
Реализуйте функцию is_prime() с использованием генераторных выражений, которая 
принимает один аргумент:

number — натуральное число
Функция должна возвращать True, если число number является простым, или False 
в противном случае.

Примечание 1. Простое число — натуральное число, имеющее ровно два различных 
натуральных делителя — единицу и самого себя.

Примечание 2. В задаче удобно воспользоваться функциями all() или any(). 

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию is_prime(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640049/tests_2779987.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.6/Module_10.6.16

Sample Input 1:
print(is_prime(7))
Sample Output 1:
True

Sample Input 2:
print(is_prime(8))
Sample Output 2:
False

Sample Input 3:
print(is_prime(1))
Sample Output 3:
False
'''
from __future__ import annotations
from _collections_abc import Generator

def is_prime(number: int) -> Generator:
    return (all(number % i for i in range(2, int(number**0.5)+1)), False)[2 > number]
            
if __name__ == '__main__':
    print(is_prime(7)) # 1
 
    print(is_prime(8)) # 2

    print(is_prime(1)) # 3

    print(is_prime(16)) # 4