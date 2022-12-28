'''
Количество дней 😎
Напишите программу, которая определяет количество дней в заданном месяце.

Формат входных данных
На вход программе подаются год и полное название месяца на английском, 
разделенные пробелом.

Формат выходных данных
Программа должна вывести единственное число — количество дней 
в введенном месяце.

Примечание. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/570049/tests_2575860.zip

Sample Input 1:
1983 January
Sample Output 1:
31

Sample Input 2:
1956 February
Sample Output 2:
29

Sample Input 3:
1959 March
Sample Output 3:
31
'''
from datetime import datetime
from calendar import monthrange

pattern = '%Y %B'
d = datetime.strptime(input(), pattern).date()
print(monthrange(d.year, d.month)[1])