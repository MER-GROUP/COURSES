'''
Американские почтовые индексы

Дополните приведенный ниже код, чтобы переменная regex содержала 
регулярное выражение, которому соответствуют Американские почтовые индексы, 
удовлетворяющие следующим условиям:

почтовый индекс начинается с пяти цифр
далее следует необязательная часть из четырех цифр, которая отделяется 
от пяти первых цифр дефисом
Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/684549/tests_3182183.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.5/Module_11.5.5

regex = r''

Sample Input 1:
My old poscode: 18491
And new: 48034-1234
Sample Output 1:
18491 48034-1234

Sample Input 2:
New postcode: 09090-8989, old postcode 0909-8989
Sample Output 2:
09090-8989

Sample Input 3:
New postcode: ABCDE-8989, old postcode 0909-, 01928-0909
Sample Output 3:
01928-0909
'''
regex = r'(\d{5})' +\
        r'(-\d{4})?'