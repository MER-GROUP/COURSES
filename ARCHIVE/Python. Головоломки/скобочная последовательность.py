# объявление функции
def is_correct_bracket(text):
    count = int()
    for i in text:
    	if 0 > count: return False
    	if '(' == i:
    		count += 1
    	else: count -= 1
    return 0 == count

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))