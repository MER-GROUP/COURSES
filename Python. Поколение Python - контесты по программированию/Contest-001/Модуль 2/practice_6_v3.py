class Poker:
    def __init__(self, arr) -> None:
        self.card = {i: arr.count(i) for i in arr}.values()
        self.__algo(arr)

    def __algo(self, arr):
        if 1 == len(self.card):
            print('Шулер')
        elif 2 == len(self.card):
            print('Фулл Хаус') if 2 in self.card else print('Каре')
        elif 3 == len(self.card):
            print('Сет') if 3 in self.card else print('Две пары')
        elif 4 == len(self.card):
            print('Пара')
        elif '101112131' == ''.join(sorted(map(str, arr))):
            print('Стрит')
        else: # len(d) == 5
            print('Стрит') if max(arr) == min(arr) + 4 else print('Старшая карта')
        
if __name__ == '__main__':
    Poker(list(map(int, input().split())))