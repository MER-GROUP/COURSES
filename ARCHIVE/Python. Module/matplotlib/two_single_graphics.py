import matplotlib.pylab as pylab

x = pylab.linspace(0, 5, 10)
y = x ** 2

fig, axes = pylab.plt.subplots(nrows=1, ncols=2)

cnt = int(1)
for ax in axes:
	ax.plot(x, y, 'r')
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	title = 'title ' + str(cnt)
	ax.set_title(title)
	cnt += 1

fig.tight_layout()

pylab.show()