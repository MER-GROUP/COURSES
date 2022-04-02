# пример работы с API сайта openweathermap.org
import requests
import json
# ввод города
city = input('City? ')
# составляем запрос
url_api = 'https://api.openweathermap.org/data/2.5/weather'
params = {'q': city, 'units': 'metric', 'appid': '909bc44160ec78019e5bd0c0596f54a5'}
# делаем запрос
res = requests.get(url_api, params=params)
print('----------------------------')
# получаем статус код и хидер
print(res.status_code)
print(res.headers['Content-Type'])
print('----------------------------')
# получаем запрос в виде текста
text = res.text
print(text)
print(type(text))
print('----------------------------')
# получаем запрос в виде словаря
arr = json.loads(text)
print(arr)
print(type(arr))
print('----------------------------')
# получаем запрос в виде словаря
#data_json = json.loads(res.text)
data_json = res.json()
print(data_json)
print(type(data_json))
print('----------------------------')
# выводим температуру в кельвинах
print(data_json['main']['temp'])
# создаем шаблон для вывода
template = 'Current temperature in {} is {}'
# выводим город и температуру
print(template.format(data_json['name'], data_json['main']['temp']))