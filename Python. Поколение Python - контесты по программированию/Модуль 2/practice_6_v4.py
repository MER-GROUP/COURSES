class Poker:
    def __init__(self, arr) -> None:
        self.card = sorted({i: arr.count(i) for i in arr}.values())
        self.__algo(arr)

    def __algo(self, arr):
        if [5] == self.card:
            print('Шулер')
        elif [1, 4] == self.card:
            print('Каре')
        elif [2, 3] == self.card:
            print('Фулл Хаус')
        elif [1, 1, 3] == self.card:
            print('Сет')
        elif [1, 2, 2] == self.card:
            print('Две пары')
        elif [1, 1, 1, 2] == self.card:
            print('Пара')
        elif '101112131' == ''.join(sorted(map(str, arr))):
            print('Стрит')
        else: # elif [1, 1, 1, 1, 1] == self.card
            print('Стрит') if max(arr) == min(arr) + 4 else print('Старшая карта')
        
if __name__ == '__main__':
    Poker(list(map(int, input().split())))