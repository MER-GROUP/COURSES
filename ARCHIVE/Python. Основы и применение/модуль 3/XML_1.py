# импортируем библиотеку для работы с xml файлами
from xml.etree import ElementTree

# парсим весь xml файл
tree = ElementTree.parse('studentsList.xml')

# получаем корень xml файла
root = tree.getroot()
print(root)

# получаем корневой тэг
print(root.tag)

# получаем атрибут у корневого тэга
print(root.attrib)

# сделать парсинг из строковых данных
#root_too = ElementTree.fromstring('str_xml_data')

# перебираем детей из корня
for child in root:
	print(child.tag, child.attrib)
	
# обращение через индексацию
print(root[0][0])

# получение текста расположенного между тэгами
print(root[0][0].text)

# итерируем нужный тэг в xml файле
# и в нужном тэге переберем всех детей и вычислим сумму чисел которые хранят дети
for element in root.iter('scores'):
	print(element)
	sm = int()
	for child in element:
		sm += float(child.text)
		print(child.tag, child.text)
	print(sm)
	
# перебор элементов-детей корня
for element in root.findall('student'):
	print(element)
	
# записать дерево в xml формате
# записывает в xml файл объек который уже пропарсен (копия файла 'studentsList.xml)
tree.write('example.xml')

# модифицируем первого студента
greg = root[0]
print(greg.tag)
module1 = next(greg.iter('module1'))
print(module1)
print(module1.text)
module1.text = str(int(module1.text) + 30)
print(module1.text)
tree.write('example.xml')

# модифицируем тэг certificate
certificate = greg[2]
print(certificate)
print(certificate.text)
# добавляем атрибут type в тэг certificate
certificate.set('type', 'with distinction')
tree.write('example.xml')

# создание нового элемента
description = ElementTree.Element('description')
description.text = 'You are the best !'
greg.append(description)
tree.write('example.xml')

# удаление любого элемента
description = greg.find('description')
greg.remove(description)
tree.write('example.xml')

# создание нового дерева (элементов)
my_root = ElementTree.Element('student')
# создание ребенка
firstName = ElementTree.SubElement(my_root, 'firstName')
firstName.text = 'Max'
# создание ребенка
lastName = ElementTree.SubElement(my_root, 'lastName')
lastName.text = 'Ramanenka'
# создание детей
scores = ElementTree.SubElement(my_root, 'scores')
module4 = ElementTree.SubElement(scores, 'module4')
module4.text = '100'
module5 = ElementTree.SubElement(scores, 'module5')
module5.text = '90'
module6 = ElementTree.SubElement(scores, 'module6')
module6.text = '80'
# создание нового дерева (корня)
my_tree = ElementTree.ElementTree(my_root)
# запись всего созданного в xml файл
my_tree.write('example2.xml')