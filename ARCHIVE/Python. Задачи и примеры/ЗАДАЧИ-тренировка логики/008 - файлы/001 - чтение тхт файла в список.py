class Red:
	def __init__(self):
		pass
		
	@staticmethod
	def file_read():
		file = open('text.txt')
		return file
		
	@staticmethod
	def file_print(file):
		for i in file:
			print(i)
			
	@staticmethod
	def file_copy_to_arr(file):
		arr = list()
		for i in file:
			print(i)
			arr.append(i)
		return arr
		
	@staticmethod
	def arr_clear(arr):
		for i in range(len(arr)):
			if '\n' == arr[i][-1]:
				arr[i] = arr[i][ : -1]
				
	@staticmethod
	def arr_clear_strip(arr):
		for i in range(len(arr)):
			arr[i] = arr[i].strip()
		
def main():
	file = Red.file_read()
	Red.file_print(file)
	print('--------------------------')
	file = Red.file_read()
	print(file)
	print('--------------------------')
	arr = Red.file_copy_to_arr(file)
	print(arr)
	print('--------------------------')
	#Red.arr_clear(arr)
	Red.arr_clear_strip(arr)
	print(arr)
	
if __name__ == '__main__':
	main()