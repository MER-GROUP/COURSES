# объявление функции
def is_pangram(text):
    for i in range(ord('a'), ord('z') + 1):
    	if chr(i) in text.lower():
    		continue
    	else: return False
    return True

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))

#можно использовать множество
# len(set(text)) == длине алфавита