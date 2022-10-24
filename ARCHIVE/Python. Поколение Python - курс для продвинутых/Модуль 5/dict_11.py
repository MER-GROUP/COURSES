class Morse:
	def __init__(self, s):
		letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
		morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
		self.morse = dict(zip(letters, morse))
		# print(self.morse)
		self.__crypt(s)
		
	def __crypt(self, s):
		for i in s:
			if i in self.morse.keys():
				print(self.morse.get(i), end=' ')
		
if __name__ == '__main__':
	Morse(input().upper())