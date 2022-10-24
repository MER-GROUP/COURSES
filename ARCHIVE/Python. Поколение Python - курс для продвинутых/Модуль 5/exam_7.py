class Shop:
	def __init__(self):
		count_baza = int(input())
		baza_arr = [input() for _ in range(count_baza)]
		# print(baza_arr)
		
		baza_dict = dict()
		tmp = dict()
		for client in baza_arr:
			klient, tovar, cena = client.split()
			baza_dict[klient] = baza_dict.get(klient, dict())
			baza_dict[klient][tovar] = baza_dict.get(klient, dict()).get(tovar, 0) + int(cena)
				
		# print(baza_dict)
		for i in sorted(baza_dict):
			print(f'{i}:', sep='\n')
			for k in sorted(baza_dict[i]):
				print(f'{k} {baza_dict[i][k]}', sep='\n')
		
if __name__ == '__main__':
	Shop()