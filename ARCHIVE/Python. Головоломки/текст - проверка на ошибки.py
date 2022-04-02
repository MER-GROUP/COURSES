class Text:
	def __init__(self):
		pass
		
	@staticmethod
	def enter_words(words: int) -> list:
		return [input().lower() for _ in range(words)]
		
	@staticmethod
	def enter_lines(lines: int) -> list:
		arr = list()
		for _ in range(lines):
			arr += input().strip().lower().split()
		return arr
		
def main() -> None:
	words = int(input())
	words_set = set(Text.enter_words(words))
	#print(words_set)
	lines = int(input())
	lines_set = set(Text.enter_lines(lines))
	#print(lines_set)
	print(*(lines_set - words_set), sep='\n')
	
if __name__ == '__main__':
	main()