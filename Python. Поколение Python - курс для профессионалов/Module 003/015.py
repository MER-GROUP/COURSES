'''
Функция is_correct()
Реализуйте функцию is_correct(), которая принимает 
три аргумента в следующем порядке:

day — натуральное число, день
month — натуральное число, месяц
year — натуральное число, год

Функция должна возвращать True, если дата с компонентами day, 
month и year является корректной, или False в противном случае.

Примечание 1. Вспомните про конструкцию try-except. 

Примечание 2. В тестирующую систему сдайте программу, 
содержащую только необходимую функцию is_correct(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/570048/tests_2321748.zip

Sample Input 1:
print(is_correct(31, 12, 2021))
Sample Output 1:
True

Sample Input 2:
print(is_correct(31, 13, 2021))
Sample Output 2:
False
'''
from datetime import date

def is_correct(day: int, month: int, year: int) -> False:
    try:
        date(year, month, day)
        return True
    except:
        return False

if __name__ == '__main__':
    print(is_correct(31, 12, 2021))
    print(is_correct('31', '12', '2021'))
    print(is_correct(31, 13, 2021))