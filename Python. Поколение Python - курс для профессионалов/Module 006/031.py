'''
Бесплатные курсы берут свое 😢
Для дополнительного заработка Тимур решил заняться продажей овощей. 
У него имеются данные о продажах за год, разделенные на четыре файла 
по кварталам: quarter1.csv, quarter2.csv, quarter3.csv и quarter4.csv. 
В каждом файле в первом столбце указывается название продукта, 
а в последующих — количество проданного продукта в килограммах за определенный месяц:

продукт,январь,февраль,март
Картофель,39,61,3
Дайкон,51,96,83
...

Также присутствует файл prices.json, содержащий словарь, 
в котором ключом является название продукта, а значением — цена за килограмм в рублях:

{
   "Картофель": 53,
   "Дайкон": 55,
...
}

Напишите программу, которая выводит единственное число — сумму, 
заработанную Тимуром за год на продаже овощей.

Примечание 1. Ссылки на указанные файлы: quarter1.csv, quarter2.csv, 
quarter3.csv, quarter4.csv, prices.json. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/635441/quarter1.csv
https://stepik.org/media/attachments/lesson/635441/quarter2.csv
https://stepik.org/media/attachments/lesson/635441/quarter3.csv
https://stepik.org/media/attachments/lesson/635441/quarter4.csv
https://stepik.org/media/attachments/lesson/635441/prices.json
https://stepik.org/media/attachments/lesson/635441/clue_free.txt

Примечание 2. При открытии файла используйте явное указание кодировки UTF-8.
'''
from collections import Counter

pass