import matplotlib.pylab as pylab

x = pylab.linspace(0, 5, 10)
y = x ** 2

fig, axes = pylab.plt.subplots(figsize=(12, 3))

axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')

pylab.show()