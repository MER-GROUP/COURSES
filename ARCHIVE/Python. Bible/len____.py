while True:
	word=input('Введите слово'
	                      'для прдсчета '     
	                      'символов (Q - выход) : ')
	if word=='Q' or word=='q':
		break
	print('{} имеет {} символов'.
	          format(word,len(word)))