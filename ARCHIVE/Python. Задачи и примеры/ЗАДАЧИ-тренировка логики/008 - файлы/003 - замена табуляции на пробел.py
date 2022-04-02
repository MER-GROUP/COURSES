class Red:
	def __init__(self):
		pass
		
	@staticmethod	
	def file_read():
		file = str()
		with open('text3.txt') as text:
			file = text.read()
		return file
		
	@staticmethod
	def file_tab_to_space(s):
		arr = s.split('\t')
		return '    '.join(arr)
		
	@staticmethod
	def file_write(file):
		with open('text3space.txt', 'w') as text:
			text.write(file)
	
def main():
	file = Red.file_read()
	print(repr(file))
	file_convert = Red.file_tab_to_space(file)
	print(repr(file_convert))
	Red.file_write(file_convert)
	
if __name__ == '__main__':
	main()