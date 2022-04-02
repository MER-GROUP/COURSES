class Student:
	def __init__(self):
		pass
		
	@staticmethod
	def tire():
		print('------------------------------')
		
	@staticmethod
	def file_read():
		arr = list()
		words_dict = dict()
		with open('students.txt') as f:
			arr = f.readlines()
		for row in arr:
			word = row.strip().split(';')
			words_dict[word[0]] = [int(i) for i in word[1 : ]]
		return words_dict
		
	@staticmethod
	def students_average(students):
		average = dict()
		for k, v in students.items():
			average[k] = str(sum(v) / len(v)) + '\n'
		return average
		
	@staticmethod
	def students_all_avarage(students):
		arr = [0] * 3
		for v in students.values():
			for i in range(len(arr)):
				arr[i] += v[i]
		for i in range(len(arr)):
			arr[i] = str(arr[i] / len(students))
		return arr
		
	@staticmethod
	def file_write(average, all):
		with open('students_ans.txt', 'w') as f:
			f.writelines(average.values())
			f.writelines(all)
		
def main():
	print('RED ALERT')
	students = Student.file_read()
	print(students)
	average = Student.students_average(students)
	Student.tire()
	print(average)
	Student.tire()
	average_all = Student.students_all_avarage(students)
	print(average_all)
	Student.tire()
	average_all = ' '.join(average_all)
	print(average_all)
	Student.file_write(average, average_all)
	
if __name__ == '__main__':
	main()