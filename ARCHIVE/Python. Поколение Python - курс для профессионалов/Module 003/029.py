'''
Функция num_of_sundays()
Реализуйте функцию num_of_sundays(), 
которая принимает на вход один аргумент:

year — натуральное число, год
Функция должна возвращать количество воскресений в году year.

Примечание 1. В тестирующую систему сдайте программу, 
содержащую только необходимую функцию num_of_sundays(), 
но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/570050/tests_2506803.zip

Sample Input 1:
print(num_of_sundays(2021))
Sample Output 1:
52

Sample Input 2:
year = 2000
print(num_of_sundays(year))
Sample Output 2:
53

Sample Input 3:
print(num_of_sundays(768))
Sample Output 3:
52
'''
from datetime import date, datetime, timedelta

def num_of_sundays(year: int) -> int:
    start = date(year=year, month=1, day=1).toordinal()
    end = date(year=year + 1, month=1, day=1).toordinal()
    count = 0
    for i in range(start, end):
        if 7 == date.fromordinal(i).isoweekday():
            count += 1
    return count

if __name__ == '__main__':
    print(num_of_sundays(2021))

    year = 2000
    print(num_of_sundays(year))

    print(num_of_sundays(768))