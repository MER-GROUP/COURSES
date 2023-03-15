print('------------------')

from collections import ChainMap

# создаем пустой ChainMap объект
empty_chain_map = ChainMap()                      
print(empty_chain_map)

numbers = {'one': 1, 'two': 2}
letters = {'a': 'A', 'b': 'B'}

# создаем ChainMap объект на основе словарей numbers и letters
chain_map = ChainMap(numbers, letters)            
print(chain_map)

print('------------------')

from collections import ChainMap

chain_map1 = ChainMap.fromkeys(['one', 'two', 'three'])
chain_map2 = ChainMap.fromkeys(['one', 'two', 'three'], -1)

print(chain_map1)
print(chain_map2)

print('------------------')

from collections import ChainMap

numbers = {'one': 1, 'two': 2}
letters = {'a': 'A', 'b': 'B'}

alpha_num = ChainMap(numbers, letters)


print(alpha_num['one'])
print(alpha_num['b'])
print(alpha_num.get('a'))
print(alpha_num.get('c'))
print(alpha_num.get('d', False))

print('------------------')

from collections import ChainMap

for_adoption = {'dogs': 15, 'cats': 8, 'pythons': 9}
vet_treatment = {'dogs': 7, 'cats': 2, 'tigers': 3}

pets = ChainMap(for_adoption, vet_treatment)

print(pets['dogs'])
print(pets['cats'])

print(pets['pythons'])
print(pets['tigers'])

print('------------------')

from collections import ChainMap

numbers = {'one': 1, 'two': 2}
letters = {'a': 'A', 'b': 'B'}

alpha_num = ChainMap(numbers, letters)

for key in alpha_num:
    print(key, '->', alpha_num[key])

print('------------------')

from collections import ChainMap

for_adoption = {'dogs': 15, 'cats': 8, 'pythons': 9}
vet_treatment = {'dogs': 7, 'cats': 2, 'tigers': 3}

pets = ChainMap(for_adoption, vet_treatment)

for key in pets:
    print(key, '->', pets[key])

print('------------------')

from collections import ChainMap

for_adoption = {'dogs': 15, 'cats': 8, 'pythons': 9}
vet_treatment = {'dogs': 7, 'cats': 2, 'tigers': 3}

pets = ChainMap(for_adoption, vet_treatment)

for key in pets.keys():
    print(key, '->', pets[key])

print()

for value in pets.values():
    print(value)

print()

for key, value in pets.items():
    print(key, '->', value)

print('------------------')

from collections import ChainMap

numbers = {'one': 1, 'two': 2}
letters = {'a': 'A', 'b': 'B'}

alpha_num = ChainMap(numbers, letters)
print(alpha_num)

alpha_num['c'] = 'C'
print(alpha_num)

alpha_num['b'] = 'b'
print(alpha_num)

alpha_num.pop('two')
print(alpha_num)

del alpha_num['c']
print(alpha_num)

alpha_num.clear()
print(alpha_num)

print('------------------')

from collections import ChainMap

numbers = {'one': 1, 'two': 2}
letters = {'a': 'A', 'b': 'B'}

alpha_num = ChainMap({}, numbers, letters)
print(alpha_num)

alpha_num['colon'] = ':'
alpha_num['comma'] = ','
alpha_num['period'] = '.'
print(alpha_num)

print('------------------')

from collections import ChainMap

for_adoption = {'dogs': 15, 'cats': 8, 'pythons': 9}
vet_treatment = {'hamsters': 2, 'tigers': 3}

pets = ChainMap(for_adoption, vet_treatment)
print(pets)

print('------------------')

for_adoption = {'dogs': 15, 'cats': 8, 'pythons': 9}
vet_treatment = {'hamsters': 2, 'tigers': 3}

pets = {}
pets.update(for_adoption)
pets.update(vet_treatment)
print(pets)

print('------------------')

for_adoption = {'dogs': 15, 'cats': 8, 'pythons': 9}
vet_treatment = {'dogs': 7, 'cats': 2, 'tigers': 3}

pets = {}
pets.update(for_adoption)
pets.update(vet_treatment)

print(pets)

print('------------------')

from collections import defaultdict, OrderedDict, Counter, ChainMap

numbers = OrderedDict(one=1, two=2)
letters = defaultdict(str, {'a': 'A', 'b': 'B'})
counter = Counter('aabbbcccc')

chain_map = ChainMap(numbers, letters, counter)

print(chain_map)

print('------------------')

from collections import ChainMap

for_adoption = {'dogs': 15, 'cats': 8, 'pythons': 9}
vet_treatment = {'dogs': 7, 'cats': 2, 'tigers': 3}

pets = ChainMap(for_adoption, vet_treatment)

print(len(pets))

print('------------------')

from collections import ChainMap

for_adoption = {'dogs': 15, 'cats': 8, 'pythons': 9}
vet_treatment = {'dogs': 7, 'cats': 2, 'tigers': 3}

pets = ChainMap(for_adoption, vet_treatment)
print(pets)

for_adoption['dogs'] = 10000
for_adoption['lions'] = 9

print(pets)

print('------------------')