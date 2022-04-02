def isPolindrom(s):
	return s[ : ] == s[ : : -1]
	
def isProstoe(s):
	count = int()
	for i in range(2, int(s) + 1):
		if 0 == int(s) % i:
			count += 1
	return True if 1 == count else False
	
def isEven(s):
	return True if 0 == int(s) % 2 else False

# объявление функции
def is_valid_password(password):
    arr = password.split(':')
    if 3 == len(arr):
    	return isPolindrom(arr[0]) and isProstoe(arr[1]) and isEven(arr[2])
    return False

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))