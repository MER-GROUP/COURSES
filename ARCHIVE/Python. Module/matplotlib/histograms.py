import numpy
import matplotlib.pylab as pylab

n = numpy.random.randn(100000)
print(n)

fig, axes = pylab.plt.subplots(1, 2, figsize=(12, 4))

axes[0].hist(n)
axes[0].set_title('default histogram')
axes[0].set_xlim((min(n), max(n)))

axes[1].hist(n, cumulative=True, bins=50)
axes[1].set_title('cumulative histogram')
axes[1].set_xlim((min(n), max(n)))

fig.tight_layout()

pylab.show()