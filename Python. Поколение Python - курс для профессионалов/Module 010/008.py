'''
Дополните приведенный ниже код, чтобы в переменной infinite_love содержался итератор, 
бесконечно генерирующий единственное значение — строку i love beegeek!.

Примечание. В тестирующую систему сдайте программу, содержащую только 
необходимый итератор infinite_love.

infinite_love = ____

Sample Input 1:
print(next(infinite_love))
Sample Output 1:
i love beegeek!

Sample Input 2:
print(next(infinite_love))
print(next(infinite_love))
print(next(infinite_love))
Sample Output 2:
i love beegeek!
i love beegeek!
i love beegeek!
'''
infinite_love = iter(lambda: 'i love beegeek!', 'inf')

if __name__ == '__main__':
    print(next(infinite_love))

    print(next(infinite_love))
    print(next(infinite_love))
    print(next(infinite_love))