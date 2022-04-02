from random import *

def Global():
	global digits
	digits = str('0123456789')
	global lowercase_letters
	lowercase_letters = str('abcdefghijklmnopqrstuvwxyz')
	global uppercase_letters
	uppercase_letters = str('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	global punctuation
	punctuation = str('!#$%&*+-=?@^_')
	global chars
	chars = str()
	
def int_check(s):
	while True:
		if s.isdigit():
			return int(s)
		else:
			s = input('некоректный ввод : ')
	
def Equil(s):
	while True:
		if 'д' == s.lower():
			return True
		elif 'н' == s.lower():
			return False
		else:
			s = input('некоректный ввод : ')
	
def Zapros():
	count = input('Количество паролей для генерации : ')
	count = int_check(count)
	lengh = input('Длина одного пароля : ')
	lengh = int_check(lengh)
	bool_digits =input('Включать ли цифры 0123456789 ? (д/н) :')
	bool_digits = Equil(bool_digits)
	bool_uppercase_letters = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (д/н) : ')
	bool_uppercase_letters = Equil(bool_uppercase_letters)
	bool_lowercase_letters = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz ? (д/н) : ')
	bool_lowercase_letters = Equil(bool_lowercase_letters)
	bool_punctuation = input('Включать ли символы !#$%&*+-=?@^_ ? (д/н) : ')
	bool_punctuation = Equil(bool_punctuation)
	boo_no_std_chars = input('Исключать ли неоднозначные символы il1Lo0O? : ')
	boo_no_std_chars = Equil(boo_no_std_chars)
	return count, lengh, bool_digits, bool_uppercase_letters, bool_lowercase_letters, bool_punctuation, boo_no_std_chars
	
def Generate(count, lengh, bool_digits, bool_uppercase_letters, bool_lowercase_letters, bool_punctuation, boo_no_std_chars):
	abc = str()
	if bool_digits:
		abc += digits
	if bool_uppercase_letters:
		abc += uppercase_letters
	if bool_lowercase_letters:
		abc += lowercase_letters
	if bool_punctuation:
		abc += punctuation
	if boo_no_std_chars:
		for i in 'il1Lo0O?':
			if i in abc:
				abc = abc.replace(i, '')
	return [choices(abc, k=lengh) for _ in range(count)]
	
def arr_output(arr):
	for i in arr:
		print(''.join(i))
	
def Main():
	count, lengh, bool_digits, bool_uppercase_letters, bool_lowercase_letters, bool_punctuation, boo_no_std_chars = Zapros()
	arr = Generate(count, lengh, bool_digits, bool_uppercase_letters, bool_lowercase_letters, bool_punctuation, boo_no_std_chars)
	arr_output(arr)
	
Global()
Main()