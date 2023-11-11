'''
Подозрительно просто 🤫
Вам доступна функция traffic(), реализованная с помощью цикла while, 
которая принимает в качестве аргумента число n и выводит n раз строку Не парковаться.

Перепишите данную функцию с использованием рекурсии, чтобы она выполняла ту же задачу.

Примечание. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию traffic(), но не код, вызывающий ее.

def traffic(n):
    while n > 0:
        print('Не парковаться')
        n -= 1

Sample Input 1:
traffic(3)
Sample Output 1:
Не парковаться
Не парковаться
Не парковаться

Sample Input 2:
traffic(5)
Sample Output 2:
Не парковаться
Не парковаться
Не парковаться
Не парковаться
Не парковаться

Sample Input 3:
traffic(0)
Sample Output 3:
'''
def traffic_while(n):
    while n > 0:
        print('Не парковаться')
        n -= 1

# 1
def traffic(n):
    def _repeat(num):
        if 0 < num:
            print('Не парковаться')
            _repeat(num-1)
    _repeat(n)

# 2
def traffic_2(n):
    if 0 < n:
        print('Не парковаться')
        traffic_2(n-1)

if __name__ == '__main__':
    traffic_while(3)
    print()
    traffic(3)
    print()
    traffic_2(3)