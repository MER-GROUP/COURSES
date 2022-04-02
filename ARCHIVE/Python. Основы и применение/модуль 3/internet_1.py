import requests

# делаем get запрос
res = requests.get('https://docs.python.org/3.5/')

# выводим статус код страницы
# 200 - страница существует
# 404 - страница не существует
print(res.status_code)

# посмотреть все хедеры
print(res.headers)

# посмотреть конкретный хедер
print(res.headers['Content-Type'])

# вывести контент страницы
# (бинарные данные)
print(res.content)

# вывести код (текст) страницы
print(res.text)

# копируем изображение (рисунок) с сайта на комп
res_png = requests.get('https://docs.python.org/3.5/_static/py.png')
pic = res_png.content
with open('py.png', 'wb') as file:
	file.write(pic)
	
# просмотр хедера картинки с сайта
print(res_png.headers['Content-Type'])
	
# просмотр бинарного кода картинки с сайта
print(res_png.content)

# передача поисковику Яндекс параметра для поиска
res_yandex = requests.get('https://yandex.ru/search', params={'text': 'Stepic'})
print(res_yandex.status_code)
print(res_yandex.headers['Content-Type'])
print(res_yandex.url)
print(res_yandex.text)

# передача поисковику Яндекс несколько параметров для поиска
res_yandex = requests.get('https://yandex.ru/search', params={'text': 'Stepic', 'test': 'test1', 'name': 'Name With Spaces', 'list': ['test1', 'test2']})
print(res_yandex.status_code)
print(res_yandex.headers['Content-Type'])
print(res_yandex.url)
print(res_yandex.text)