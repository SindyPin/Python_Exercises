# Exemplo de Gráfico 3D:

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import *

# Especificando os pontos do domínio:
# Nota: A função np.meshgrid especifica a malha de pontos bidimensional aonde será inserido o gráfico
x = y = np.linspace(-4, 4, 50)
X, Y = np.meshgrid(x, y)

# Especificamos os pontos da imagem:
Z = (X**2 + Y**2)

# Plotamos o gráfico 3D:
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot_surface(X, Y, Z)
plt.show()

# Notas:
# Fizemos uso da função plt.subplots para criar uma figura (objeto fig) contendo um gráfico 3D (objeto ax).
# Uma vez criada a figura, usamos a função plt.plot_surface para plotar a superfície desejada utilizando os pontos
# armazenados em X, Y e Z.
