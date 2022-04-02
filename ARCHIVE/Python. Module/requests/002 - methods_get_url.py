import requests

#сохраняем ссылку в клaссе str
url = 'http://www.killprog.com/'
#задаем параметры ссылки в классе dict
pair ={'key1' : 'value1', 'key2' : 'value2'}
#передача параметров в запрос метрдом get()
req = requests.get(url, pair)
#получение ссылки с параметрами методом url
print(req.url)