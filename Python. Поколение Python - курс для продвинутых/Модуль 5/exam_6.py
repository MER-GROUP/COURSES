class Zapros:
	def __init__(self):
		count_files = int(input())
		files_arr = [input() for _ in range(count_files)]
		files_dict = {}
		for file in files_arr:
			k, *v = file.split()
			files_dict[k] = v
		# print(files_dict)###
		
		count_zapros = int(input())
		zapros_arr = [input() for _ in range(count_zapros)]
		# print(zapros_arr)
		
		dostup = {'execute': 'X', 'write': 'W', 'read': 'R'}
		# print(dostup)###
		
		for zapros in zapros_arr:
			v_zap_comand, k_zap_file = zapros.split()
			if dostup[v_zap_comand] in files_dict[k_zap_file]:
				print('OK')
			else:
				print('Access denied')
		
if __name__ == '__main__':
	Zapros()