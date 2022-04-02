import matplotlib.pylab as pylab

x = pylab.linspace(0, 5, 10)
y = x ** 2
print(x)
print(y)
'''
pylab.figure()
pylab.plot(x, y, 'r')
pylab.xlabel('x')
pylab.ylabel('y')
pylab.title('title')
pylab.show()
'''
fig = pylab.plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')
pylab.show()