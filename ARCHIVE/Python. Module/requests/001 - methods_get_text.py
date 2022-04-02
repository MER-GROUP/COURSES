import requests

#обращение с запросом к веб страничке методом get()
req = requests.get('http://www.killprog.com/')
#вывод ответа от сервера методом text без скобок (покажет код html страницы)
print(req.text)