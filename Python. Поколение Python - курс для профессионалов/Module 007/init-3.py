print('------------------')

# try:
#     num = int(input())
#     print('Квадрат числа равен:', num ** 2)
# except ValueError:
#     print('Вы ввели некорректные данные!')
# else:
#     print('Ошибки не произошло!')

# print('Работа программы завершена!')

print('------------------')

# try:
#     num = int(input())
#     print('Квадрат числа равен:', num ** 2)
# except ValueError:
#     print('Вы ввели некорректные данные!')
# finally:
#     print('Блок кода выполняется всегда!')

# print('Работа программы завершена!')

print('------------------')

# try:
#     file = open('data.txt', encoding='utf-8')
#     try:
#         text = file.read()
#     except:
#         print('При чтении из файла произошла ошибка!')
#     else:
#         print('Чтение из файла прошло успешно!')
#     finally:
#         file.close()
# except FileNotFoundError:
#     print('Файл с указанным именем не найден!')

print('------------------')

# try:
#     file = open('data.txt', encoding='utf-8')
#     try:
#         text = file.read()
#     finally:
#         file.close()
# except FileNotFoundError:
#     print('Файл с указанным именем не найден!')
# except:
#     print('Произошла ошибка!')

print('------------------')

# try:
#     х = 10 / 0
# finally:
#     print('Блoк finally')

print('------------------')

# def func():
#     try:
#         return 10
#     finally:
#         print('Выполняется блок finally!')

# print(func())

print('------------------')

# def func():
#     try:
#         return 10
#     finally:
#         return 20

# print(func())

print('------------------')

# def f():
#     try:
#         x = 10
#         return x
#     finally:
#         x = 20
          
# print(f())

print('------------------')

# def f():
#     try:
#         x = [10]
#         return x
#     finally:
#         x.append(20)
          
# print(f())

print('------------------')

# def f():
#     try:
#         return 10
#     except:
#         pass
#     else:
#         return 20
          
# print(f())

print('------------------')

# try:
#     # raise ValueError
#     print('try')
# finally:
#     print('Hello, Beegeek!')

print('------------------')

print(list(filter(int, ['1', '2', '3', '4', '5'])))

print('------------------')