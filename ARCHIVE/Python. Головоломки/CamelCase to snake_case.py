# объявление функции
def convert_to_python_case(text):
    arr = list()
    start, end = int(), int()
    count = int()
    i = int()
    while i < len(text):
    	if text[i].isupper() and 0 == count:
    		start = i
    		count += 1
    	elif text[i].isupper() and 1 == count:
    		end = i
    		count += 1
    	if 2 == count:
    		arr.append(text[start : end].lower())
    		count = 0
    		i -= 1
    	elif 1 == count and i + 1 == len(text):
    		arr.append(text[start : ].lower())
    	i += 1
    return '_'.join(arr)

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))