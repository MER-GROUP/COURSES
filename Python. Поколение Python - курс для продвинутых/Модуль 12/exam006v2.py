'''
Forbidden words 🌶️
На вход программе подается строка текста с именем текстового файла. 
апишите программу, выводящую на экран содержимое этого файла, 
но с заменой всех запрещенных слов звездочками * 
(количество звездочек равно количеству букв в слове).

Запрещенные слова, разделенные символом пробела, 
хранятся в текстовом файле forbidden_words.txt. 
Гарантируется, что все слова в этом файле записаны в нижнем регистре.

Формат входных данных
На вход программе подается строка текста с именем существующего текстового файла, 
в котором необходимо заменить запрещенные слова звездочками.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание 1. Ваша программа должна заменить запрещенные слова, 
где бы они ни встречались, даже если они встречаются в середине другого слова.

Примечание 2. Программа должна заменять запрещенные слова 
независимо от их регистра. Например, если файл forbidden_words.txt 
содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM 
и подобные должны быть заменены на ****.

Примечание 3. Если бы файл forbidden_words.txt содержал слова:

hello email python the exam wor is

а файл в котором заменяются слова имел бы вид:

Hello, world! Python IS the programming language of thE future. My EMAIL is....
PYTHON is awesome!!!!

то результатом будет:

*****, ***ld! ****** ** *** programming language of *** future. My ***** **....
****** ** awesome!!!!

Примечание 4. Файл forbidden_words.txt можно скачать по ссылке. 
Ваша программа прогоняется на трех файлах data.txt, stepik.txt и beegeek.txt.
https://stepik.org/media/attachments/lesson/448983/forbidden_words.txt
https://stepik.org/media/attachments/lesson/448983/data.txt
https://stepik.org/media/attachments/lesson/448983/stepik.txt
https://stepik.org/media/attachments/lesson/448983/beegeek.txt
'''
# Решение
with open('forbidden_words.txt') as f:
    forbidden_words = {word: '*' * len(word) for word in f.read().split()}
with open(input()) as f:
# with open('test_beegeek.txt') as f:
    s = f.read()
    s_lower = s.lower()
for forbidden_word in forbidden_words:
    s_lower = s_lower.replace(forbidden_word, forbidden_words[forbidden_word])
print(*map((lambda c1, c2: '*' if c2 == '*' else c1), s, s_lower), sep='')