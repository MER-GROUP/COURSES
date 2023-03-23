print('------------------')

# try:
#     num1 = int(input())
#     num2 = int(input())
#     print('Частное чисел равно', num1 / num2)
# except:
#     print('Вы ввели некорректные данные!')

# print('Работа программы завершена!')

print('------------------')

# try:
#     num1 = int(input())
#     num2 = int(input())
#     print('Частное чисел равно', num1 / num2)
# except ValueError:
#     print('Нужно было ввести числа!')
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')

# print('Работа программы завершена!')

print('------------------')

# try:
#     num1 = int(input())
#     num2 = int(input())
#     print('Частное чисел равно', num1 / num2)
# except (ValueError, IndexError, KeyError):
#     print('Тут обрабатываются сразу три типа ошибок!')
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
# except:
#     print('Если не сработал ни один из предыдущих блоков except.')

# print('Работа программы завершена!')

print('------------------')

# print('beegeek' + 2022)

print('------------------')

# num = int('beegeek')

print('------------------')

# nums = [1, 2, 3]

# print(nums[7])

print('------------------')

def this_fails():
    num = 1 / 0

try:
    this_fails()
except ZeroDivisionError:
    print('Деление на ноль')

print('------------------')