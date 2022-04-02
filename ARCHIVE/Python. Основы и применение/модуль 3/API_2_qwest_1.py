'''
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com 

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true

Пример входного файла:
31
999
1024
502

﻿Пример выходного файла:
Interesting
Boring
Interesting
Boring
'''
# пример работы API с сайта numbersapi.com
import requests

# читаем файл
arr = None
with open('API3.txt', 'r') as file:
	arr = [int(i.strip()) for i in file.readlines()]
#print(arr)

# делаем запросы и выволим интересное число или нет
for i in range(len(arr)):
	#url ='http://numbersapi.com/31/math?json=true'
	url ='http://numbersapi.com/'+str(arr[i])+'/math?'
	params = {'json': 'true'}
	res = requests.get(url, params=params)
	#print(res.text)
	#print(res.url)
	data_json = res.json()
	#print(data_json['number'])
	if data_json['found']:
		print('Interesting')
	else:
		print('Boring')