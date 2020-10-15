# Otimizando um problema:

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

x = np.linspace(-2, 2, 20)
y = np.linspace(-1, 3, 20)
X, Y = np.meshgrid(x, y)

Z = 100*(Y-X**2)**2 + (1-X)**2

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot_surface(X, Y, Z, cmap=cm.rainbow)

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$f(x,y)$')

plt.show()
