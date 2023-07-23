'''
Такие правила

Том Сойер и его друг соревнуются в беге. 
Напишите функцию find_faster_runner(tom_speed, friend_speed), которая принимает 
на вход два одномерных массива NumPy tom_speed и friend_speed, содержащие 
скорости Тома и его друга соответственно в различных забегах. Функция возвращает 
строку "Tom" , если Том победил хотя бы в одном забеге и строку "Friend" 
если Том ни разу не превзошел своего друга. Если скорости обоих бегунов 
всегда равны, функция должна вернуть строку "Draw". 

Нужно написать только функцию, вызывать ее не нужно.

Sample Input:
1 2 3 2 4 5 2 3
2 2 4 5 5 6 3 1
Sample Output:
Tom
'''
import numpy as np

def find_faster_runner(tom_speed: np, friend_speed: np) -> str:
    return ('Tom', 'Friend', 'Draw')[
        sum(
            (
                np.all(tom_speed<=friend_speed),
                np.all(tom_speed==friend_speed)
            )
        )
    ]

if __name__ == '__main__':
    print(
        find_faster_runner(
            np.fromstring('1 2 3 2 4 5 2 3', dtype=None, sep=' '),
            np.fromstring('2 2 4 5 5 6 3 1', dtype=None, sep=' ')
        )
    )