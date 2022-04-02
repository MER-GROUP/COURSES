# пример списка
print('####################')
languages = ['Python', 'C#', 'Java', 'C++']
print(languages[0])
print(languages[2])

# хранение имя создателя каждого языка программирования
print('####################')
languages = ['Python', 'C#', 'Java', 'C++']
creators = ['Гвидо ван Россум', 'Андерс Хейлсберг', 'Джеймс Гослинг', 'Бьёрн Страуструп']
print('Создателем языка', languages[0], 'является', creators[0])

# хранение имя создателя каждого языка программирования
print('####################')
languages = [('Python', 'Гвидо ван Россум'), 
             ('C#', 'Андерс Хейлсберг'), 
             ('Java', 'Джеймс Гослинг'), 
             ('C++', 'Бьёрн Страуструп')]
print('Создателем языка', languages[2][0], 'является', languages[2][1])

# хранение имя создателя каждого языка программирования
print('####################')
languages = [('Python', 'Гвидо ван Россум'), 
             ('C#', 'Андерс Хейлсберг'), 
             ('Java', 'Джеймс Гослинг'), 
             ('C++', 'Бьёрн Страуструп')]
for item in languages:
    if item[0] == 'C++':
        print('Создателем языка', item[0], 'является', item[1])
        
# Создание словаря
print('####################')
languages = {'Python': 'Гвидо ван Россум', 
             'C#': 'Андерс Хейлсберг', 
             'Java': 'Джеймс Гослинг', 
             'C++': 'Бьёрн Страуструп'}
print(languages)

# Обращение к элементу словаря
print('####################')
languages = {'Python': 'Гвидо ван Россум', 
             'C#': 'Андерс Хейлсберг', 
             'Java': 'Джеймс Гослинг', 
             'C++': 'Бьёрн Страуструп'}
print('Создателем языка C# является', languages['C#'])

# возникновение ошибки KeyError
'''
languages = {'Python': 'Гвидо ван Россум', 
             'C#': 'Андерс Хейлсберг', 
             'Java': 'Джеймс Гослинг', 
             'C++': 'Бьёрн Страуструп'}
print('Создателем языка C# является', languages[1])
'''

# Обращение к элементу словаря через выражение
print('####################')
languages = {'Python': 'Гвидо ван Россум', 
             'C#': 'Андерс Хейлсберг', 
             'Java': 'Джеймс Гослинг', 
             'C++': 'Бьёрн Страуструп'}
print('Создателем языка C# является', languages['C' + '#'])

# Создание словаря с помощью функции dict()
print('####################')
info = dict(name = 'Timur', age = 28, job = 'Teacher')
print(info)

# Создание словаря на основании списков и кортежей
print('####################')
# список кортежей
info_list = [('name', 'Timur'), ('age', 28), ('job', 'Teacher')]
#  создаем словарь на основе списка кортежей
info_dict = dict(info_list)
print(info_dict)

# Создание словаря на основании списков и кортежей
print('####################')
# кортеж списков
info_tuple = (['name', 'Timur'], ['age', 28], ['job', 'Teacher'])
# создаем словарь на основе кортежа списков
info_dict = dict(info_tuple)

# Если необходимо создать словарь, каждому ключу которого соответствует одно и то же значение, можно воспользоваться методом fromkeys()
print('####################')
dict1 = dict.fromkeys(['name', 'age', 'job'], 'Missed information')
print(dict1)

# Если методу fromkeys() не передать второй параметр, то по умолчанию присваивается значение None
print('####################')
dict1 = dict.fromkeys(['name', 'age', 'job'])
print(dict1)

# Пустой словарь
print('####################')
dict1 = {}
dict2 = dict()
print(dict1)
print(dict2)
print(type(dict1))
print(type(dict2))

# Вывод словаря
print('####################')
languages = {'Python': 'Гвидо ван Россум', 
             'C#': 'Андерс Хейлсберг', 
             'Java': 'Джеймс Гослинг'}
info = dict(name = 'Timur', age = 28, job = 'Teacher')
print(languages)
print(info)

# Начиная с версии Python 3.6 словари являются упорядоченными, то есть сохраняют порядок следования ключей в порядке их внесения в словарь.

# Примечание 1. Словари принципиально отличаются от списков по структуре хранения в памяти. Список — последовательная область памяти, то есть все его элементы (указатели на элементы) действительно хранятся в указанном порядке, расположены последовательно. Благодаря этому и можно быстро «прыгнуть» к элементу по его индексу. В словаре же используется специальная структура данных — хеш-таблица. Она позволяет вычислять числовой хеш от ключа и использовать обычные списки, где в качестве индекса элемента берется этот хеш.

# Примечание 2. В рамках одного словаря каждый ключ уникален.

# Примечание 3. Словари удобно использовать для хранения различных сущностей. Например, если нужно работать с информацией о человеке, то можно хранить все необходимые сведения, включающие такие разные сущности как "возраст", "профессия", "название города", "адрес электронной почты" в одном словаре  info и легко обращаться к его элементам по ключам:
print('####################')
info = {'name': 'Timur',
        'age': 28,
        'job': 'Teacher',
        'city': 'Moscow',
        'email': 'timyr-guev@yandex.ru'}
print(info['name'])
print(info['email'])

# Примечание 4. Создать словарь на основании двух списков (кортежей) можно с помощью встроенной функции-упаковщика zip()
print('####################')
keys = ['name', 'age', 'job']
values = ['Timur', 28, 'Teacher']
info = dict(zip(keys, values))
print(info)
# В случае несовпадения длины списков, функция самостоятельно отсечет лишние элементы