'''
Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов, которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида
<a href="../some_path/index.html">.

Сайты следует выводить в алфавитном порядке.

Пример HTML файла:

<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">

Пример ответа:

mail.ru
neerc.ifmo.ru
stepic.org
www.ya.ru
ya.ru
'''

import requests
import re

'''
text = ['<a href="http://stepic.org/courses">', "<a href='https://stepic.org'>", "<a href='http://neerc.ifmo.ru:1345'>", 
'<a href="ftp://mail.ru/distib" >', 
'<a href="ya.ru">', 
'<a href="www.ya.ru">', 
'<a href="../skip_relative_links">',
'<a href="www.rambler.ru.com.by">',
'<a href="http://www.cnews.ru/cgi-bin/redirect.cgi?http://corp.cnews.ru">']
'''

#url = 'https://pastebin.com/raw/hfMThaGb'
#url = 'https://pastebin.com/raw/7543p0ns'
url = input()

#pattern = r'<a.*?href=["\'](.*?)["\'].*?>'
#pattern = r'<a.*?href=[\"\']((http[s]*|ftp)*([\:]*[\/]*)(.*?))[\"\'].*?>'
#pattern = r'((http[s]?|ftp):\/\/)?(([\da-z\.-]+)\.([a-z\.]{2,6}))([\/\w \.-]*)*\/?'
pattern = r'<a.*?href=[\"\']((http[s]*|ftp)*([\:]*[\/]*)(([\da-z\.-]+)\.([a-z\.]{2,6}))).*?>'

res = requests.get(url)
text = res.text

#arr = re.findall(pattern, ''.join(text))
'''
arr = re.findall(pattern, text)
print(*arr, sep='\n')
print(len(arr))
'''

'''
print(*arr, sep='\n')
print('------------------')
print(arr[0][2])
print(type(arr[0]))
'''

arr = re.findall(pattern, text)
arr_domain = [arr[i][3] for i in range(len(arr))]
arr_domain = sorted(list(set(arr_domain)))
print(*arr_domain, sep='\n')