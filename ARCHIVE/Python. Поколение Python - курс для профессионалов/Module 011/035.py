'''
Последовательности из 8 цифр

Дополните приведенный ниже код, чтобы переменная regex содержала 
регулярное выражение, которому соответствуют последовательности из 8 цифр. 
Причем последовательность может содержать символы дефиса - в качестве разделителей, 
только если они делят ее на группы по 2 цифры.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/684549/tests_3182181.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.5/Module_11.5.16

regex = r''

Sample Input 1:
Digits from 0 to 7: 01234567
Sample Output 1:
01234567

Sample Input 2:
Digits from 1 to 8 by groups: 12-34-56-78
Sample Output 2:
12-34-56-78

Sample Input 3:
Digits from 1 to 8 by groups: 1234-5678
Sample Output 3:
'''
regex = r'\d{8}|(\d{2}-){3}\d{2}'