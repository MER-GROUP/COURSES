'''
Последовательность символов 3

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют последовательности символов длины 6, удовлетворяющие следующим условиям:

первый символ — произвольная цифра
второй символ — строчная латинская гласная буква (a, e, i, o, u, y)
третий символ — любой символ, кроме b, c, D, F
четвертый символ — любой не пробельный символ
пятый символ — любой символ, кроме заглавной латинской гласной буквы (A, E, I, O, U, Y)
шестой символ — любой символ, кроме точки и запятой

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/683127/tests_2833097.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.2/Module_11.2.18

regex = r''

Sample Input 1:
What password do you prefer: 9ython or 4uTUMN?
Sample Output 1:
9ython 4uTUMN

Sample Input 2:
Kate doesn’t eat_a_ any kind of meat nor wears she 1i -1) 1 at_a_
Sample Output 2:
1i -1)

Sample Input 3:
1Alark decided to stay at home #2aeb-Q): he had a terrible headache.
Sample Output 3:
2aeb-Q
'''
regex = r'\d[aeiouy][^bcDF]\S[^AEIOUY][^.,]'