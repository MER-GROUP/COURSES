from random import sample

class Anagram:
	def __init__(self, word):
		print(''.join(sample(word, len(word))))
		
if __name__ == '__main__':
	Anagram(input().strip())