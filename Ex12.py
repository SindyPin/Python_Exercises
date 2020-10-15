# Plote a superfície da função 𝑓(𝑥,𝑦)=cos(𝑥2)+sin3(𝑦) no intervalo 𝑥=[−4,4] e 𝑦=[−4,4]

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import *

# Especificando os pontos do domínio:
x = y = np.linspace(-4, 4, 50)
X, Y = np.meshgrid(x, y)

# Especificamos os pontos da imagem:
Z = (np.cos(x) + 3*np.sin(y))

# Plotamos o gráfico 3D:
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
# ax.plot_trisurf(X, Y, Z, cmap='viridis', edgecolor='none')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
plt.show()

