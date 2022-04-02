import matplotlib.pylab as pylab

x = pylab.linspace(0, 5, 10)
y = x ** 2

fig = pylab.plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

#main figure
axes1.plot(x, y ,'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('main figure')

#insert figure
axes2.plot(y, x, 'g')
axes2.set_xlabel('x')
axes2.set_ylabel('y')
axes2.set_title('insert figure')

pylab.show()