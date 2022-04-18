# авторский алгоритм от BEEGIK
class Algo:
	def __init__(self, s):
		print(self.__algo(s))

	# Главная идея решения: строим список, который идентичен входной строке, 
	# но не содержит ничего кроме букв. Далее пользуемся методом двух указателей: 
	# left и right. Один указывает на начало строки, другой на конец соответственно.  
	# Еще заводим индикатор deleted_limit, который будет сообщать задействовали ли мы 
	# ранее возможность пропустить одну букву или нет. Логично, что если будем 
	# увеличивать left и уменьшать right то можем столкнутся с тем, что элементы 
	# на позиции не равны. В таком случае мы задействуем нашу возможность пропустить 
	# букву, отобразив в коде это как deleted_limit = True, остается только аккуратно 
	# проверить, что после пропущенного элемента будут стоять равные элементы.
	def __algo(self, s):
		string = [i for i in s if i.isalpha()]
		left, right = 0, len(string) - 1
		deleted_limit = False
		result = True

		while left <= right:
			if string[left] == string[right]:
				left += 1
				right -= 1
			elif string[left] != string[right] and not deleted_limit:
				if string[left+1] == string[right]:
					left += 1
					deleted_limit = True
				elif string[left] == string[right - 1]:
					right -= 1
					deleted_limit = True
				else:
					result = False
					break
			else:
				result = False
				break
		return result
		
if __name__ == '__main__':
	Algo(input())