'''
Количество секунд
Напишите программу, которая принимает на вход время 
и выводит целое количество секунд, прошедшее с начала суток.

Формат входных данных
На вход программе подается время в формате HH:MM:SS.

Формат выходных данных
Программа должна вывести целое количество секунд, прошедшее с начала суток.

Примечание 1. Началом суток считается момент времени, соответствующий 00:00:00.

Примечание 2. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/570050/tests_2505142.zip

Sample Input 1:
00:01:01
Sample Output 1:
61

Sample Input 2:
00:00:00
Sample Output 2:
0

Sample Input 3:
12:12:12
Sample Output 3:
43932
'''
from datetime import datetime, timedelta
t = (datetime.strptime(input(), '%H:%M:%S') - datetime(year=1900, month=1, day=1)).total_seconds()
print(int(t))