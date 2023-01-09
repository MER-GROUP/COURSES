'''
Функция csv_columns()
Реализуйте функцию csv_columns(), которая принимает один аргумент:

filename — название csv файла, например, data.csv
Функция должна возвращать словарь, в котором ключом является название 
столбца файла filename, а значением — список элементов этого столбца.

Примечание 1. Гарантируется, что в передаваемом в функцию файле 
разделителем является запятая, при этом кавычки не используются.

Примечание 2. Гарантируется, что у передаваемого в функцию 
файла первая строка содержит названия столбцов.

Примечание 3. Например, если бы файл exam.csv имел вид:

name,grade
Timur,5
Arthur,4
Anri,5

то следующий вызов функции csv_columns():

csv_columns('exam.csv')

должен был бы вернуть:

{'name': ['Timur', 'Arthur', 'Anri'], 'grade': ['5', '4', '5']}

Примечание 4. Ключи в словаре, а также элементы в списках должны располагаться 
в своем исходном порядке.

Примечание 5. В тестирующую систему сдайте программу, 
содержащую только необходимую функцию csv_columns(), но не код, вызывающий ее.

Примечание 6. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/518491/tests_3072469.zip
'''
import csv

def csv_columns(file_name: str) -> dict():
    with open(file_name, 'rt', newline='', encoding='utf-8') as file_opener:
        csv_opener = csv.DictReader(file_opener)
        colums = dict()
        for line in csv_opener:
            for key in csv_opener.fieldnames:
                colums[key] = colums.get(key, []) + [line[key]]
        return colums

if __name__ == '__main__':
    print(csv_columns('014-exam.csv'))