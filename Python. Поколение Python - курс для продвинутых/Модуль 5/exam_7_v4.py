class Shop:
	def __init__(self):
		count_baza = int(input())
		baza_arr = [input() for _ in range(count_baza)]
		# print(baza_arr)
		
		baza_dict = dict()
		for client in baza_arr:
			klient, tovar, cena = client.split()
			baza_dict.setdefault(klient, dict()).update({tovar: baza_dict[klient].get(tovar, 0) + int(cena)})
		# print(baza_dict)
		
		for klient in sorted(baza_dict):
			print(f'{klient}:')
			for tovar in sorted(baza_dict[klient]):
				print(f'{tovar} {baza_dict[klient][tovar]}')
		
if __name__ == '__main__':
	Shop()