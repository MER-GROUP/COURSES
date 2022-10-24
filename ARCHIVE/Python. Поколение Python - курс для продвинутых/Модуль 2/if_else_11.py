class Roskomnadzor:
	def __init__(self, word):
		word += ' запретил букву'
		#print(word)
		abc = [chr(i) for i in range(ord('а'), ord('я') + 1)]
		# print(abc)
		
		for i in abc:
			if i in word:
				print(word, i)
				word = word.replace(i, '').strip()
				word = word.replace('  ', ' ')
		
if __name__ == '__main__':
	Roskomnadzor(input())