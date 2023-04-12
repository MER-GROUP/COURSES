print('------------------')

def get_all_str(data):
    if type(data) == str:
        print(data, end=' ') # базовый случай
    if type(data) == list:
        for i in data:
            get_all_str(i)   # рекурсивный случай

numbers = ['1', ['2', '3', ['4'], ['5', ['6', '7']]]]

get_all_str(numbers)

print('------------------')

def find_key(data, key):
    if key in data:
        return data[key]             # базовый случай
    
    for k, v in data.items():
        if type(v) == dict:
            value = find_key(v, key) # рекурсивный случай
            if value is not None:
                return value 

info = {'name': 'Alyson', 
        'surname': 'Hannigan', 
        'birthday': {'day': 24, 'month': 'March', 'year': 1974},
        'family': {'parents': {'mother': 'Emilie Posner', 'father': 'Alan Hannigan'}}}

print(find_key(info, 'year'))
print(find_key(info, 'father'))

print('------------------')

from sys import getrecursionlimit

limit = getrecursionlimit()
print(limit)

print('------------------')

import sys

limit = sys.getrecursionlimit()
print(limit)

sys.setrecursionlimit(6000)
new_limit = sys.getrecursionlimit()
print(new_limit)

print('------------------')