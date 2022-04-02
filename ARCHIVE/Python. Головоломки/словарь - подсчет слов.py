class Words:
	def __init__(self):
		pass
		
	@staticmethod
	def enter():
		return input().lower().split()
		
	@staticmethod
	def words(arr):
		my_set = set(arr)
		my_dict = dict()
		for i in my_set:
			my_dict[i] = arr.count(i)
		return my_dict
		
	@staticmethod
	def out(my_dict):
		for k, v in my_dict.items():
			print(k, v)
	
def main():
	arr = Words.enter()
	my_dict = Words.words(arr)
	Words.out(my_dict)
	
if __name__ == '__main__':
	main()