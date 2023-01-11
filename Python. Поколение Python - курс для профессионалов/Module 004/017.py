'''
Последний день на Титанике
Вам доступен файл titanic.csv, который содержит данные о пассажирах, 
присутствовавших на борту парохода Титаник. В первом столбце указана единица, 
если пассажир выжил, и ноль в противном случае, во втором столбце 
записано полное имя пассажира, в третьем — пол, в четвертом — возраст:

survived;name;sex;age
0;Mr. Owen Harris Braund;male;22
1;Mrs. John Bradley (Florence Briggs Thayer) Cumings;female;38
...

Напишите программу, которая выводит имена выживших пассажиров, которым было менее 18 лет, 
каждое на отдельной строке. Причем сначала должны быть расположены имена всех пассажиров 
мужского пола, а затем — женского, имена же непосредственно в мужском и 
женском списках должны быть расположены в своем исходном порядке.

Примечание 1. Разделителем в файле titanic.csv является точка с запятой, 
при этом кавычки не используются.

Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/518491/titanic.csv
https://stepik.org/media/attachments/lesson/518491/clue_titanic.txt

Примечание 3. Часть ответа выглядит так:

Master. Gerios Moubarek
Master. Alden Gates Caldwell
...
Master. Harold Theodor Johnson
Mrs. Nicholas (Adele Achem) Nasser
Miss. Marguerite Rut Sandstrom
...

Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
'''
import csv

# with open(file='017-titanic.csv', mode='rt', encoding='utf-8', newline='') as file_opener:
with open(file='titanic.csv', mode='rt', encoding='utf-8', newline='') as file_opener:
    csv_opener = csv.reader(file_opener, delimiter=';', quoting=csv.QUOTE_NONE)
    next(csv_opener)
    arr = list(
        filter(
            # lambda x: '1' == x[0] and float(x[3]).is_integer() and 18 > int(x[3]),
            lambda x: '1' == x[0] and 18 > float(x[3]),
            csv_opener
        )
    )
# print(*arr, sep='\n') # test
arr.sort(key=lambda x: x[2], reverse=True)
[print(x[1]) for x in arr]