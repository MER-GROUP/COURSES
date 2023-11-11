'''
Я и сам своего рода переводчик
Дана строка соответствия латинскому алфавиту: первый символ строки 
соответствует букве a, второй — b, третий — c, и так далее. 
Каждый символ соответствует как заглавной, так и строчной буквам. 
Количество символов в строке совпадает с количеством букв в латинском алфавите.

Напишите программу, которая с помощью данной строки переводит заданный текст.

Формат входных данных
На вход программе в первой строке подается строка соответствия латинскому алфавиту, 
в следующей — текст, требующий перевода.

Формат выходных данных
Программа должна с помощью данной строки соответствия латинскому алфавиту 
перевести введенный текст и вывести полученный результат.

Примечание 1. Программа должна игнорировать все символы, не являющиеся латинскими буквами.

Примечание 2. Составить словарь соответствия можно с помощью строкового метода maketrans(), 
подробнее о котором рассказывается по ссылке.
https://docs-python.ru/tutorial/operatsii-tekstovymi-strokami-str-python/metod-str-maketrans/

Примечание 3. Тестовые данные доступны по ссылкам:
Архив с тестами
https://stepik.org/media/attachments/lesson/631917/tests_3079498.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_6/Module_6.2/Module_6.2.17

Sample Input 1:
🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩
I love Python =)
Sample Output 1:
🅘 🅛🅞🅥🅔 🅟🅨🅣🅗🅞🅝 =)

Sample Input 2:
😀😄😁😆😉😌😍🥰😘😗😙😚😋😛😝😜🤪🤨😫😩🥺😢😭😤😠😡
Dont be so sad!
Sample Output 2:
😆😝😛😩 😄😉 😫😝 😫😀😆!
'''
from string import ascii_letters, ascii_lowercase

abc_decode = input()
text = input()

tbl = str.maketrans(
    ascii_lowercase,
    ''.join([c for c in abc_decode if c not in ascii_letters])
)

# print('--------------')
# print(''.join([c for c in abc_decode if c not in ascii_letters]))
# print(ascii_lowercase)
# print(tbl)
# print(type(tbl))
# print('--------------')

print(text.lower().translate(tbl))