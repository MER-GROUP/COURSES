class File:
	def __init__(self) -> None:
		pass
		
	@staticmethod
	def file_read() -> list:
		with open('text3space.txt') as f:
			return f.readlines()
			
	@staticmethod
	def counts(arr: list) -> tuple:
		line = len(arr)
		word, abc = [int()] * 2
		for i in arr:
			tmp = i.strip().split()
			word += len(tmp)
			for j in tmp:
				abc += len(j)
		return line, word, abc
		
def main() -> None:
	arr = File.file_read()
	print(File.counts(arr))
	
if __name__ == '__main__':
	main()