class File:
	def __init__(self) -> None:
		pass
		
	@staticmethod
	def file_read() -> list:
		with open('школьники.txt') as f:
			return f.readlines()

class School(File):
	def __init__(self):
		self.__a__ = [i for i in range(1, 12)]
		self.__b__ = [[0] * 2 for _ in range(1, 12)]
		self.__my_dict__ = dict(zip(self.__a__, self.__b__))
	
	#@staticmethod
	def __average_stat__(self, my_dict: dict) -> dict:
		tmp = dict()
		for k, v in my_dict.items():
			if 0 == v[0]:
				tmp[k] = '-'
			tmp[k] = v[0] / v[1]
		return tmp
		
	#@staticmethod
	def __out_stat__(self, my_dict: dict) -> None:
		for k, v in my_dict.items():
			print(k, v)
	
	#@staticmethod
	def statistics(self, arr: list) -> None:
		for i in arr:
			words = i.strip().split('\t')
			self.__my_dict__[int(words[0])][0] += int(words[2])
			self.__my_dict__[int(words[0])][1] += 1
		self.__out_stat__(self.__average_stat__(self.__my_dict__))
		
def main() -> None:
	school = School()
	file = school.file_read()
	#print(file)
	school.statistics(file)
	
if __name__ == '__main__':
	main()