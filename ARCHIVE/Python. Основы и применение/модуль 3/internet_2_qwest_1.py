'''
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.
'''
import requests
import re

url_a, url_b = [input() for i in range(2)]
res = requests.get(url_a)

#url = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
#url = 'http://www.dimonius.ru/?tigerpad'
#url = 'https://raw.githubusercontent.com/pykili/pykili.github.io/master/content/pena0.html'

res = requests.get(url_a)
text = res.text
#print(text)

pattern =r'<a.*?href=["\'](.*?)["\'].*?>'
arr_ahref = re.findall(pattern, text)
#print(arr_ahref)

count = int()
while True:
	count += 1
	for url in arr_ahref:
		#print(url)
		res = requests.get(url)
		text = res.text
		arr = re.findall(pattern, text)
		if url_b in arr:
			count += 1
			break
	if 1 <= count:
		break

if 1 == count:
	print('No')
else:
	print('Yes')