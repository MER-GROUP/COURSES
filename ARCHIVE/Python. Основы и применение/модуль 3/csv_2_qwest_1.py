import csv
import re

# ищем виды преступлений
def whois(arr):
	my_dict = dict()
	for i in arr:
		try:
			if my_dict[i[5]] is not None:
				my_dict[i[5]] += 1
			else:
				raise KeyError
		except KeyError:
			my_dict[i[5]] = 1
	return my_dict
	
# сортируем от макс до мин
def sort_dict(my_dict):
	arr = list(my_dict.items())
	arr.sort(key=lambda x: int(x[1]), reverse=True)
	#print(*arr, sep='\n')
	arr_dict = dict(zip([arr[i][0] for i in range(len(arr))], [arr[i][1] for i in range(len(arr))]))
	for k, v in arr_dict.items():
		print(k, '=', v)

if __name__ == '__main__':
	arr = list()
	pattern = r'\d{2}\/\d{2}\/2015'
	
	with open('Crimes.csv', 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			#print(type(row))
			if re.search(pattern, ' '.join(row)):
				arr.append(row)
	'''	
	for row in arr:
		print(row)
	'''
	my_dict = whois(arr)
	'''
	for k, v in my_dict.items():
		print(k, '=', v)
	'''
	sort_dict(my_dict)