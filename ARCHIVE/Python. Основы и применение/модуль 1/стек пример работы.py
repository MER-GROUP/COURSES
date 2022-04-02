class Stack:
    def __init__(self):
        self.values = []
        self.size = 0
        self.maxsize = 0

    def push(self, element):
        self.values.append(element)
        self.size += 1
        if self.maxsize < self.size:
            self.maxsize = self.size

        print(self.values, '| size =', self.size, '| maxsize =', self.maxsize)

    def pop(self):
        assert self.size > 0, 'Нельзя удалять элементы из пустого стека'
        element = self.values.pop()
        self.size -= 1
        print(self.values, '| size =', self.size, '| maxsize =', self.maxsize)
        return element

stack = Stack()
stack.push('module')

def h():
    stack.push('h')
    stack.push('print')
    print(12)
    stack.pop()  # print
    stack.pop()  # h

def f():
    stack.push('f')
    g(h)
    stack.pop()  # f

def g(a):
    stack.push('g')
    a()
    stack.pop()  # g

g(f)
print('\nМаксимальный размер стека (maxsize) =', stack.maxsize)