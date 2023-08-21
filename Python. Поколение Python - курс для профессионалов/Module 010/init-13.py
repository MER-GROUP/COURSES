print('------------------')

from itertools import chain

chain_iter1 = chain('ABC', 'DEF')
print(*chain_iter1)

chain_iter2 = chain(enumerate('ABC'))
print(*chain_iter2)

for i in chain([1, 2, 3], ['a', 'b', 'c'], ('Timur', 29, 'Male', 'Teacher')):
    print(i, end=' ')

print('------------------')

from itertools import chain

chain_iter1 = chain.from_iterable(['ABC', 'DEF'])      # передаем список
print(*chain_iter1)

chain_iter2 = chain.from_iterable(enumerate('ABC'))
print(*chain_iter2)

for i in chain.from_iterable(['Timur', '29', 'Male', 'Teacher']):
    print(i, end=' ')

print('------------------')

# from itertools import chain

# for i in chain.from_iterable(('Timur', 29, 'Male', 'Teacher')):    # 29 - не итерируемый объект    
#     print(i, end=' ')

print('------------------')

from itertools import zip_longest

print(*zip([1, 2, 3], ['a', 'b', 'c', 'd', 'e']))
print(*zip_longest([1, 2, 3], ['a', 'b', 'c', 'd', 'e'])) # fillvalue=None
print(*zip_longest([1, 2, 3], ['a', 'b', 'c', 'd', 'e'], fillvalue='*'))
print(*zip_longest(['a', 'b', 'c', 'd', 'e'], [1, 2, 3], fillvalue=777))

print('------------------')

from itertools import tee

iter1, iter2 = tee([1, 'a', 2, 'b', 3, 'c']) # по умолчанию n=2

print(*iter1)
print(*iter2)

print('------------------')

from itertools import tee

result = tee(range(2, 7), 5)
print(type(result))
for i in result:
    print(*i)

for i in result:
    print(*i)
print(type(result))

print('------------------')

from itertools import tee

data = (i for i in range(10)) # используем генераторное выражение

iter1, iter2 = tee(data)

print(next(data))             # изменяем data                        

print(*iter1)
print(*iter2)

print('------------------')

from itertools import tee

data = [1, 2, 3, 4, 5]

iter1, iter2 = tee(data)

data.append(6)                      

print(*iter1)
print(*iter2)

print('------------------')

from itertools import pairwise

print(*pairwise('ABCDEFG'))
print(*pairwise([1, 2, 3, 4, 5]))

print('------------------')

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

print('------------------')

print(tuple(i for i in range(3)))
print(tuple([1, 2, 3]))

def f (*args):
    print(tuple(i for i in args))

print(f(1, 2, 3, [4, 5, 6]))

print('------------------')

import collections
def tee_my(iterable, n=2):
    it = iter(iterable)
    deques = [collections.deque() for i in range(n)]
    def gen(mydeque):
        while True:
            if not mydeque:             # when the local deque is empty
                try:
                    newval = next(it)   # fetch a new value and
                except StopIteration:
                    # return
                    break
                for d in deques:        # load it to all the deques
                    d.append(newval)
            temp = mydeque.popleft()
            print(temp)
            yield temp
    return tuple(gen(d) for d in deques)


a, b = tee_my([1, 2, 3, 4])
print(*a, *b)

print('------------------')

from itertools import chain

print(*chain([[1,2,3],[4,5,6],[7,8,9]]))

print(*chain.from_iterable([[1,2,3],[4,5,6],[7,8,9]]))

print('------------------')