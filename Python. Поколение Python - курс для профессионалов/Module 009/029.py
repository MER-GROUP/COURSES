'''
Функция date_formatter()
Нередко в разных странах используются разные форматы дат. 
Рассмотрим часть из них:

код страны    формат даты
ru            DD.MM.YYYY
us            MM-DD-YYYY
ca            YYYY-MM-DD
br            DD/MM/YYYY
fr            DD.MM.YYYY
pt            DD-MM-YYYY

Реализуйте функцию date_formatter(), которая принимает один аргумент:

country_code — код страны

Функция date_formatter() должна возвращать функцию, которая принимает 
в качестве аргумента дату (тип date) и возвращает строку с данной датой 
в формате страны с кодом country_code.

Примечание 1. Гарантируется, что в функцию date_formatter() передаются 
только те коды стран, что перечислены в приведенной выше таблице.

Примечание 2. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию date_formatter(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/651459/tests_3131753.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.5/Module_9.5.19

Sample Input 1:
date_ru = date_formatter('ru')
today = date(2022, 1, 25)
print(date_ru(today))
Sample Output 1:
25.01.2022

Sample Input 2:
date_ru = date_formatter('us')
today = date(2025, 1, 5)
print(date_ru(today))
Sample Output 2:
01-05-2025

Sample Input 3:
date_ru = date_formatter('ca')
today = date(2015, 12, 7)
print(date_ru(today))
Sample Output 3:
2015-12-07
'''
pass

if __name__ == '__main__':
    pass