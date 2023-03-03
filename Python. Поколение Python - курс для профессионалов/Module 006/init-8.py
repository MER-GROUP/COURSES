print('------------------')

data = 'mississippi'
counter = 0

for letter in data:
    if letter == 's':
        counter += 1

print(counter)

print('------------------')

data = 'mississippi'
counter = {}

for letter in data:
     if letter not in counter:
         counter[letter] = 0
     counter[letter] += 1

print(counter)

print('------------------')

data = 'mississippi'
counter = {}

for letter in data:
     counter[letter] = counter.get(letter, 0) + 1

print(counter)

print('------------------')

from collections import defaultdict

data = 'mississippi'
counter = defaultdict(int)

for letter in data:
     counter[letter] += 1

print(dict(counter))

print('------------------')

from collections import Counter

# создаем счетчик на основе строки
counter = Counter('mississippi')     
print(counter)

print('------------------')

from collections import Counter

counter1 = Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
counter2 = Counter(i=4, s=4, p=2, m=1)

print(counter1)
print(counter2)

print('------------------')

# from collections import Counter

# counter = Counter.fromkeys('mississippi', 2)

print('------------------')

from collections import Counter

inventory = Counter(apple=5, orange=7, banana=0, tomato=-2, watermelon='N/A')
print(inventory)

print('------------------')

from collections import Counter

letters = Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
print(letters)

letters.update('missouri')
print(letters)

print('------------------')

from collections import Counter

sales = Counter(apple=20, orange=5, banana=10)
monday_sales = Counter(apple=3, orange=12, banana=7)
tuesday_sales = {'apple': 4, 'orange': 5, 'tomato': 6}

print(sales)

sales.update(monday_sales)
print(sales)

sales.update(tuesday_sales)
print(sales)

print('------------------')

from collections import Counter

letters = Counter('mississippi')

# обращение по ключу
print(letters['p'])
print(letters['i'])
print()

# перебор ключей напрямую
for letter in letters:
    print(letter, '->', letters[letter])
print()

# перебор ключей через метод
for letter in letters.keys():
    print(letter, '->', letters[letter])
print()

# перебор значений через метод
for count in letters.values():
    print(count)
print()

# перебор пар (ключ, значение) через метод
for letter, count in letters.items():
    print(letter, '->', count)

print('------------------')

from collections import Counter

counter = Counter(i=4, s=40, a=1, p=20, b=98, z=69)
counter.clear()
print(counter)

print('------------------')

from collections import Counter

counter1 = Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
counter2 = Counter(m=1, s=4, i=4, p=2)
counter3 = Counter('iiiisspm')

print(counter1 == counter2)
print(counter1 == counter3)

print('------------------')

from collections import Counter

counter1 = Counter(i=4)
counter2 = Counter(i=4, s=0)
print(counter1 == counter2)

print('------------------')

from collections import Counter

counter1 = Counter(i=4, s='4')
counter2 = Counter(i=5, s='5')
counter1.update(counter2)
print(counter1)

print('------------------')

from collections import Counter

browsers = Counter(['Firefox', 'Chrome', 'Edge', 'Edge' 'Chrome', 'Firefox', 'Opera', 'Yandex', 'Chrome'])

print(browsers['Firefox'])
print(browsers)

print('------------------')