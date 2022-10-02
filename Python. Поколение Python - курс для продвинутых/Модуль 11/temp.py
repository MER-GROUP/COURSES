vertical = sum(
    map(
        lambda x: len(x),
        map(
            str, [1, 2, 10, 23, 123, 3000]
        )
    )  
) + (len([1, 2, 10, 23, 123, 3000]) * 2) + (len([1, 2, 10, 23, 123, 3000]) - 1)
    
print(vertical)

print('----------------------------------------------')
print('dghghHJHJHJ'.swapcase())
print('----------------------------------------------')
print('dghghHJHJHJ'.swapcase())
print('----------------------------------------------')
from functools import reduce
import operator
print('----------------------------------------------')
print([256] * 4)
print(*range(3, -1, -1))
print('----------------------------------------------')