'''
Схожие буквы
В русском и английском языках есть буквы, которые выглядят одинаково. 
Вот список английских букв "AaBCcEeHKMOoPpTXxy", 
а вот их русские аналоги "АаВСсЕеНКМОоРрТХху". Напишите программу, 
которая для трёх букв из данных списков букв определяет, 
русские они, английские или и те и другие (смесь русских и английских букв).

Формат входных данных
На вход программе подаются три буквы из указанных в условии наборов букв, 
каждая на отдельной строке.

Формат выходных данных
Программа должна вывести

ru, если все три буквы русские
en, если все три буквы английские
mix, если среди букв есть как русские, так и английские

Примечание 1. Гарантируется, что введенные три буквы находятся 
в наборе "AaBCcEeHKMOoPpTXxy" + "АаВСсЕеНКМОоРрТХху" (английские + русские буквы).

Примечание 2. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/569749/tests_2310070.zip

Sample Input 1:
Р
О
А
Sample Output 1:
ru

Sample Input 2:
o
K
M
Sample Output 2:
en

Sample Input 3:
T
а
B
Sample Output 3:
mix
'''
def letters(*args):
    eng_set ={ord(c) for c in 'AaBCcEeHKMOoPpTXxy'}
    rus_set ={ord(c) for c in 'АаВСсЕеНКМОоРрТХху'}
    if set(args).intersection(eng_set) and set(args).intersection(rus_set):
        return 'mix'
    elif set(args).intersection(eng_set):
        return 'en'
    else:
        return 'ru'

print(
    letters(
        *map(lambda x: ord(x) ,[input() for _ in range(3)])
    )
)