def Main():
	print('---Main---')
	things = 'Я люблю про програмить на питоне ура !'
	fin = things.find('на')
	print(fin)
	print(things[fin : fin + len('на')])
	
Main()