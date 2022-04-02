# использование множественного наследования
import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
        
class LoggableList(list, Loggable):
	def append(self, obj):
		super(LoggableList, self).append(obj)
		super(LoggableList, self).log(obj)
		
		super().append(obj)
		super().log(obj)
		
		# self.append(obj) будет ошибка
		super().append(obj)
		self.log(obj)
		
		list.append(self, obj)
		Loggable.log(self, obj)
		
test = LoggableList()
test.append(5)
print(test)