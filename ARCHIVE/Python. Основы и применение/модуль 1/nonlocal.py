def f():	
	ok_status = True
	vowels = list('auieo')
	#print(vowels)
	
	def check(word):
		nonlocal ok_status
		for vowel in vowels:
			if vowel in word:
				return True
		ok_status = False
		return False
		
	print(check('abacaba'))
	print(ok_status)
	print(check('www'))
	print(ok_status)
	
f()
#print(ok_status)