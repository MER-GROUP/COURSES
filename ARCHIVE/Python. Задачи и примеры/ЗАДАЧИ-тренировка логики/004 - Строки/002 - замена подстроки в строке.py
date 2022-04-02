def Enter():
	try:
		word = input()
		if 'q' == word:
			pass
	except ValueError:
		print('Некоректный ввод')
	finally:
		return word
		
def ReplaceWords(oldWord, newWord, words):
	beginWord = words.find(oldWord)
	while 0 < beginWord:
		beginStr = words[ : beginWord]
		endStr = words[beginWord + len(oldWord) : ]
		words = beginStr + newWord + endStr
		beginWord = words.find(oldWord)
	print(words)

def Main():
	print('---Main---')
	words = "tree, box, chair, lamp, \n desk, cat, dog, grass, \n pig, box, lamp, shelf"
	print(words)
	while True:
	   oldWord = None
	   while oldWord is None:
	   	oldWord = Enter()
	   if 'q' == oldWord:
	   	break
	   newWord = None
	   while newWord is None:
	   	newWord = Enter()
	   ReplaceWords(oldWord, newWord, words)
	
Main()