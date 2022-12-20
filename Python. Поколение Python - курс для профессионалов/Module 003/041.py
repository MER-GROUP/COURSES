'''
FAKE NEWS 🌶️
Команда BEEGEEK планирует выпустить свой новый курс 08.11.2022 ровно в 12:00. 
Напишите программу, которая принимает на вход текущие дату и время и определяет, 
сколько времени осталось до выхода курса.

Формат входных данных
На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.

Формат выходных данных
Программа должна вывести текст с указанием количества дней и часов, 
оставшихся до выхода курса, в следующем формате:

До выхода курса осталось: <кол-во дней> дней и <кол-во часов> часов
Если в данном случае количество часов равно нулю, то вывести нужно только дни.

Если количество дней равно нулю, то вывести нужно только часы и минуты в следующем формате:

До выхода курса осталось: <кол-во часов> часов и <кол-во минут> минут
Если в данном случае количество минут равно нулю, то вывести нужно только часы. 
Аналогично, если количество часов равно нулю, то вывести нужно только минуты.

Если введенные дата и время больше либо равны 08.11.2022 12:00, 
программа должна вывести текст: 

Курс уже вышел!

Примечание 1. Программа должна подбирать правильную форму 
для существительных «день» и «минута». Для этого можете смело взять свою функцию 
choose_plural() из этой задачи.
https://stepik.org/lesson/569748/step/13?unit=564262

Примечание 2. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/571244/tests_2506742.zip

Sample Input 1:
16.11.2021 06:30
Sample Output 1:
До выхода курса осталось: 357 дней и 5 часов

Sample Input 2:
6.11.2022 12:00
Sample Output 2:
До выхода курса осталось: 2 дня

Sample Input 3:
08.11.2022 10:30
Sample Output 3:
До выхода курса осталось: 1 час и 30 минут

Sample Input 4:
08.11.2022 09:00
Sample Output 4:
До выхода курса осталось: 3 часа

Sample Input 5:
08.11.2022 11:40
Sample Output 5:
До выхода курса осталось: 20 минут

Sample Input 6:
08.11.2022 12:15
Sample Output 6:
Курс уже вышел!
'''
from datetime import datetime

def choose_plural(amount: int, declensions: tuple):
    if str(amount).endswith(('0', '5', '6', '7', '8', '9', '11', '12', '13', '14')):
        return f'{amount} {declensions[2]}'
    elif str(amount).endswith('1'):
        return f'{amount} {declensions[0]}'
    else:
        return f'{amount} {declensions[1]}'

if __name__ == '__main__':
    course_datetime = datetime(year=2022, month=11, day=8, hour=12, minute=0)
    pattern_date = '%d.%m.%Y'
    pattern_time = '%H:%M'
    current_datetime = datetime.strptime(input(), f'{pattern_date} {pattern_time}')
    days_tuple = ('день', 'дня', 'дней')
    hours_tuple = ('час', 'часа', 'часов')
    minutes_tuple = ('минута', 'минуты', 'минут')

    if current_datetime < course_datetime:
        delta = abs(current_datetime - course_datetime)
        # print(f'delta = {delta}') # test
        days = delta.days
        # print(f'days = {days}') # test
        hours = int(delta.total_seconds() // 60 // 60 % 24)
        # print(f'hours = {hours}') # test
        minutes = int(delta.total_seconds() // 60 % 60)
        # print(f'minutes = {minutes}') # test

        if 0 != days and 0 != hours:
            print(f'До выхода курса осталось: {choose_plural(days, days_tuple)} и {choose_plural(hours, hours_tuple)}')
        elif 0 != days and 0 == hours:
            print(f'До выхода курса осталось: {choose_plural(days, days_tuple)}')
        elif 0 == days and 0 != hours and 0 != minutes:
            print(f'До выхода курса осталось: {choose_plural(hours, hours_tuple)} и {choose_plural(minutes, minutes_tuple)}')
        elif 0 == days and 0 != hours and 0 == minutes:
            print(f'До выхода курса осталось: {choose_plural(hours, hours_tuple)}')
        elif 0 == days and 0 == hours and 0 != minutes:
            print(f'До выхода курса осталось: {choose_plural(minutes, minutes_tuple)}')
    else:
        print('Курс уже вышел!')