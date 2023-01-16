print('------------------')

# Приведенный ниже код:
import json

data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}
# сериализуем словарь data в json строку
json_data = json.dumps(data)            

print(type(json_data))
print(json_data)

print('------------------')

import json

data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}

with open('contries.json', 'w') as file:
    json.dump(data, file)

print('------------------')

# Приведенный ниже код:
import json

data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}

json_data1 = json.dumps(data, indent=2)
json_data2 = json.dumps(data, indent=10)

print(json_data1)
print(json_data2)

print('------------------')

import json

data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}

json_data = json.dumps(data, indent='++++')

print(json_data)

print('------------------')

import json

data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}

json_data1 = json.dumps(data, indent=3)
json_data2 = json.dumps(data, indent=3, sort_keys=True)

print(json_data1)
print(json_data2)

print('------------------')

import json

data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}

json_data = json.dumps(data, indent=3, separators=(';', ' = '))

print(json_data)

print('------------------')

import json

json_data = '{"name": "Russia", "phone_code": 7, "capital": "Moscow", "currency": "RUB"}'

data = json.loads(json_data)
print(type(data))
print(data)

print('------------------')

# import json

# # строка
# json_data = '{"name":, "Russia", "phone_code": 7, "capital": "Moscow", "currency": "RUB"}'  

# data = json.loads(json_data)
# print(type(data))
# print(data)

print('------------------')

import json

with open('data.json') as file:
    # передаем файловый объект
    data = json.load(file)                
    for key, value in data.items():
        if type(value) == list:
            print(f'{key}: {", ".join(value)}')
        else:
            print(f'{key}: {value}')

print('------------------')

import json

json_data = '''
{
   "name": "Russia",
   "phone_code": 7,
   "latitude": 60.0,
   "capital": "Moscow",
   "timezones": ["Anadyr", "Barnaul", "Moscow", "Kirov"],
   "translations": {
      "nl": "Rusland",
      "hr": "Rusija",
      "de": "Russland",
      "es": "Rusia",
      "fr": "Russie",
      "it": "Russia"
   }
}'''

data = json.loads(json_data)

print(type(data['name']))
print(type(data['phone_code']))
print(type(data['latitude']))
print(type(data['timezones']))
print(type(data['translations']))

print('------------------')

import json

data = {
        'name': 'Russia', 
        'phone_code': 7,
        'latitude': 60.0,
        'capital': 'Moscow',
        'timezones': ('Anadyr', 'Barnaul', 'Moscow', 'Kirov')
       }

# преобразуем dict в json
json_data = json.dumps(data)   
# преобразуем json в dict     
new_data = json.loads(json_data)    

print(data == new_data)
print(data)
print(new_data)

print('------------------')

# import json

# data = {
#         'beegeek': 2018,
#         ('Timur', 'Guev'): 29,
#         ('Arthur', 'Kharisov'): 20,
#         'stepik': 2013
#        }

# # преобразуем dict в json
# json_data = json.dumps(data)        

# print(json_data)

print('------------------')

import json

data = {
        'beegeek': 2018,
        ('Timur', 'Guev'): 29,
        ('Arthur', 'Kharisov'): 20,
        'stepik': 2013
       }
# преобразуем dict в json
json_data = json.dumps(data, skipkeys=True)        

print(json_data)

print('------------------')

import json

data = {1: 'Timur', False: 'Arthur', None: 'Ruslan'}
json_data = json.dumps(data)

print(json_data)

print('------------------')

import json

data = {'firstName': 'Тимур', 'lastName': 'Гуев'}
s = json.dumps(data)
print(s)

print('------------------')

import json

data = {'firstName': 'Тимур', 'lastName': 'Гуев'}
s = json.dumps(data)
print(s)
result = json.loads(s)
print(result)

print('------------------')

import json

data = {'firstName': 'Тимур', 'lastName': 'Гуев'}
s = json.dumps(data, ensure_ascii=False)
print(s)
result = json.loads(s)
print(result)

print('------------------')