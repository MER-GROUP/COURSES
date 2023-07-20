'''
Функция card_deck()
Реализуйте генераторную функцию card_deck(), которая принимает один аргумент:

suit — одна из четырех карточных мастей: пик, треф, бубен, червей

Функция должна возвращать генератор, циклично порождающий колоду игральных карт без масти suit. 
Каждая карта должна представлять собой строку в следующем формате:

<номинал> <масть>

Например, 7 пик, валет треф, дама бубен, король червей, туз пик.

Примечание 1. Карты, генерируемые итератором, должны располагаться сначала по величине номинала, 
затем масти.

Примечание 2. Старшинство мастей по возрастанию: пики, трефы, бубны, червы. Старшинство карт 
в масти по возрастанию: двойка, тройка, четверка, пятерка, шестерка, семерка, восьмерка, 
девятка, десятка, валет, дама, король, туз.

Примечание 3. Масти не требуют склонения и независимо от номинала должны сохранять следующее 
написание: пик, треф, бубен, червей.

Примечание 4. В тестирующую систему сдайте программу, содержащую только необходимую генераторную 
функцию card_deck(), но не код, вызывающий ее.

Примечание 5. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640048/tests_2777687.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.5/Module_10.5.20

Sample Input 1:
generator = card_deck('пик')
print(next(generator))
print(next(generator))
print(next(generator))
Sample Output 1:
2 треф
3 треф
4 треф

Sample Input 2:
generator = card_deck('треф')
cards = [next(generator) for _ in range(40)]
print(*cards)
Sample Output 2:
2 пик 3 пик 4 пик 5 пик 6 пик 7 пик 8 пик 9 пик 10 пик валет пик дама пик король пик 
туз пик 2 бубен 3 бубен 4 бубен 5 бубен 6 бубен 7 бубен 8 бубен 9 бубен 10 бубен валет бубен 
дама бубен король бубен туз бубен 2 червей 3 червей 4 червей 5 червей 6 червей 7 червей 
8 червей 9 червей 10 червей валет червей дама червей король червей туз червей 2 пик
'''
from __future__ import annotations
from _collections_abc import Generator

def card_deck(suit: str) -> Generator:
    numbers = tuple(range(2, 11)) + ('валет',  'дама',  'король', 'туз')
    numbers_step = 0
    numbers_len = len(numbers)

    suits = ['пик', 'треф', 'бубен', 'червей']
    del suits[suits.index(suit)]
    suits_step = 0
    suits_len = len(suits)

    while True:
        yield f'{numbers[numbers_step]} {suits[suits_step]}'
        numbers_step += 1
        if numbers_step == numbers_len:
            numbers_step = 0
            suits_step += 1
            if suits_step == suits_len:
                suits_step = 0
            
if __name__ == '__main__':
    generator = card_deck('пик')
    print(next(generator))
    print(next(generator))
    print(next(generator))

    generator = card_deck('треф')
    cards = [next(generator) for _ in range(40)]
    print(*cards)