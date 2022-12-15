'''
Коровы
По данному числу n закончите фразу 
"На лугу пасется..." одним из возможных продолжений: 
"n коров", "n корова", "n коровы", правильно склоняя слово "корова".

Входные данные
Дано число n (n<100).

Выходные данные
Программа должна вывести введенное число n 
и одно из слов (на латинице): korov, korova или korovy, 
например, 1 korova, 2 korovy, 5 korov. 
Между числом и словом должен стоять ровно один пробел.

Sample Input:
1
Sample Output:
1 korova
'''
def choose_plural(amount: int, declensions: tuple):
    if str(amount).endswith(('0', '5', '6', '7', '8', '9', '11', '12', '13', '14')):
        return f'{amount} {declensions[2]}'
    elif str(amount).endswith('1'):
        return f'{amount} {declensions[0]}'
    else:
        return f'{amount} {declensions[1]}'

if __name__ == '__main__':
    # print(choose_plural(int(input()), ('пример', 'примера', 'примеров')))
    print(choose_plural(int(input()), ('korova', 'korovy', 'korov')))