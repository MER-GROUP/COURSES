'''
Загадка от Жака Фреско 🌶️

Однажды Жака Фреско спросили:
"Если ты такой умный, почему не богатый?"

Жак не стал отвечать на столь провокационный вопрос, 
вместо этого он задал загадку спрашивающему:
"Были разноцветные козлы. Сколько?"
"Сколько чего?"
"Сколько из них составляет более 7% от общего количества козлов?"

Вам доступен текстовый файл goats.txt в первой строке которого 
написано слово COLOURS, далее идет список всех возможных цветов козлов. 
Затем идет строка со словом GOATS, и далее непосредственно перечисление 
козлов разных цветов. Перечень козлов включает только строки из первого списка.

Напишите программу создания файла answer.txt и вывода в него списка козлов, 
которые удовлетворяют условию загадки от Жака Фреско.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем answer.txt и вывести в него 
в алфавитном порядке названия цветов козлов, которые удовлетворяют условию загадки Жака Фреско.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

Примечание 2. Если бы файл goats.txt содержал строки:
COLOURS
Pink goat
Green goat
Black goat
GOATS
Pink goat
Pink goat
Black goat
Pink goat
Pink goat
Black goat
Green goat
Pink goat
Black goat
Black goat
Pink goat
Pink goat
Black goat
Black goat
Pink goat

то файл answer.txt имел бы вид:
Black goat
Pink goat

Примечание 3. Указанный файл можно скачать по ссылке. 
https://stepik.org/media/attachments/lesson/519126/goats.txt
'''
# Решение
# from collections import Counter
# with open('goats.txt', 'rt', encoding='utf-8') as file_in,\
#     open('answer.txt', 'wt', encoding='utf-8') as file_out:
#     counter = Counter()
#     goat = False
#     for line in file_in:
#         if 'GOATS' == line.strip():
#             goat = True
#             continue
#         if goat:
#             counter.update([line.split()[0]])
#     # print(counter.most_common())
#     # print(counter.total())
#     for k, v in sorted(counter.items()):
#         if(counter.total() * 7 / 100 < v):
#             print(f'{k} goat', file=file_out)

with open('goats.txt', 'rt', encoding='utf-8') as file_in,\
    open('answer.txt', 'wt', encoding='utf-8') as file_out:
    counter = dict()
    sum = int()
    goat = False
    for line in file_in:
        if 'GOATS' == line.strip():
            goat = True
            continue
        if goat:
            counter[line.split()[0]] = counter.get(line.split()[0], 0) + 1
            sum += 1
    for k, v in sorted(counter.items()):
        if(sum * 7 / 100 < v):
            print(f'{k} goat', file=file_out)