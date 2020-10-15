import numpy as np
import matplotlib.pyplot as plt

# Valores do domínio:
x = np.linspace(-2*np.pi, 2*np.pi, 50)

# Valores da imagem:
y = np.cos(x)

# Plotar curva:
plt.plot(x, y)
plt.show()

# Plotar curva com asteriscos em vermelho:
plt.plot(x, y, '*r')
plt.show()

# Uma lista completa dos marcadores para customizar as curvas pode ser acessada por meio do help da função:
# help(plt.plot)
