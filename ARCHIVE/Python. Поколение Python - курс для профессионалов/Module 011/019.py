'''
Слова

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное 
выражение, которому соответствуют слова a, A, an и An.

Примечание 1. Словом будем считать последовательность символов, 
соответствующих \w, окруженную символами, соответствующими \W

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/690796/tests_2862306.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.4/Module_11.4.10

regex = r''

Sample Input 1:
A cow is an animal.
Sample Output 1:
A an

Sample Input 2:
I have been reading this text for aN hour. Сan you give me this book? AN or an apple
Sample Output 2:
an

Sample Input 3:
An acle, a Ancle, A antarktida, an Any
Sample Output 3:
An a A an
'''
regex = r'\b[aA]\b|' + \
        r'\ban\b|' + \
        r'\bAn\b'