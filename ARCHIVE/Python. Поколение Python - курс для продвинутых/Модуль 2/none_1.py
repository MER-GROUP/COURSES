# Литерал None
# определение типа NoneType (Синглтон)
print('##########')
var = None
print(type(var))

# Проверка на None
# используем оператор is
print('##########')
var = None
if var is None:
  print('None')
else:
  print('Not None')
  
# Проверка на None
# используем оператор ==
print('##########')
var = None
if var == None:
  print('None')
else:
  print('Not None')
  
# Сравнение None с другими типами данных
print('##########')
print(None == None)

print(None == 17)
print(None == 3.14)
print(None == True)
print(None == [1, 2, 3])
print(None == 'Beegeek')

print(None == 0)
print(None == False)
print(None == '')

# print(None > 0)
# print(None <= False)

# функция не возвращающая значения всегда возвращает None
def print_message() :
    print('Я - Тимур,')
    print('король матана. ')
    
print_message()
res = print_message()
print(res) # выведет None