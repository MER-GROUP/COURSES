print('------------------')

class NegativeAgeError(Exception):
    pass

try:
    print('Введите свой возраст')
    age = int(input())
    if age < 0:
        raise NegativeAgeError('Возраст не может быть отрицательным')
    print('Ваш возраст равен', age)
except ValueError:
    print('Возраст должен быть числом')
except NegativeAgeError as e:
    print(e)

print('------------------')

data = {'Timur': 29, 'Ivan': 54}

if 'Anri' in data:
    data['Anri'] += 1
else:
    print('Ключ Anri отсутсвует в словаре.')

print('------------------')

data = {'Timur': 29, 'Ivan': 54}

try:
    data['Anri'] += 1
except KeyError:
    print('Ключ Anri отсутсвует в словаре.')

print('------------------')