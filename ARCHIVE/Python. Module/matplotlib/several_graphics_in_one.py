import matplotlib.pylab as pylab

x = pylab.linspace(0, 5, 10)
y = x ** 2

fig, axes = pylab.plt.subplots()

axes.plot(x, x ** 2, label = 'y = x ** 2')
axes.plot(x, x ** 3, label = 'y = x ** 3')
axes.legend(loc=2)
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')

pylab.show()