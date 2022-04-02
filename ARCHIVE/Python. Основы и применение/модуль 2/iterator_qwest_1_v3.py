class multifilter:

    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина функций (pos >= neg)
        return pos >= neg

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return pos >= 1

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge
        self.index = int()

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        return self
        
    def __next__(self):
        pos, neg = [0] * 2
        if self.index < len(self.iterable):
            self.index += 1
            for func in self.funcs:
                if func(self.iterable[self.index - 1]):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                return self.iterable[self.index - 1]
            else:
                #return next(self)
                return self.__next__()
        else:
            raise StopIteration
            
def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0

a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5))) 
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half))) 
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all))) 
# [0, 30]

print('--------------------')
lst = [i for i in range(-50, 50)]

test_base = [
    -50, -48, -46, -45, -44, -42, -40, -39, -38, -36, -35, -34, -33, -32, -30, -28, -27, -26, -25, -24, -22,
    -21, -20, -18, -16, -15, -14, -12, -10, -9, -8, -6, -5, -4, -3, -2, 0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14,
    15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48
]

test_half = [-50, -48, -45, -42, -40, -36, -30, -24, -20, -18, -15, -12, -10,
             -6, 0, 6, 10, 12, 15, 18, 20, 24, 30, 36, 40, 42, 45, 48]

test_all = [-30, 0, 30]

print(list(multifilter(lst, mul2, mul3, mul5))) 

print(list(multifilter(lst, mul2, mul3, mul5, judge=multifilter.judge_half)))

print(list(multifilter(lst, mul2, mul3, mul5, judge=multifilter.judge_all))) 
'''
assert list(multifilter(lst, mul2, mul3, mul5)) == test_base
assert list(multifilter(lst, mul2, mul3, mul5, judge=multifilter.judge_half)) == test_half
assert list(multifilter(lst, mul2, mul3, mul5, judge=multifilter.judge_all)) == test_all
'''