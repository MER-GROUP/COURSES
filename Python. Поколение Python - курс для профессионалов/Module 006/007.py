'''
Data
Вам доступен список кортежей data с данными о доходах некоторого образовательного ресурса.
 Первым элементом кортежа является название продукта, вторым — прибыль в долларах.

Дополните приведенный ниже код, чтобы он определил, какой общий доход принес каждый продукт 
и вывел названия всех продуктов, указав для каждого соответствующую общую прибыль. 
Продукты должны быть расположены в лексикографическом порядке, каждый на отдельной строке, 
в следующем формате:

<продукт>: $<общая прибыль>
Примечание. Начальная часть ответа выглядит так:

Books: $7969
Courses: $2991
...

from collections import defaultdict

data = [
    ('Books', 1343), 
    ('Books', 1166), 
    ('Merch', 616), 
    ('Courses', 966), 
    ('Merch', 1145), 
    ('Courses', 1061), 
    ('Books', 848), 
    ('Courses', 964), 
    ('Tutorials', 832), 
    ('Merch', 642), 
    ('Books', 815), 
    ('Tutorials', 1041), 
    ('Books', 1218), 
    ('Tutorials', 880), 
    ('Books', 1003), 
    ('Merch', 951), 
    ('Books', 920), 
    ('Merch', 729), 
    ('Tutorials', 977), 
    ('Books', 656)
]
'''
from collections import defaultdict

data = [
    ('Books', 1343), 
    ('Books', 1166), 
    ('Merch', 616), 
    ('Courses', 966), 
    ('Merch', 1145), 
    ('Courses', 1061), 
    ('Books', 848), 
    ('Courses', 964), 
    ('Tutorials', 832), 
    ('Merch', 642), 
    ('Books', 815), 
    ('Tutorials', 1041), 
    ('Books', 1218), 
    ('Tutorials', 880), 
    ('Books', 1003), 
    ('Merch', 951), 
    ('Books', 920), 
    ('Merch', 729), 
    ('Tutorials', 977), 
    ('Books', 656)
]

products = defaultdict(int)
for k, v in data:
    products[k] += v
[print(f'{k}: ${v}') for k, v in sorted(products.items())]