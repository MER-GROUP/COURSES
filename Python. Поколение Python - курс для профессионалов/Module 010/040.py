'''
Инвестиции
Вам доступен файл data.csv, который содержит информацию об инвестициях в различные стартапы. 
В первом столбце записано название компании (стартапа), во втором — инвестируемая сумма 
в долларах, в третьем — раунд инвестиции:

company,raisedAmt,round
LifeLock,6850000,b
LifeLock,6000000,a
LifeLock,25000000,c
MyCityFaces,50000,seed
Flypaper,3000000,a
...

Напишите программу с использованием конвейеров генераторов, определяющую общую сумму, 
которая была инвестирована в раунде а, и выводящую полученный результат.

Примечание 1. Разделителем в файле data.csv является запятая, при этом кавычки не используются.

Примечание 2. Указанный файл доступен по ссылке.
https://stepik.org/media/attachments/lesson/673155/data.csv

Примечание 3. Пример вывода:
86900000000

Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
'''
from _collections_abc import Generator
import csv

if __name__ == '__main__':
    with open(file='data.csv', mode='rt', encoding='utf-8', newline='') as file_open:
    # with open(file='040-data.csv', mode='rt', encoding='utf-8', newline='') as file_open:
        csv_file = csv.DictReader(f=file_open, delimiter=',', quotechar=None, quoting=csv.QUOTE_NONE)
        # print(csv_file.fieldnames)
        
        round_a = (
            i.get(csv_file.fieldnames[-2])
            for i in csv_file 
            if 'a' == i.get(csv_file.fieldnames[-1])
        )
        round_int = map(int, round_a)
        result = sum(round_int)
        print(result)