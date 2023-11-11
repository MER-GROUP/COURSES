'''
Слова 3

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют слова, начинающиеся с латинской заглавной буквы.

Примечание 1. Словом будем считать последовательность символов, соответствующих \w, 
окруженную символами, соответствующими \W

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/690796/tests_3166018.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.4/Module_11.4.12

regex = r''

Sample Input 1:
I signed up in the app using my Apple ID. How can I sign in to the web version?
Sample Output 1:
I Apple ID How I

Sample Input 2:
I can Do it MYSELF
Sample Output 2:
I Do MYSELF

Sample Input 3:
How are --U--
Sample Output 3:
How U
'''
regex = r'\b[A-Z][\wА-Яа-я]*\b'