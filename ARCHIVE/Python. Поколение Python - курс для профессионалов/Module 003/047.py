'''
Количество дней 😉
Напишите программу, которая определяет количество дней в заданном месяце.

Формат входных данных
На вход программе подаются год и порядковый номер месяца (начиная с 1), разделенные пробелом.

Формат выходных данных
Программа должна вывести единственное число — количество дней в введенном месяце.

Примечание 1. Январь имеет порядковый номер 1, Февраль — 2, Март — 3, и так далее.

Примечание 2. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/570049/tests_2575859.zip

Sample Input 1:
2008 1
Sample Output 1:
31

Sample Input 2:
1977 2
Sample Output 2:
28

Sample Input 3:
2000 3
Sample Output 3:
31
'''
from datetime import datetime
from calendar import monthrange

pattern = '%Y %m'
d = datetime.strptime(input(), pattern).date()
print(monthrange(d.year, d.month)[1])