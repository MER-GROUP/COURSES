print('------------------')

from datetime import date, time

day, month, year = input('Введите дату в формате ДД.ММ.ГГГГ ').split('.')
hour, minute, second = input('Введите время в формате ЧЧ:ММ:СС ').split(':')

# создаем объект типа date
my_date = date(int(year), int(month), int(day)) 
# создаем объект типа time       
my_time = time(int(hour), int(minute), int(second))    

print(my_date)
print(my_time)

print('------------------')

from datetime import date, time

try:
    day, month, year = input('Введите дату в формате ДД.ММ.ГГГГ ').split('.')
    my_date = date(int(year), int(month), int(day))
    print(my_date)
except ValueError:
    print('Ошибка ввода')

print('------------------')

from datetime import date, time

while True:
    try:
        day, month, year = input('Введите дату в формате ДД.ММ.ГГГГ ').split('.')
        my_date = date(int(year), int(month), int(day))
        print('Введена корректная дата:', my_date)
        break
    # перехватываем ошибку типа ValueError
    except ValueError:    
        print('Введенная дата не является корректной, попробуйте еще раз')

print('------------------')

from datetime import date, time

while True:
    try:
        day, month, year = input('Введите дату в формате ДД.ММ.ГГГГ ').split('.')
        my_date = date(int(year), int(month), int(day))
        print('Введена корректная дата:', my_date)
        break
    # перехватываем любую ошибку
    except:      
        print('Введенная дата не является корректной, попробуйте еще раз')

print('------------------')

from datetime import date

my_date = date.fromisoformat('2020-01-31')

print(my_date)
print(type(my_date))

print('------------------')