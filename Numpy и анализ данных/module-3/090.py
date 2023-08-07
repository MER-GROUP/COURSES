'''
Поиски утерянной магии тройки

Глубоко в древних темницах, скрытых глубоко под землей, находится таинственный свиток, 
который хранит в себе знание о древней магии и секретах, присущих тайнам Вселенной. 
Но чтобы раскрыть его секреты, вам нужно пройти через непростой путь, полный опасностей 
и испытаний.

Вы - молодой археолог, решивший исследовать эти тайные подземелья, и вы не знаете, 
что вас ждет. Вам нужно быть осторожным и знать магию, чтобы преодолеть все препятствия, 
которые вы встретите на своем пути.

Когда вы идете по темным коридорам, вы замечаете, что все стены украшены символами, 
которые напоминают числа. Вы понимаете, что это древний язык магии, который можно 
расшифровать только с помощью программирования. Вы достаете свой ноутбук и начинаете 
писать функцию getArrayElementsDivisibleByThree(arr), которая принимает на вход 
одномерный массив чисел и возвращает массив, содержащий только те числа, которые 
делятся на 3 без остатка.

Sample Input:
-5 -11 8 5 3 -3 -11 -1 6 -6 10 -9 -5 7 -6 -8 11 5 -7 -5 9 11
Sample Output:
[ 3 -3  6 -6 -9 -6  9]
'''
import numpy as np

def getArrayElementsDivisibleByThree(arr: np) -> np:
    return arr[0==arr%3]

if __name__ == '__main__':
    print(
        getArrayElementsDivisibleByThree(
            np.array(
                object='-5 -11 8 5 3 -3 -11 -1 6 -6 10 -9 -5 7 -6 -8 11 5 -7 -5 9 11'.split(),
                dtype=int
            )
        )
    )