'''
Апельсины бочками
Бизнесмен Василий после прочтения известной книги решил 
открыть новый бизнес – отгружать апельсины бочками. 
Партнерам важно знать сколько именно бочек апельсинов отгружается каждый день.

Мобильный телефон Василия поддерживает только транслит, 
поэтому он передает сообщения вида "N bochek" . Например, "3 bochki" или "1 bochka" .

Напишите программу, которая выбирает правильное 
слово (из "bochka" , "bochek" , "bochki" ) в зависимости от N.

Входные данные
Одно число N (0 ≤ N ≤ 1000).

Выходные данные
Фраза на транслите (см. примеры).

Sample Input:
15
Sample Output:
15 bochek
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
    print(choose_plural(int(input()), ('bochka', 'bochki', 'bochek')))