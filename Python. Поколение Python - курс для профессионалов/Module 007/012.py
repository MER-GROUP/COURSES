'''
Функция get_weekday()
Реализуйте функцию get_weekday(), которая принимает один аргумент:

number — целое число (от 1 до 7 включительно)

Функция должна возвращать полное название дня недели на русском, 
который соответствует числу number, при этом:

если number не является целым числом, функция должна возбуждать исключение: 
TypeError('Аргумент не является целым числом')

если number является целым числом, но не принадлежит отрезку [1;7], 
функция должна возбуждать исключение: 
ValueError('Аргумент не принадлежит требуемому диапазону')

Примечание 1. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию get_weekday(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640051/tests_2713716.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_7/Module_7.4/Module_7.4.18

Sample Input 1:
print(get_weekday(1))
Sample Output 1:
Понедельник

Sample Input 2:
try:
    print(get_weekday('hello'))
except Exception as err:
    print(err)
    print(type(err))
Sample Output 2:
Аргумент не является целым числом
<class 'TypeError'>

Sample Input 3:
try:
    print(get_weekday(8))
except ValueError as err:
    print(err)
    print(type(err))
Sample Output 3:
Аргумент не принадлежит требуемому диапазону
<class 'ValueError'>
'''
from calendar import day_name
from locale import setlocale, LC_ALL
setlocale(LC_ALL, 'ru_RU.UTF-8')

def get_weekday(number: int) -> str:
    try:
        # if not(issubclass(type(number), int)) or number % 1:
        # if not(isinstance(number, int)) or number % 1:
        if number % 1:
            raise TypeError('Аргумент не является целым числом')
        elif not(1 <= number <= 7):
            raise ValueError('Аргумент не принадлежит требуемому диапазону')
        else:
            return day_name[number - 1]
    except TypeError as e:
        # print(e)
        # raise
        # raise TypeError('Аргумент не является целым числом') from None
        raise TypeError('Аргумент не является целым числом')
    except ValueError as e:
        # print(e)
        # raise
        # raise ValueError('Аргумент не принадлежит требуемому диапазону') from None
        raise ValueError('Аргумент не принадлежит требуемому диапазону')

if __name__ == '__main__':
    print('00000')
    print(day_name[0])
    print('11111')
    print(get_weekday(1))
    print('22222')
    try:
        print(get_weekday('hello'))
    except Exception as err:
        print(err)
        print(type(err))
    print('33333')
    try:
        print(get_weekday(8))
    except ValueError as err:
        print(err)
        print(type(err))
    print('44444')
    try:
        print(get_weekday('4'))
    except Exception as err:
        print(err)
        print(type(err))
    print('55555')