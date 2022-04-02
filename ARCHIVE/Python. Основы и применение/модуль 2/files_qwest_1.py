class File:
	def copy_reverse(self):
		with open('file4_test.txt', 'r') as file_read, open('file3_test.txt', 'w') as file_write:
			arr = file_read.readlines()
			arr.reverse()
			file_write.writelines(arr)
		
def main():
	file = File()
	file.copy_reverse()
	
if __name__ == '__main__':
	main()