with open('file_test.txt', 'r') as file1, open('file3_test.txt', 'w') as file2:
	for line in file1:
		tmp = line.rstrip()
		print(tmp)
		file2.write(line)