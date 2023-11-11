'''
Телефонные номера

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют телефонные номера формата xxx-xxx-xxxx, где x — произвольная цифра.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640164/tests_2829467.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.1/Module_11.1.24

regex = r''

Sample Input 1:
Call me tonight: 415-441-9116, xxx-xxx-xx37
Sample Output 1:
415-441-9116

Sample Input 2:
www441-515-9867www
Sample Output 2:
441-515-9867
'''
regex = r'\d{3}-\d{3}-\d{4}'