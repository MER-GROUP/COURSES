print('------------------')

from collections import ChainMap

for_adoption = {'dogs': 15, 'cats': 8, 'pythons': 9}
vet_treatment = {'dogs': 7, 'cats': 2, 'tigers': 3}

pets = ChainMap(for_adoption, vet_treatment)

print(pets)
print(pets.maps)
print(type(pets.maps))

print('------------------')

from collections import ChainMap

for_adoption = {'dogs': 15, 'cats': 8, 'pythons': 9}
vet_treatment = {'dogs': 7, 'cats': 2, 'tigers': 3}

pets = ChainMap(for_adoption, vet_treatment)

pets.maps.reverse()
pets.maps[0]['lions'] = 10
del pets.maps[1]['cats']

print(pets)
print(pets.maps)

print('------------------')

from collections import ChainMap

for_adoption = {'dogs': 15, 'cats': 8, 'pythons': 9}
vet_treatment = {'dogs': 7, 'cats': 2, 'tigers': 3}

pets = ChainMap(for_adoption, vet_treatment)

for animals in pets.maps:
    for key, value in animals.items():
        print(key, '->', value)

print('------------------')

from collections import ChainMap

dad = {'name': 'Timur', 'age': 29}
mom = {'name': 'Rosaly', 'age': 28}

old_family = ChainMap(dad, mom)

son = {'name': 'Soslan', 'age': 0}

new_family = old_family.new_child(son)

print(old_family)
print(new_family)

print('------------------')

from collections import ChainMap

dad = {'name': 'Timur', 'age': 29}
mom = {'name': 'Rosaly', 'age': 28}

old_family = ChainMap(dad, mom)
new_family = old_family.new_child()

print(old_family)
print(new_family)

print('------------------')

from collections import ChainMap

dad = {'name': 'Timur', 'age': 29}
mom = {'name': 'Rosaly', 'age': 28}
son = {'name': 'Soslan', 'age': 0}

family = ChainMap(son, dad, mom)

print(family)
print(family.parents)
print(type(family.parents))

print('------------------')

from collections import ChainMap

empty_chain = ChainMap()
print(empty_chain.maps)

print('------------------')

from collections import ChainMap

chainmap1 = ChainMap({'a': 10, 'b': 20})
chainmap2 = ChainMap({'a': 10, 'b': 20})

print(chainmap1 == chainmap2)

chainmap1 = ChainMap({'a': 10, 'b': 20}, {'a': 1, 'b': 2})
chainmap2 = ChainMap({'a': 10, 'b': 20})

print(chainmap1 == chainmap2)

print('------------------')

from collections import ChainMap

dicts = [{'math': 4, 'physics': 5, 'geometry': 4},
         {'biology': 3, 'chemistry': 3},
         {'literature': 4, 'languages': 4},
         {'history': 3, 'music': 3}]

lessons = ChainMap(*dicts)

print(lessons['literature'])

print('------------------')