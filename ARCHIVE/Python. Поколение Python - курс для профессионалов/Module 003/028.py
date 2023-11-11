'''
Таймер
Часы показывают время в формате HH:MM:SS. 
На этих часах запустили таймер, который прозвенит через n секунд. 
Напишите программу, которое определит, какое время будет на часах, 
когда прозвенит таймер.

Формат входных данных
На вход программе в первой строке подается текущее время 
на часах в формате HH:MM:SS. В следующей строке вводится 
целое неотрицательное число n — количество секунд, 
через которое должен прозвенеть таймер.

Формат выходных данных
Программа должна вывести время в формате HH:MM:SS, 
которое будет на часах, когда прозвенит таймер.

Примечание. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/570050/tests_2505143.zip

Sample Input 1:
09:00:00
90
Sample Output 1:
09:01:30

Sample Input 2:
23:59:59
1
Sample Output 2:
00:00:00

Sample Input 3:
13:34:46
456
Sample Output 3:
13:42:22
'''
from datetime import time, timedelta

timer, sec = time.fromisoformat(input()), timedelta(seconds=int(input()))
total_sec = (
    timedelta(hours=timer.hour, minutes=timer.minute, seconds=timer.second) + sec
).total_seconds()
print(
    f'{str(int(total_sec // 60 // 60 % 24)).zfill(2)}:{str(int(total_sec // 60 % 60)).zfill(2)}:{str(int(total_sec % 60)).zfill(2)}'
)