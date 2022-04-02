s =int(input()[1 : ])
arr = [input() for _ in range(s)]
for i in range(len(arr)):
	if '#' == arr[i][0]: 
		#del arr[i]
		continue
	elif '#' in arr[i]:
		arr[i] = arr[i][ : arr[i].find('#')].rstrip()
		print(arr[i])
	else:
		print(arr[i])