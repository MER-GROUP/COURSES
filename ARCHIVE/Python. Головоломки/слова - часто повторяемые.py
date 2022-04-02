class Words:
	def __init__(self):
		pass
	
	@staticmethod	
	def file_read():
		arr = list()
		with open('words.txt') as f:
			for line in f:
				arr += line.lower().strip().split()
		return arr
		
	@staticmethod
	def word_max_count(arr):
		word_set = set(arr)
		word_dict = {word : arr.count(word) for word in word_set}
		word_list_sort = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
		word_dict = dict(word_list_sort)
		m = max(word_dict.values())
		res = dict()
		for k, v in word_dict.items():
			if m > v:
				break
			res[k] = v
		return res
		
	@staticmethod
	def file_write(s):
		with open('words_ans.txt', 'w') as f:
			f.write(s)
		
def main():
	print('hello')
	arr = Words.file_read()
	print(arr)
	print('--------------')
	word = Words.word_max_count(arr)
	print(word)
	print(min(word.keys()), word.get(min(word.keys())))
	s = str(min(word.keys())) + ' ' + str(word.get(min(word.keys())))
	Words.file_write(s)
	
if __name__ == '__main__':
	main()