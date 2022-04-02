import requests

#сохраняем ссылку в клaссе str
url = 'http://www.killprog.com/'
#задаем параметры cookies в классе dict
cookies = {'cookies_are' : 'working'}
#отправка сформмрованных cookies на сервер
req = requests.get(url, cookies = cookies)
#вывод ответа от сервера методом text без скобок (покажет код html страницы)
print(req.text)
#использование cookies полученных от сервера
#print(req.cookies['example_cookies_name'])
print(req.cookies)