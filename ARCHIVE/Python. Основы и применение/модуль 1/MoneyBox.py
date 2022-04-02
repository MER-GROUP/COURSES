class MoneyBox:
    def __init__(self, capacity = int()):
    	self.coins = int()
    	self.capacity = capacity
    	
    def can_add(self, v):
        return True if v <= (self.capacity - self.coins) and 0 <= v else False

    def add(self, v):
        self.coins += v
        
x = MoneyBox(10)
x.add(5)
x.add(5)
print(x.coins, x.capacity)
print(x.can_add(0)) # True
x.add(0)
print(x.coins, x.capacity)