'''
Функция fill_up_missing_dates()

Реализуйте функцию fill_up_missing_dates(), 
которая принимает на вход один аргумент:

dates — список строковых дат в формате DD.MM.YYYY

Функция должна возвращать список, 
в котором содержатся все даты из списка dates, 
расположенные в порядке возрастания, 
а также все недостающие промежуточные даты.

Примечание 1. Рассмотрим первый тест. 
Список dates содержит период с 01.11.2021 по 07.11.2021:

dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
в котором отсутствуют даты 02.11.2021, 05.11.2021, 06.11.2021. 
Тогда вызов функции:

fill_up_missing_dates(dates)

должен вернуть список: 

['01.11.2021', '02.11.2021', '03.11.2021', '04.11.2021', '05.11.2021', '06.11.2021', '07.11.2021']

Примечание 2. Функция должна создавать и возвращать новый список, а не изменять переданный.

Примечание 3. В тестирующую систему сдайте программу, 
содержащую только необходимую функцию fill_up_missing_dates(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/570050/tests_2505131.zip

Sample Input 1:
dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
print(fill_up_missing_dates(dates))
Sample Output 1:
['01.11.2021', '02.11.2021', '03.11.2021', '04.11.2021', '05.11.2021', '06.11.2021', '07.11.2021']

Sample Input 2:
dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']
print(fill_up_missing_dates(dates))
Sample Output 2:
['01.11.2021', '02.11.2021', '03.11.2021', '04.11.2021', '05.11.2021', '06.11.2021', '07.11.2021', '08.11.2021', '09.11.2021', '10.11.2021', '11.11.2021', '12.11.2021', '13.11.2021', '14.11.2021', '15.11.2021']
'''
pass