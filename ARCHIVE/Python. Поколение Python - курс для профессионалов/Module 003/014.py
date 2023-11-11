'''
Функция print_good_dates()
Тимур считает дату «интересной», если её год совпадает с годом его рождения, 
а сумма номера месяца и номера дня равна его возрасту. 
Год рождения Тимура — 1992, возраст — 29 лет.

Реализуйте функцию print_good_dates(), которая принимает один аргумент:

dates — список дат (тип date)

Функция должна выводить «интересные» даты в порядке возрастания, 
каждую на отдельной строке, в формате  month_name DD, YYYY, 
где month_name — полное название месяца на английском. 

Примечание 1. Если в функцию передается пустой список или 
список без интересных дат, функция ничего не должна выводить.

Примечание 2. В тестирующую систему сдайте программу, 
содержащую только необходимую функцию print_good_dates(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/570048/tests_2503974.zip

Sample Input 1:
dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)
Sample Output 1:
September 20, 1992
October 19, 1992

Sample Input 2:
dates = [date(1993, 9, 15), date(2021, 11, 2), date(2000, 7, 7)]
print_good_dates(dates)
Sample Output 2:
'''
from datetime import date

def print_good_dates(dates):
    print(
        *map(
            lambda x: x.strftime('%B %d, %Y'),
            filter(
                lambda x: 1992 == x.year\
                        and 29 == sum((x.month, x.day)),
                sorted(dates)
            )
        ),
        sep='\n'
    )

if __name__ == '__main__':
    dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
    print_good_dates(dates)

    dates = [date(1993, 9, 15), date(2021, 11, 2), date(2000, 7, 7)]
    print_good_dates(dates)