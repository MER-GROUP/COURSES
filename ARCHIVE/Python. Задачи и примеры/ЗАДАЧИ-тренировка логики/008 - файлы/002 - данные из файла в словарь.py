class Red:
	def __init__(self):
		pass
		
	@staticmethod
	def file_read():
		return open('text2.txt')
		
	@staticmethod
	def my_dict(arr):
		tmp = list()
		my_d = dict()
		for i in arr:
			tmp = i.strip().split()
			tmp[1] = float(tmp[1])
			tmp[2] = int(tmp[2])
			my_d[tmp[0]] = tmp[1 : ]
		return my_d
			
	@staticmethod
	def dict_out(my_dict):
		for k, v in my_dict.items():
			print(k, '=', v)
		
def main():
	file = Red.file_read()
	print(file)
	arr = file.readlines()
	print(arr)
	my_dict = Red.my_dict(arr)
	Red.dict_out(my_dict)
	print(my_dict)
	
if __name__ == '__main__':
	main()