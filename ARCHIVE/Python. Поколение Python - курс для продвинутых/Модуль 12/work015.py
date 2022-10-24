'''
CSV-файл
Вам доступен CSV-файл data.csv, содержащий информацию в csv формате. 
Напишите функцию read_csv для чтения данных из этого файла. 
Она должна возвращать список словарей, интерпретируя 
первую строку как имена ключей, а каждую последующую 
строку как значения этих ключей.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна содержать реализованную функцию read_csv.

Примечание 1. Вызывать функцию read_csv не нужно.

Примечание 2. Функция read_csv не должна принимать аргументов. 

Примечание 2. Подробнее прочитать про CSV-файлы можно тут.
https://ru.wikipedia.org/wiki/CSV

Примечание 3. Считайте, что все ключи и значения по этим ключам 
в результирующем словаре имеют строковый тип (str).

Примечание 4. Указанный файл можно скачать по ссылке.
https://stepik.org/media/attachments/lesson/530408/data.csv

Примечание 5. Если бы файл data.csv содержал информацию

name,address,age
George,4312 Abbey Road,22
John,54 Love Ave,21

то вызов функции read_csv() вернул бы список:

[{'name': 'George', 'address': '4312 Abbey Road', 'age': '22'}, 
{'name': 'John', 'address': '54 Love Ave', 'age': '21'}]
'''
# Решение
def read_csv():
    with open('data.csv', 'rt', encoding='utf-8') as file:
        keys_arr = file.readline().rstrip('\n').split(',')
        values_arr = file.readlines()
        arr = list()
        for string in values_arr:
            my_dict = dict()
            for i, word in enumerate(string.rstrip('\n').split(',')):
                my_dict[keys_arr[i]] = word
            arr.append(my_dict)
        # print(arr)
        return arr
# read_csv()
# print(read_csv())