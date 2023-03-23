'''
Only numbers
На вход программе подается неопределенное количество строк, 
каждая из которых содержит произвольное значение. Напишите программу 
с использованием конструкции try-except, которая выводит сумму всех 
введенных чисел, а затем — количество введенных нечисловых значений.

Формат входных данных
На вход программе подается неопределенное количество строк (хотя бы одна), 
каждая из которых содержит произвольное значение.

Формат выходных данных
Программа должна вывести сумму всех введенных чисел (тип int и float), 
а затем на следующей строке — количество введенных нечисловых значений.

Примечание 1. Если ни одно число введено не было, то сумма равна 0.

Примечание 2. Рассмотрим первый тест. Имеем три введенных числа, сумма которых равна:

100 + 10 + 1.1 = 111.1

Также три нечисловых значения, а именно: i'm number!, [1, 99], {'math', 'physics'}.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640050/tests_3013981.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_7/Module_7.2/Module_7.2.23

Sample Input 1:
100
i'm number!
10
[1, 99]
1.1
{'math', 'physics'}
Sample Output 1:
111.1
3

Sample Input 2:
10
10
Sample Output 2:
20
0

Sample Input 3:
abc
cda
xyz
Sample Output 3:
0
3
'''
import sys
# sys.stdin = open(file='008 tests.csv', mode='rt', encoding='utf-8', newline='')
from decimal import Decimal as dec, InvalidOperation

_count, _sum = int(), dec()
for _el in sys.stdin:
    try:
        _sum += dec(_el)
    except (InvalidOperation):
        _count += 1
print(_sum, _count, sep='\n')