# авторский алгоритм от BEEGIK
class Poker:
    def __init__(self, arr) -> None:
        self.__algo()

    # Решение. Двойная сортировка подсчетом: храним количество каждых карт в одном списке, 
    # а в другом количество количеств карт. Для того чтобы проверить карты на стрит, 
    # проверяем руку на наличие пяти идущих подряд карт, перебирая все возможные варианты. 
    # Для остальных комбинаций достаточно информации из первых двух списков, а также переменной, 
    # в которой хранится максимальное количество одинаковых карт. Проверяем комбинации в 
    # иерархическом порядке.
    def __algo(self):
        hand = input().split()
        cards = [0] * 13

        for i in range(5):
            addcard = int(hand[i])
            cards[addcard - 1] += 1

        cards_count = [0] * 6

        for i in cards:
            cards_count[i] += 1

        kind = max(cards)

        straight_draw = 0

        if kind == 1:
            for i in range(0, 9):
                if cards[i] + cards[i + 1] + cards[i + 2] + cards[i + 3] + cards[i + 4] > straight_draw:
                    straight_draw = cards[i] + cards[i + 1] + cards[i + 2] + cards[i + 3] + cards[i + 4]

        if kind > 4:
            print('Шулер')
        elif kind > 3:
            print('Каре')
        elif cards_count[3] == 1 and cards_count[2] == 1:
            print('Фулл Хаус')
        elif straight_draw == 5:
            print('Стрит')
        elif kind > 2:
            print('Сет')
        elif cards_count[2] == 2:
            print('Две пары')
        elif kind == 2:
            print('Пара')
        else:
            print('Старшая карта')
        
if __name__ == '__main__':
    Poker(list(map(int, input().split())))