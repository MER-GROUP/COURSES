class ExtendedStack(list):
    # операция сложения
    def sum(self):
    	s = self.pop() + self.pop()
    	self.append(s)

	# операция вычитания
    def sub(self):
    	s = self.pop() - self.pop()
    	self.append(s)

	 # операция умножения
    def mul(self):
    	s = self.pop() * self.pop()
    	self.append(s)

	# операция целочисленного деления
    def div(self):
        s = self.pop() // self.pop()
        self.append(s)