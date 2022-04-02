class Anagram:
	def __init__(self, word):
		arr = list(word)
		__import__('random').shuffle(arr)
		print(''.join(arr))
		
if __name__ == '__main__':
	Anagram(input().strip())