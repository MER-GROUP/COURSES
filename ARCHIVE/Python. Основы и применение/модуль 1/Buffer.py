class Buffer:
    # конструктор без аргументов
    def __init__(self):
        self.__arr__ = list()

	# добавить следующую часть последовательности
    def add(self, *a):
        self.__arr__.extend(a)
        if 5 <= len(self.__arr__):
        	self.get_current_part()

	# вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
    def get_current_part(self):
        if 5 > len(self.__arr__):
        	#print(self.__arr__)
        	return self.__arr__
        else:
        	#res = list()
        	while True:
        		if 5 > len(self.__arr__):
        			break
        		else:
        			tmp = self.__arr__[ : 5].copy()
        			print(sum(tmp))
        			#res.append(sum(tmp))
        			del self.__arr__[ : 5]
        	#return res
        			
buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]