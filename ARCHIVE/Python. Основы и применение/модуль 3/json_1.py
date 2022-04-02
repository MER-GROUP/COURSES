# библиотека для работы с форматом файла json, данные хранятся в виде словаря (ключ = значение)
import json

students1 = {
			"first name": "Greg",
			"last name": "Dean",
			"certificate": True,
			"scores": [70, 80, 90],
			"description": "Good job, Greg"
}

students2 = {
			"first name": "Wirt",
			"last name": "Wood",
			"certificate": True,
			"scores": [70, 80.2, 80],
			"description": "Nicely Done"
}

# dumps - возвращает данные в формате json в консоль
# indent - количество отступов
# sort_keys - сортировка ключей словаря
data = [students1, students2]
data_json = json.dumps(data, indent=4, sort_keys=True)
print(data_json)
print(type(data_json))

# записываем в файл данные в формате json
with open('example4.json', 'w') as file:
	json.dump(data, file, indent=4, sort_keys=True)
	
# получение объекта из json файла
# в списке открываем первый словарь ищем ключ scores и суммируем все значения ключа
data_again = json.loads(data_json)
print(type(data_again))
print(sum(data_again[0]["scores"]))

# считываем из файла
with open('example4.json', 'r') as file:
	data_again_read = json.load(file)
	print(sum(data_again_read[1]["scores"]))