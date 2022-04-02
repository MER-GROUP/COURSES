'''
В этой задаче вам необходимо воспользоваться API сайта artsy.net

API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.

В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).

Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника и годе рождения.
Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год
 рождения, выведите их имена в лексикографическом порядке.

Работа с API Artsy

Полностью открытое и свободное API предоставляют совсем немногие проекты. В большинстве случаев, 
для получения доступа к API необходимо зарегистрироваться в проекте, создать свое приложение, 
и получить уникальный ключ (или токен), и в дальнейшем все запросы к API осуществляются при помощи этого ключа.

Чтобы начать работу с API проекта Artsy, вам необходимо пройти на стартовую страницу документации 
к API https://developers.artsy.net/start и выполнить необходимые шаги, а именно зарегистрироваться, 
создать приложение, и получить пару идентификаторов Client Id и Client Secret. Не публикуйте эти идентификаторы.

После этого необходимо получить токен доступа к API. На стартовой странице документации есть примеры того, 
как можно выполнить запрос и как выглядит ответ сервера. Мы приведем пример запроса на Python.

import requests
import json

client_id = '...'
client_secret = '...'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]
 
Теперь все готово для получения информации о художниках. На стартовой странице документации есть пример того, 
как осуществляется запрос и как выглядит ответ сервера. Пример запроса на Python.
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
r = requests.get("https://api.artsy.net/api/artists/4d8b92b34eb68a1b2c0003f4", headers=headers)

# разбираем ответ сервера
j = json.loads(r.text)


Примечание:
В качестве имени художника используется параметр sortable_name в кодировке UTF-8.

Пример входных данных:
4d8b92b34eb68a1b2c0003f4
537def3c139b21353f0006a6
4e2ed576477cc70001006f99

Пример выходных данных:
Abbott Mary
Warhol Andy
Abbas Hamra

Примечание для пользователей Windows
При открытии файла для записи на Windows по умолчанию используется кодировка CP1251, 
в то время как для записи имен на сайте используется кодировка UTF-8, что может привести к 
ошибке при попытке записать в файл имя с необычными символами. Вы можете использовать print, 
или аргумент encoding функции open.
'''

import requests
import json
#import operator

# создаем заголовок, содержащий наш токен
token = 'eyJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsInN1YmplY3RfYXBwbGljYXRpb24iOiI2MTYwNTFkOGQxMjY1MDAwMGQ0MDdkYWEiLCJleHAiOjE2MzQzMDc2ODQsImlhdCI6MTYzMzcwMjg4NCwiYXVkIjoiNjE2MDUxZDhkMTI2NTAwMDBkNDA3ZGFhIiwiaXNzIjoiR3Jhdml0eSIsImp0aSI6IjYxNjA1M2U0MWI4N2FlMDAwYjAxMmFjZCJ9.kZjXbu_6BeXXqIJc6LobZV9vMOCSsQL5wluW_WfYx40'
headers = {'X-Xapp-Token' : token}

# ввод данных
id_art = None
#id_art = ['53ee751c6361721944780200', '4d8b92b34eb68a1b2c0003f4', '537def3c139b21353f0006a6', '4e2ed576477cc70001006f99']
with open('arts.txt', 'r', encoding='utf-8') as file:
    id_art = file.readlines()
id_art = [i.strip() for i in id_art]
#print(id_art)

# словарь хранения имении художника и даты рождения
my_dict = dict()

for i in id_art:
    # url
    url = f'https://api.artsy.net/api/artists/{i}'

    # инициируем запрос с заголовком
    r = requests.get(url, headers=headers)
    #r.encoding = 'utf-8'
    #print(r)

    # разбираем ответ сервера
    j = json.loads(r.text)
    #print(j)
    '''
    for k, v in j.items():
        print(k, '=', v)
        print('---------')
    '''

    # заполняем в словарь данные
    my_dict[j['sortable_name']] = int(j['birthday'])

# вывод словаря в консоль    
#print(my_dict)

# сортировка по имени и потом году рождения (двухэтапная сортировка)
arr = sorted(list(my_dict.items()), key=lambda x: x[0])
arr = sorted(arr, key=lambda x: x[1])
#arr = sorted(list(my_dict.items()), key=lambda x: (x[1], x[0]))

# сортировка по году рождения потом по имени (двухэтапная сортировка)
#arr = sorted(list(my_dict.items()), key=operator.itemgetter(1,0))

# вывод инфы
#print(arr, sep='\n')
for i in range(len(arr)):
    print(arr[i][0])