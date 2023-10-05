'''
Последовательности из 8 цифр

Дополните приведенный ниже код, чтобы переменная regex содержала 
регулярное выражение, которому соответствуют последовательности из 8 цифр, 
удовлетворяющие следующим условиям:

последовательность может содержать символы -, --- или . в качестве разделителей, 
только если они делят ее на группы по 2 цифры
последовательность должна содержать только один тип разделителя, если он присутствует

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/684549/tests_3182182.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.5/Module_11.5.17

regex = r''

Sample Input 1:
I have some groups of digits. Do you want to see? 11-22-33-44
Sample Output 1:
11-22-33-44

Sample Input 2:
Look at this: 12345678
Sample Output 2:
12345678

Sample Input 3:
1-2-3-4-5-6-7-89-w9--99
Sample Output 3:
'''
regex = r''