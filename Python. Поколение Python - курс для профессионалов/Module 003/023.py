'''
Функция is_available_date() 🌶️
Во время визита очередного гостя сотрудникам отеля приходится проверять, 
доступна ли та или иная дата для бронирования номера.

Реализуйте функцию is_available_date(), которая принимает 
два аргумента в следующем порядке:

booked_dates — список строковых дат, недоступных для бронирования. 
Элементом списка является либо одиночная дата, либо период (две даты через дефис). Например:
['04.11.2021', '05.11.2021-09.11.2021']
date_for_booking — одиночная строковая дата или период (две даты через дефис), 
на которую гость желает забронировать номер. Например:
'01.11.2021' или '01.11.2021-04.11.2021'
Функция is_available_date() должна возвращать True, 
если дата или период date_for_booking полностью доступна для бронирования. 
В противном случае функция должна возвращать False.

Примечание 1. Гарантируется, что в периоде левая дата всегда меньше правой.

Примечание 2. В периоде (две даты через дефис) граничные даты включены.

Примечание 3. В тестирующую систему сдайте программу, 
содержащую только необходимую функцию is_available_date(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/611754/tests_2506745.zip

Sample Input 1:
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))
Sample Output 1:
True

Sample Input 2:
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))
Sample Output 2:
False

Sample Input 3:
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '06.11.2021'
print(is_available_date(dates, some_date))
Sample Output 3:
False
'''
from datetime import datetime

def is_available_date(booked_dates: list[str], date_for_booking: str):
    dates_dict = {'one': [], 'two': []}
    for s in booked_dates:
        arr = s.split('-')
        arr = list(map(lambda x: datetime.strptime(x, '%d.%m.%Y'), arr))
        if 1 == len(arr):
            dates_dict['one'] = arr
        else:
            dates_dict['two'] = arr
    
    my_dates_dict = {'one': [], 'two': []}
    arr = date_for_booking.split('-')
    arr = list(map(lambda x: datetime.strptime(x, '%d.%m.%Y'), arr))
    if 1 == len(arr):
        my_dates_dict['one'] = arr
    else:
        my_dates_dict['two'] = arr

    print(dates_dict) # test
    # print(my_dates_dict) # test

    # res_arr = list()
    # if 1 == len(arr):
    #     for date_booked in dates_dict['one']:
    #         if my_dates_dict['one'] == date_booked:
    #             res_arr.append(False)
    #         else:
    #             res_arr.append(True)
    #     for date_booked_1, date_booked_2 in dates_dict['two']:        #############
    #         if date_booked_1 <= my_dates_dict['one'] <= date_booked_2:
    #             res_arr.append(False)
    #         else:
    #             res_arr.append(True)
    # else:
    #     my_dates_1, my_dates_2 = my_dates_dict['two']
    #     for date_booked in dates_dict['one']:
    #         if my_dates_1 <= date_booked <= my_dates_2:
    #             res_arr.append(False)
    #         else:
    #             res_arr.append(True)
    #     for date_booked_1, date_booked_2 in dates_dict['two']:        ############
    #         if my_dates_1 <= date_booked_1 <= date_booked_2 <= my_dates_2:
    #             res_arr.append(False)
    #         else:
    #             res_arr.append(True)

    # return all(res_arr)

if __name__ == '__main__':
    dates = ['04.11.2021', '05.11.2021-09.11.2021']
    some_date = '01.11.2021'
    print(is_available_date(dates, some_date))

    dates = ['04.11.2021', '05.11.2021-09.11.2021']
    some_date = '01.11.2021-04.11.2021'
    print(is_available_date(dates, some_date))

    dates = ['04.11.2021', '05.11.2021-09.11.2021']
    some_date = '06.11.2021'
    print(is_available_date(dates, some_date))

    dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
    some_date = '09.11.2021'
    print(is_available_date(dates, some_date))