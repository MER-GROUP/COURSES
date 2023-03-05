'''
Не поленимся и запишем

Тимур составляет список покупок, но так как на его клавиатуре перестал 
работать блок с цифрами, то вместо указания количества товара числом, 
он добавляет его в список столько раз, сколько планирует купить. 
Все товары Тимур записывает в нижнем регистре через запятую.

Напишите программу, которая выводит все товары из данного списка покупок, 
указывая для каждого его количество.

Формат входных данных
На вход программе подается последовательность товаров, разделенных запятой без пробелов.

Формат выходных данных
Программа должны вывести все введенные товары, указывая для каждого, 
сколько раз он встречается в данной последовательности. Товары должны 
быть расположены в лексикографическом порядке, каждый на отдельной строке, 
в следующем формате:

<товар>: <количество>
Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/590120/tests_3090871.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_6/Module_6.7/Module_6.7.17

Sample Input 1:
лимон,лимон,лимон,груша,банан,банан,киви,киви,киви,киви
Sample Output 1:
банан: 2
груша: 1
киви: 4
лимон: 3

Sample Input 2:
рубашка,футболка,футболка,брюки,футболка,рубашка,носки,рубашка
Sample Output 2:
брюки: 1
носки: 1
рубашка: 3
футболка: 3
'''
from collections import Counter

[print(f'{k}: {v}') for k, v in sorted(Counter(input().split(',')).items())]