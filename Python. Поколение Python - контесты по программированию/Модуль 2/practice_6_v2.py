class Poker:
    def __init__(self, arr) -> None:
        self.card_set = set(arr)
        self.__algo(arr)

    def __algo(self, arr):
        if 1 == len(self.card_set):
            print('Шулер')
        elif 2 == len(self.card_set):
            if any(filter(lambda x: 4 == arr.count(x), arr)):
                print('Каре')
            else:
                print('Фулл Хаус')
        elif 3 == len(self.card_set):
            if any(filter(lambda x: 3 == arr.count(x), arr)):
                print('Сет')
            else:
                print('Две пары')
        elif 4 == len(self.card_set):
            print('Пара')
        else:
            if sorted(arr) == list(range(sorted(arr)[0], sorted(arr)[0] + len(arr))):
                print('Стрит')
            elif '101112131' == ''.join(sorted(map(str, arr))):
                print('Стрит')
            else:
                print('Старшая карта')
        
if __name__ == '__main__':
    Poker(list(map(int, input().split())))