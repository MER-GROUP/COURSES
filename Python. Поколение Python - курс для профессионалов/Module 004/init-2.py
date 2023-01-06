print('------------------')

with open('products.csv', encoding='utf-8') as file:
    data = file.read()
    for line in data.splitlines():
        print(line.split(','))

print('------------------')

with open('products.csv', encoding='utf-8') as file:
    data = file.read()
    table = [r.split(',') for r in data.splitlines()]
    # удаляем заголовок
    del table[0]                                        
    table.sort(key=lambda item: int(item[1]))
    for line in table[:5]:
        print(line)

print('------------------')

with open('products.tsv', encoding='utf-8') as file:
    data = file.read()
    table = [r.split('\t') for r in data.splitlines()]
    del table[0]
    table.sort(key=lambda item: int(item[1]))
    for line in table[:5]:
        print(line)

print('------------------')

import csv

with open('products.csv', encoding='utf-8') as file:
    # создаем reader объект
    rows = csv.reader(file)                               
    for row in rows:
        print(row)

print('------------------')

import csv

with open('products.csv', encoding='utf-8') as file:
    rows = csv.reader(file)
    for keywords, price, product_name in rows:
        print(f'Ключевые слова: {keywords}, цена: {price}, название: {product_name}')

print('------------------')

import csv

with open('products.dsv', encoding='utf-8') as file:
    rows = csv.reader(file, delimiter=';', quotechar='"')
    for index, row in enumerate(rows):
        if index > 5:
            break
        print(row)

print('------------------')

import csv

with open('products.dsv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';', quotechar='"')
    print(type(rows))
    for row in rows:
        print(row)
        print(type(row))

print('------------------')

import csv

with open('products.dsv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';', quotechar='"')
    expensive = sorted(rows, key=lambda item: int(item['price']), reverse=True)
    for record in expensive[:5]:
        print(record)

print('------------------')

import csv

columns = ['first_name', 'second_name', 'class_number', 'class_letter']
data = [['Тимур', 'Гуев', 11, 'А'], ['Руслан', 'Чаниев', 9, 'Б'], ['Артур', 'Харисов', 10, 'В']]

with open('students.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    for row in data:
        writer.writerow(row)

print('------------------')

import csv

columns = ['first_name', 'second_name', 'class_number', 'class_letter']
data = [['Тимур', 'Гуев', 11, 'А'], ['Руслан', 'Чаниев', 9, 'Б'], ['Роман', 'Белых', 10, 'В']]

with open('students.dsv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(columns)
    for row in data:
        writer.writerow(row)

print('------------------')

import csv

columns = ['first_name', 'second_name', 'class_number', 'class_letter']
data = [['Тимур', 'Гуев', 11, 'А'], ['Руслан', 'Чаниев', 9, 'Б'], ['Роман', 'Белых', 10, 'В']]

with open('students2.dsv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(columns)
    writer.writerows(data)

print('------------------')

import csv

columns = ['first_name', 'second_name', 'class_number', 'class_letter']
data = [['Тимур', 'Гуев', 11, 'А'], ['Руслан', 'Чаниев', 9, 'Б'], ['Роман', 'Белых', 10, 'В']]

with open('students2.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(columns)
    writer.writerows(data)

print('------------------')

import csv

columns = ['first_name', 'second_name', 'class_number', 'class_letter']
data = [['Тимур', 'Гуев', 11, 'А'], ['Руслан', 'Чаниев', 9, 'Б'], ['Роман', 'Белых', 10, 'В']]

with open('students2.dsv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(columns)
    writer.writerows(data)

print('------------------')

import csv

columns = ['first_name', 'second_name', 'class_number', 'class_letter']
data = [['Тимур', 'Гуев', 11, 'А'], ['Руслан', 'Чаниев', 9, 'Б'], ['Роман', 'Белых', 10, 'В']]

with open('students3.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter='\t', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(columns)
    writer.writerows(data)

print('------------------')

import csv

data = [{'first_name': 'Тимур', 'second_name': 'Гуев', 'class_number': 11, 'class_letter': 'А'},
        {'first_name': 'Руслан', 'second_name': 'Чаниев', 'class_number': 9, 'class_letter': 'Б'},
        {'first_name': 'Роман', 'second_name': 'Белых', 'class_number': 10, 'class_letter': 'В'}]

columns = ['first_name', 'second_name', 'class_number', 'class_letter']

with open('students4.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=columns, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

print('------------------')

import csv

data = [{'first_name': 'Тимур', 'second_name': 'Гуев', 'class_number': 11, 'class_letter': 'А'},
        {'first_name': 'Руслан', 'second_name': 'Чаниев', 'class_number': 9, 'class_letter': 'Б'},
        {'first_name': 'Роман', 'second_name': 'Белых', 'class_number': 10, 'class_letter': 'В'}]

columns = ['first_name', 'second_name', 'class_number', 'class_letter']

with open('students5.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=columns, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    writer.writerows(data)

print('------------------')