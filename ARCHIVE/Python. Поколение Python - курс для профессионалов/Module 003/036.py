'''
Снова не успел

Дан режим работы магазина:

Понедельник    9:00 - 21:00
Вторник        9:00 - 21:00
Среда          9:00 - 21:00
Четверг        9:00 - 21:00
Пятница        9:00 - 21:00
Суббота        10:00 - 18:00
Воскресенье    10:00 - 18:00

Напишите программу, которая принимает на вход текущие дату и время 
и определяет количество минут, оставшееся до закрытия магазина.

Формат входных данных
На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.

Формат выходных данных
Программа должна вывести количество минут, которое осталось до закрытия магазина, 
или текст Магазин не работает, если он закрыт.

Примечание. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/571244/tests_2506803.zip

Sample Input 1:
01.11.2021 20:45
Sample Output 1:
15

Sample Input 2:
02.11.2021 21:15
Sample Output 2:
Магазин не работает

Sample Input 3:
07.11.2021 10:00
Sample Output 3:
480
'''
from datetime import datetime

current_date = datetime.strptime(input() ,'%d.%m.%Y %H:%M')
shop_times = {
    1: (current_date.replace(hour=9, minute=0), current_date.replace(hour=21, minute=0)),
    2: (current_date.replace(hour=9, minute=0), current_date.replace(hour=21, minute=0)),
    3: (current_date.replace(hour=9, minute=0), current_date.replace(hour=21, minute=0)),
    4: (current_date.replace(hour=9, minute=0), current_date.replace(hour=21, minute=0)),
    5: (current_date.replace(hour=9, minute=0), current_date.replace(hour=21, minute=0)),
    6: (current_date.replace(hour=10, minute=0), current_date.replace(hour=18, minute=0)),
    7: (current_date.replace(hour=10, minute=0), current_date.replace(hour=18, minute=0))
}

if (shop_times[current_date.isoweekday()][0].time() \
        <= current_date.time() \
        < shop_times[current_date.isoweekday()][1].time()):
    print(
        int((shop_times[current_date.isoweekday()][1] - current_date).total_seconds() // 60)
    )
else:
    print('Магазин не работает')