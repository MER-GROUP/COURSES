import  csv
# библиотека для работы с табличными данными текстового файла
# csv - текстовый файл для хранения табличных данных, разделитель данных в строке ,(запятая)
# tsv - текстовый файл для хранения табличных данных, разделитель данных в строке \t(табуляция)

# читаем данные из csv файла
# разделитель в строке ,
print('-----разделитель в строке ,-----')
with open('example1.csv', 'r') as file:
	file_csv = csv.reader(file)
	for row in file_csv:
		print(row)
	
# читаем данные из tsv файла
# разделитель в строке \t
print('-----разделитель в строке \\t-----')
with open('example2.tsv', 'r') as file:
	file_csv = csv.reader(file, delimiter='\t')
	for row in file_csv:
		print(row)
		
# записываем данные в csv файл
students =[['Red', 'Alert', 100, 100, 100, 'Excellent score'], ['Alan', 'Wake', 94, 97, 99, 'Good, score']]
with open('example1.csv', 'a') as file:
	# file_csv = csv.writer(file)
	# quoting=csv.QUOTE_ALL - все значения записывается в "..."
	# file_csv = csv.writer(file, quoting=csv.QUOTE_ALL)
	# quoting=csv.QUOTE_NONNUMERIC - все не числовые значения записать в "..."
	file_csv = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
	# for row in students:
	#	 file_csv.writerow(row)
	file_csv.writerows(students)