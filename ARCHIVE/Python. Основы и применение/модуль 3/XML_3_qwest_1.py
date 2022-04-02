from xml.etree import ElementTree

# заполняем словарь ключами
def color(root):
	my_dict = dict()
	for child in root.iter('cube'):
		my_dict[child.attrib['color']] = 0
	return my_dict
	
# создаем словарь и получаем детей и их значения
def color_count(element, my_dict, level):
	for child in list(element):
		if 0 == len(list(element)):
			break
		else:
			if child.attrib['color'] in my_dict:
				my_dict[child.attrib['color']] += level
			else:
				my_dict[child.attrib['color']] = level
			color_count(child, my_dict, level + 1)
	return my_dict

xml_data = input()
'''
xml_data = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'
xml_data = '<cube color="blue"><cube color="red"><cube color="green"><cube color="green"><cube color="green"><cube color="blue"></cube><cube color="green"></cube><cube color="red"></cube></cube></cube></cube></cube><cube color="red"><cube color="blue"></cube></cube></cube>'
'''
'''
red = 10(2, 6, 2)
green = 18(3, 4, 5, 6)
blue = 10(1, 6, 3)
'''
# создаем парсинг из str данных
root = ElementTree.fromstring(xml_data)
#print(root, root.attrib)
#print(type(root))
#print('----------------------')

# заполняем словарь ключами
my_dict = color(root)
#print(my_dict)
#print('----------------------')

'''
# пример взятия детей только из нижнего уровня
# root.getchildren() - выдает предупреждение (мол её не будет в следующих версиях)
def my_kids_warning(element):
	for child in root.getchildren():
		print(child.attrib)
my_kids_warning(root)
'''

'''
# пример взятия детей только из нижнего уровня
print('----------------------')
def my_kids(element):
    for child in list(element):
        print(child.attrib)
my_kids(root)
'''

# создаем словарь и получаем детей и их значения
my_dict[root.attrib['color']] = 1
my_dict = color_count(root, my_dict, 2)
#print(my_dict)

# выводи красное, зеленое, синее
print(my_dict['red'], my_dict['green'], my_dict['blue'])