# шаблоны и форматирование (использование format)
capital = 'London is the capital of Great Britain'
template = '{} is the capital of {}'
template2 = '{1} is the capital of {0}'
print(capital)
print(template.format('Minsk', 'Belarussia'))
print(template2.format('Roma', 'Italy'))
#print(template.format.__doc__)

template3 = '{capital} is the capital of {country}'
print(template3.format(capital='Paris', country='France'))
print(template3.format(country='France', capital='Paris'))

import requests
template4 = 'Responce from {0.url} with code {0.status_code}'
res = requests.get('https://docs.python.org/3.5/')
print(template4.format(res))
res = requests.get('https://docs.python.org/3.5/random')
print(template4.format(res))

from random import random
x = random()
print(x)
print('{:.3}'.format(x))