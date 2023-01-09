'''
Средняя зарплата
Вам доступен файл salary_data.csv, который содержит анонимную информацию 
о зарплатах сотрудников в различных компаниях. В первом столбце записано 
название компании, а во втором — зарплата очередного сотрудника:

company_name;salary
Atos;135000
ХайТэк;24400
Philax;128600
Инлайн Груп;43900
IBS;70600
Oracle;131600
Atos;91000
...

Напишите программу, которая упорядочивает компании по возрастанию 
средней зарплаты ее сотрудников и выводит их названия, каждое на отдельной строке. 
Если две компании имеют одинаковые средние зарплаты, они должны быть расположены 
в лексикографическом порядке их названий.

Примечание 1. Средняя зарплата компании определяется как отношение 
суммы всех зарплат к их количеству.

Примечание 2. Разделителем в файле salary_data.csv является точка с запятой, 
при этом кавычки не используются.

Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/518491/salary_data.csv
https://stepik.org/media/attachments/lesson/518491/clue_average_salary.txt

Примечание 4. Начальная часть ответа выглядит так:

Информзащита
Форс
OFT group
...

Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.
'''
import csv

# with open('013-salary_data.csv', 'rt', encoding='utf-8', newline='') as file_opener:
with open('salary_data.csv', 'rt', encoding='utf-8', newline='') as file_opener:
    csv_opener = csv.DictReader(file_opener, delimiter=';', quoting=csv.QUOTE_NONE)
    salary_sum = dict()
    salary_count = dict()

    for line in csv_opener:
        salary_sum[line[list(line.keys())[0]]] = salary_sum.get(line[list(line.keys())[0]], 0) \
                                            + int(line[list(line.keys())[1]])
        salary_count[line[list(line.keys())[0]]] = salary_count.get(line[list(line.keys())[0]], 0) + 1
    # print(salary_sum) # test
    # print(salary_count) # test

    average = list(
            map(
            lambda x, y: {x[0]: int(x[1])/int(y[1])},
            salary_sum.items(), 
            salary_count.items()
        )
    )
    # print(average) # test
    # print(type(average)) # test

    answer = sorted(
        average, 
        key=lambda x: ((x[list(x.keys())[0]]), list(x.keys())[0])
    )

    for i in answer:
        print(list(i.keys())[0])