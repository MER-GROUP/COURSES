# lxml библиотека для анализа xml и html тегов
#import lxml
from lxml import etree
import requests

#создаем запрос
res = requests.get('https://docs.python.org/3/')
print(res.status_code)
print(res.headers['Content-Type'])

# создаем парсер html тегов
parser = etree.HTMLParser()
# создаем корень документа
root = etree.fromstring(res.text, parser)
# выводим корень
print(root)

# выведем все таги <a>
for element in root.iter('a'):
	print(element, element.attrib)