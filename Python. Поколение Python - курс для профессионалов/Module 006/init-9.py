print('------------------')

from collections import Counter

letters = Counter('mississippi')
numbers = Counter([5, 6, 7, 1, 3, 9, 9, 1, 2, 5, 5, 7, 7, 9])

print(letters.most_common())
print(numbers.most_common())

print('------------------')

from collections import Counter

letters = Counter('mississippi')
numbers = Counter([5, 6, 7, 1, 3, 9, 9, 1, 2, 5, 5, 7, 7, 9])

print(letters.most_common(3))
print(numbers.most_common(4))

print('------------------')

from collections import Counter

letters = Counter('mississippi')
numbers = Counter([5, 6, 7, 1, 3, 9, 9, 1, 2, 5, 5, 7, 7, 9])

print(letters.most_common()[-1])
print(letters.most_common()[::-1])
print(numbers.most_common()[-3:-1])

print('------------------')

from collections import Counter

letters = Counter('mississippi')
numbers = Counter([5, 6, 7, 1, 3, 9, 9, 1, 2, 5, 5, 7, 7, 9])

print(list(letters.elements()))
print(list(numbers.elements()))

print('------------------')

from collections import Counter

letters = Counter(i=4, s=4, a=0, p=2, b=-98, m=1)
print(list(letters.elements()))

print('------------------')

from collections import Counter

letters = Counter(i=4, s=4, a=0, p=2, b=-98, m=1)
print(letters.total())

print('------------------')

from collections import Counter

letters = Counter(i=4, s=4, a=0, p=2, b=-98, m=1)
print(sum(letters.values()))

print('------------------')

from collections import Counter

counter1 = Counter(i=4, s=40, a=1, p=20, b=98, z=69)
counter2 = Counter(i=2, s=20, a=6, p=12, m=1, z=69)

# обновляем значения в counter1
counter1.subtract(counter2)       

print(counter1)

print('------------------')

from collections import Counter

counter = Counter(i=4, s=40, a=1, p=20, b=98, z=69)
letters = 'iisssssapppz'

# обновляем значения в counter
counter.subtract(letters)       

print(counter)

print('------------------')

from collections import Counter

counter1 = Counter(i=10, s=40, p=10, m=1)
counter2 = Counter(i=2, s=8, p=10, m=3)

print(counter1 + counter2)
print(counter1 - counter2)
print(counter2 - counter1)

print('------------------')

from collections import Counter

counter1 = Counter(i=10, s=40, p=10, m=1)
counter2 = Counter(i=2, s=8, p=10, m=3)

print(counter1 & counter2)
print(counter1 | counter2)

print('------------------')

from collections import Counter

multiset = Counter([1, 1, 2, 3, 3, 3, 4, 4])

# мультимножество
print(multiset) 
# мультимножество                  
print(*multiset.elements())  
# обычное множество      
print(set(multiset.keys()))       

print('------------------')

from collections import Counter

counter = Counter(a=5, b=-9, c=0)

print(counter)
print(+counter)
print(counter)
print(-counter)
print(counter)

print('------------------')

from collections import Counter

counter1 = Counter('aabc')
counter2 = Counter('abc')

print(counter1 > counter2)

counter1 = Counter('abcde')
counter2 = Counter('abc')

print(counter1 > counter2)

counter1 = Counter('abcde')
counter2 = Counter('abcdf')

print(counter1 > counter2)
print(counter1 < counter2)
print(counter1 >= counter2)
print(counter1 <= counter2)
print(counter1 == counter2)
print(counter1 != counter2)

print('------------------')

from collections import Counter

counter = Counter(green=10, red=25, blue=5)

print(counter.__dict__)

counter.__dict__['min_value'] = lambda: min(counter.values())
counter.max_value = lambda: max(counter.values())

print(counter.min_value())
print(counter.max_value())

print('------------------')