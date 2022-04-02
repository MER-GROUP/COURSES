def Words(words):
	words = words.split()
	idLong = int()
	for i in range(1, len(words)):
		if len(words[idLong])< len(words[i]):
			idLong = i
	print(words[idLong])

def Main():
	while True:
		print('---Main---')
		words = input()
		if 'q' == words:
			break
		else:
			Words(words)
		
Main()