# Frozenset - Замороженное множество
# Кортеж (тип tuple) – неизменяемая версия списка (тип list), а замороженное множество (тип frozenset) – неизменяемая версия обычного множества (тип set)
# Для создания замороженного множества используется встроенная функция frozenset()

# на основе множества
print('####################')
myset1 = frozenset({1, 2, 3})
# на основе списка
myset2 = frozenset([1, 1, 2, 3, 4, 4, 4, 5, 6, 6])
# на основе строки
myset3 = frozenset('aabcccddee')
print(myset1)
print(myset2)
print(myset3)

# Операции над замороженными множествами
print('####################')
myset1 = frozenset('hello')
myset2 = frozenset('world')
print(myset1 | myset2)
print(myset1 & myset2)
print(myset1 ^ myset2)

# Примечание 1. Будучи изменяемыми, обычные множества не могут быть элементами других множеств. Замороженные множества являются неизменяемыми, а значит могут быть элементами других множеств.
print('####################')
sentence = 'The cat in the hat had two sidekicks, thing one and thing two.'
words = sentence.lower().replace('.', '').replace(',', '').split()
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = {frozenset({letter for letter in word if letter not in vowels}) for word in words}
print(*consonants, sep='\n')

# Примечание 2. Методы изменяющие множество отсутствуют у замороженных множеств:
'''
add()
remove()
discard()
pop()
clear()
update()
intersection_update()
difference_update()
symmetric_difference_update()
'''

# Примечание 3. Мы можем сравнивать простые (тип set) и замороженные множества (тип frozenset).
print('####################')
myset1 = set('qwerty')
myset2 = frozenset('qwerty')
print(myset1 == myset2)