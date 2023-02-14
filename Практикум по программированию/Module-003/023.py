'''
Первоклассная задача
'''
import sys

sys.stdin = open(file='023.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(
    map(
        str.strip,
        sys.stdin.readlines()
    )
)
print(arr) # test