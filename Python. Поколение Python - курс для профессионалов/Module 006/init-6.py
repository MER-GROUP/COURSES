print('------------------')

from collections import defaultdict

red_1 = defaultdict(int, name='Timur', surname='Guev', hobby='math')
print(red_1)

red_2 = defaultdict(name='Timur', surname='Guev', hobby='math')
print(red_2)

red_3 = defaultdict(int, {'name': 'Timur', 'surname': 'Guev', 'hobby': 'math'})
print(red_3)

red_4 = defaultdict()
print(red_4)

red_5 = defaultdict(list)
print(red_5)

red_6 = defaultdict(int, [('name', 'Timur'), ('surname', 'Guev'), ('hobby', 'math')])
print(red_6)

# red_7 = defaultdict({'name': 'Timur', 'surname': 'Guev', 'hobby': 'math'})
# print(red_7)

red_8 = defaultdict(None)
print(red_8)

red_9 = defaultdict.fromkeys(['name', 'surname', 'hobby'], None)
print(red_9)

print('------------------')