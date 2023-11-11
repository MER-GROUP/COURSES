'''
Регулярное выражение

Вам доступно регулярное выражение regex, которому соответствуют строки car, cat и cab. 
Перепишите его с использованием набора символов, чтобы ему соответствовали те же строки.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/683127/tests_3162617.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.2/Module_11.2.14

regex = r'car|cat|cab'

Sample Input 1:
car cat cab
Sample Output 1:
car cat cab

Sample Input 2:
Car cAt caB caaaaaat carrrrrr-kar
Sample Output 2:
car

Sample Input 3:
Cart carcat caBriolet Cabriolet cabriolet
Sample Output 3:
car cat cab
'''
# regex = r'car|cat|cab'
regex = r'ca[rtb]'
