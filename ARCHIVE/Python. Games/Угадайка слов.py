from random import *

#############################
class Hangman:
	__imena__ = ['maxim', 'ilias', 'igor', 'valera', 'sergey']
	__zveri__ = ['lisa', 'sobaka', 'koshka', 'medved', 'drakon']
	__car__ = ['mersedes', 'lexus', 'porshe', 'dodge', 'reno']
	__word_list__ = ['president', 'street', 'marathon', 'computer', 'hause', 'music'] + __imena__ + __zveri__ + __car__
	__word_list_only = ['president', 'street', 'marathon', 'computer', 'hause', 'music']
	
	__help_imena__ = dict(zip(__imena__,  ['подсказка - это мужское имя'] * len(__imena__)))
	__help_zveri__ = dict(zip(__zveri__,  ['подсказка - это животные'] * len(__zveri__)))
	__help_car__ = dict(zip(__car__,  ['подсказка - это машины'] * len(__car__)))
	__help_word_list__ = dict(zip(__word_list_only,  ['подсказка - подумай сам'] * len(__word_list_only)))
	
	__help__ = {**__help_imena__, **__help_zveri__, **__help_car__, **__help_word_list__}
	
	def __init__(self):
		pass
	
	@staticmethod
	def hello():
		print('Давайте играть в угадайку слов!')
	
	def get_word(self):
		print('Хотите выбрать категорию слов ? (д/н) : ')
		if self.__is_yes__(input()):
			print('''введите :
и - категория имен;
з - категория зверей;
м - категория машин.
''')
			s = input()
			while True:
				if 'и' == s.lower():
					return choice(self.__imena__).upper()
				elif 'з' == s.lower():
					return choice(self.__zveri__).upper()
				elif 'м' == s.lower():
					return choice(self.__car__).upper()
				else:
					s = input('некоректный ввод : ')
		else:
			return choice(self.__word_list__).upper()
		
	# функция получения текущего состояния
	@staticmethod
	def display_hangman(tries):
	    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
	                '''
	                   --------
	                   |      |
	                   |      O
	                   |     \\|/
	                   |      |
	                   |     / \\
	                   -
	                ''',
	                # голова, торс, обе руки, одна нога
	                '''
	                   --------
	                   |      |
	                   |      O
	                   |     \\|/
	                   |      |
	                   |     / 
	                   -
	                ''',
	                # голова, торс, обе руки
	                '''
	                   --------
	                   |      |
	                   |      O
	                   |     \\|/
	                   |      |
	                   |      
	                   -
	                ''',
	                # голова, торс и одна рука
	                '''
	                   --------
	                   |      |
	                   |      O
	                   |     \\|
	                   |      |
	                   |     
	                   -
	                ''',
	                # голова и торс
	                '''
	                   --------
	                   |      |
	                   |      O
	                   |      |
	                   |      |
	                   |     
	                   -
	                ''',
	                # голова
	                '''
	                   --------
	                   |      |
	                   |      O
	                   |    
	                   |      
	                   |     
	                   -
	                ''',
	                # начальное состояние
	                '''
	                   --------
	                   |      |
	                   |      
	                   |    
	                   |      
	                   |     
	                   -
	                ''',
	                # без веревки
	                '''
	                   --------
	                   |      
	                   |      
	                   |    
	                   |      
	                   |     
	                   -
	                ''',
	                # без доски
	                '''
	                   -
	                   |      
	                   |      
	                   |    
	                   |      
	                   |     
	                   -
	                ''',
	                # начало
	                '''
	                   
	                   
	                   
	                   
	                   
	                   |     
	                   -
	                '''
	    ]
	    return stages[tries]
	   
	@staticmethod
	def __is_abc__(s):
		while True:
			if not s.isalpha():
				s = input('некоректный ввод : ')
			else: return s.upper()
	
	@staticmethod
	def __zamena__(word, zagadka):
		if word == zagadka: return zagadka
		zag = zagadka
		zag = zag.replace(word, '_')
		res = str()
		for i in range(len(zag)):
			if not '_' == zag[i]:
				res += '_'
			else: res += zagadka[i]
		return res
		
	@staticmethod
	def __obrabotka__(otvet, pokaz):
		if otvet == pokaz: return pokaz
		res = str()
		for i in range(len(otvet)):
			if not '_' == pokaz[i]:
				res += pokaz[i]
			elif not '_' == otvet[i]:
				res += otvet[i]
			else: res += '_'
		return res
		
	@staticmethod
	def __is_yes__(s):
		while True:
			if 'д' == s: return True
			elif 'н' == s: return False
			else: s = input('некоректный ввод : ')
			
	@staticmethod
	def __is_hard__(s, yes, no):
		while True:
			if yes == s: return True
			elif no == s: return False
			else: s = input('некоректный ввод : ')
	
	def play(self, word_random):
		# строка, содержащая символы _ на каждую букву задуманного слова
		word_completion = None
		# сигнальная метка
		guessed = False
		# список уже названных букв
		guessed_letters = []
		# список уже названных слов
		guessed_words = []
		# количество попыток
		tries = None
		# сгенерированное загаданное слово
		#zagadka = self.get_word()
		zagadka = word_random
		otvet = str()
		pokaz = word_completion
		print(zagadka)###
		podskazka = False
		#print('Давайте играть в угадайку слов!')
		print('Играем в длинную или короткую версию ? (д/к) :')
		if self.__is_hard__(input().lower(), 'д', 'к'):
			tries = 9
		else: tries = 6
		print('отображать первую и последнюю буквы загаданного слова? (д/н) : ')
		if self.__is_hard__(input().lower(), 'д', 'н'):
			word_completion = '_' * len(zagadka)
			word_completion = zagadka[0] + '_' * (len(zagadka) - 2) + zagadka[-1]
			pokaz = word_completion
		else:
			word_completion = '_' * len(zagadka)
			pokaz = word_completion
		print('Отображать подсказки ? (д/н) : ')
		if self.__is_hard__(input(), 'д', 'н'):
			podskazka = True
		else : podskazka = False
		print('tries =', tries)###
		print(self.display_hangman(tries))
		print(' ' * 26, word_completion)
		while True:
			if podskazka:
				#print(self.__help__)
				print(self.__help__.get(word_random.lower()))###подсказка
			word = self.__is_abc__(input('введи букву или слово : '))
			if word in(*guessed_letters, *guessed_words):
				print(f'вы {word} уже вводили, повторите ввод : ')
				continue
			else:
				if 1 == len(word):
					guessed_letters.append(word)
				else:
					guessed_words.append(word)
			if word in zagadka and 1 == len(word) or word in zagadka and len(word) == len(zagadka):
				otvet = self.__zamena__(word, zagadka)
				#print(otvet)###
				if not guessed:
					guessed =True
					pokaz = otvet
				pokaz = self.__obrabotka__(otvet, pokaz)
				pokaz = self.__obrabotka__(pokaz, word_completion)
				print('tries =', tries)###
				print(self.display_hangman(tries))
				print(' ' * 26, pokaz)
				if not '_' in pokaz:
					print('Поздравляем, вы угадали слово! Вы победили!')
					print('желаете сыграть еще ? (д/н)')
					if self.__is_yes__(input()):
						#guessed_letters.clear()
						#guessed_words.clear()
						self.play(self.get_word())
					else:
						#break
						exit()
			else:
				tries -= 1
				print('tries =', tries)###
				print(self.display_hangman(tries))
				print(' ' * 26, pokaz)
				if 0 == tries:
					print('загаданное слово было :', zagadka)
					print('желаете сыграть еще ? (д/н)')
					if self.__is_yes__(input()):
						#guessed_letters.clear()
						#guessed_words.clear()
						self.play(self.get_word())
					else:
						#break
						exit()
	
#############################

def main():
	hangman = Hangman()
	#print(hangman.get_word())
	#print(hangman.display_hangman(0))
	hangman.hello()
	hangman.play(hangman.get_word())

if __name__ == '__main__':
	main()