'''
Итератор CardDeck
Реализуйте класс CardDeck, порождающий итераторы, конструктор которого 
не принимает никаких аргументов.

Итератор класса CardDeck должен генерировать последовательность из 52 игральных карт, 
а после возбуждать исключение StopIteration. Каждая карта должна представлять 
собой строку в следующем формате:

<номинал> <масть>

Например, 7 пик, валет треф, дама бубен, король червей, туз пик.

Примечание 1. Карты, генерируемые итератором, должны располагаться сначала 
по величине номинала, затем масти.

Примечание 2. Старшинство мастей по возрастанию: пики, трефы, бубны, червы. 
Старшинство карт в масти по возрастанию: двойка, тройка, четверка, пятерка, шестерка, 
семерка, восьмерка, девятка, десятка, валет, дама, король, туз.

Примечание 3. Масти не требуют склонения и независимо от номинала должны сохранять 
следующее написание: пик, треф, бубен, червей.

Примечание 4. В тестирующую систему сдайте программу, содержащую только необходимый класс CardDeck.

Примечание 5. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/669733/tests_2778510.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.4/Module_10.4.13

Sample Input 1:
cards = CardDeck()
print(next(cards))
print(next(cards))
Sample Output 1:
2 пик
3 пик

Sample Input 2:
cards = list(CardDeck())
print(cards[9])
print(cards[23])
print(cards[37])
print(cards[51])
Sample Output 2:
валет пик
дама треф
король бубен
туз червей
'''
class CardDeck:
    def __init__(self) -> None:
        self.card_suit = ('пик', 'треф', 'бубен', 'червей')
        self.card_suit_len = len(self.card_suit)
        self.card_suit_index = 0

        self.card_number = tuple(map(str, range(2, 11))) + ('валет', 'дама', 'король', 'туз')
        self.card_number_len = len(self.card_number)
        self.card_number_index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.card_number_index == self.card_number_len:
            self.card_number_index = 0
            self.card_suit_index += 1

        if self.card_suit_index == self.card_suit_len:
            raise StopIteration

        card_number = self.card_number[self.card_number_index]
        card_suit = self.card_suit[self.card_suit_index]
        self.card_number_index += 1

        return ' '.join((card_number, card_suit))

if __name__ == '__main__':
    cards = CardDeck()
    print(next(cards))
    print(next(cards))

    cards = list(CardDeck())
    print(cards[9])
    print(cards[23])
    print(cards[37])
    print(cards[51])