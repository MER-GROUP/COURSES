import matplotlib.pylab as pylab

x = pylab.linspace(0, 5, 10)
y = x ** 2
print(x)
print(y)
pylab.figure()
pylab.plot(x, y, 'r')
pylab.xlabel('x')
pylab.ylabel('y')
pylab.title('title')
pylab.show()