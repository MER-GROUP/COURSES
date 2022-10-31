'''
Угадайка
Определите по тестам условие задачи и напишите программу для ее решения.

Формат входных данных
На вход программе подается единственное натуральное число.

Формат выходных данных
Программа должна вывести единственное натуральное число.

Примечание 1. Подсказки в комментариях неприемлемы.

Примечание 2. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/718107/tests_3019841.zip
'''
class Ugaday:
    def __init__(self, n: int=1) -> None:
        print(self.algo(n))

    def algo(self, n: int=1) -> int:
        from functools import reduce
        import operator
        return reduce(
            operator.add,
            map(
                lambda x: int(x) + 1,
                list(str(n))
            )
        )

if __name__ == '__main__':
    Ugaday(int(input()))