'''
Florida hurricane dates
В переменной florida_hurricane_dates хранится список дат, 
в которые произошел ураган во Флориде с 1950 по 2017 год.

Дополните приведенный ниже код, чтобы он вывел самую раннюю дату 
из списка florida_hurriance_dates в трех различных форматах:

в стандарте ISO (YYYY-MM-DD)
в типичном для России стиле (DD.MM.YYYY)
в типичном для Америки стиле (MM/DD/YYYY)
Примечание 1. Считайте, что переменная florida_hurricane_dates 
объявлена и доступна вашей программе.

Примечание 2. Считайте, что тип date уже импортирован в программу.
'''
# присваиваем самую раннюю дату урагана в переменную first_date
first_date = min(florida_hurricane_dates)

# конвертируем дату в ISO и RU формат
iso = 'Дата первого урагана в ISO формате: ' + first_date.isoformat() # (YYYY-MM-DD)
ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%d.%m.%Y') # (DD.MM.YYYY)
us = 'Дата первого урагана в US формате: ' + first_date.strftime('%m/%d/%Y') # (MM/DD/YYYY)

print(iso)
print(ru)
print(us)