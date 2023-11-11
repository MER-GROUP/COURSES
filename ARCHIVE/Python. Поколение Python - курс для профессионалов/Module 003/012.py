'''
Две даты
Напишите программу, которая принимает на вход две даты и выводит ту, что меньше.

Формат входных данных
На вход программе подаются две корректные даты в ISO формате (YYYY-MM-DD), 
каждая на отдельной строке.

Формат выходных данных
Программа должна выбрать из двух введенных дат меньшую и вывести ее в формате DD-MM (YYYY).

Примечание. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/570048/tests_2491371.zip

Sample Input 1:
2021-05-12
2021-05-04
Sample Output 1:
04-05 (2021)

Sample Input 2:
1999-07-14
1999-07-14
Sample Output 2:
14-07 (1999)
'''
from datetime import date

print(
    min([
        date.fromisoformat(input()),
        date.fromisoformat(input())
    ]).strftime('%d-%m (%Y)')
)