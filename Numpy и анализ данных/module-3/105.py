'''
Фильтрация отзывов на онлайн-маркетплейсе

Задача заключается в том, чтобы использовать булево индексирование для фильтрации 
отзывов на онлайн-маркетплейсе. Например, нужно выбрать только те отзывы, которые 
содержат ключевые слова, такие как "отличный", "качество", "быстрая доставка" и т.д. 
Для этого необходимо создать функцию filter_feedback(feeds, keywords), принимающую 
два numpy массива feeds (массив с отзывами) и keywords - список Python, содержащий 
ключевые слова, по которым фильтруются элементы первого списка.

Вывод: массив с отзывами, в которых упоминается хотя бы одно ключевое слово из второго списка.

Sample Input:
Отличный телефон!, Очень плохое качество экрана, Быстрая доставка и качественный товар, Телефон просто супер, Ужасный сервис и низкое качество товара, Купил телефон неделю назад и пока всё нравится, Это лучший телефон, который я когда-либо покупал, Очень неудобный дизайн, Отличный звук и мощная батарея, Не стоит своих денег
отличный качественный супер лучший

Sample Output:
Отличный телефон! Быстрая доставка и качественный товар Телефон просто супер Это лучший телефон Отличный звук и мощная батарея
'''
import numpy as np
from datetime import datetime, timedelta
from dateutil.parser import parse

def filter_feedback(feeds: np, keywords: np):
    feeds_lower = np.array([i.lower() for i in feeds])

    mask = list()
    for f in feeds_lower:
        for k in keywords:
            if k in f:
                mask.append(True)
                break
        else:
            mask.append(False)
    mask_np = np.array(mask)
    
    return feeds[mask_np]

if __name__ == '__main__':
    print(
        filter_feedback(
            np.array(
                object='Отличный телефон!, Очень плохое качество экрана, Быстрая доставка и качественный товар, Телефон просто супер, Ужасный сервис и низкое качество товара, Купил телефон неделю назад и пока всё нравится, Это лучший телефон, который я когда-либо покупал, Очень неудобный дизайн, Отличный звук и мощная батарея, Не стоит своих денег'.split(', '),
                dtype=str
            ),
            np.array(
                object='отличный качественный супер лучший'.split(' '),
                dtype=str
            )
        )
    )