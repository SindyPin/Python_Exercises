# O seguinte exemplo ilustra o traçado de várias curvas em uma mesma janela e o uso de comandos para especificar os
# limites dos eixos e para atribuir um título ao gráfico e legendas aos eixos e às curvas:

import numpy as np
import matplotlib.pyplot as plt

# definindo os pontos do eixo x:
x = np.arange(0.0, 1.0, 0.1)

# plotando 4 curvas:
plt.plot(x, x**2, label='$y = x^2$')
plt.plot(x, x**3, label='$y = x^3$')
plt.plot(x, x**(1/2), label='$y = \sqrt{x}$')
plt.plot(x, x**(1/3), label='$y = \sqrt[3]{x}$')

# limites dos eixos: função axis
# o argumento deve ser uma lista na forma [xmin, xmax, ymin, ymax]
plt.axis([0, 1, 0, 1])

# título do gráfico: função title
plt.title('Gráficos boladões')

# legendas dos eixos: funções xlabel e ylabel
plt.xlabel('Eixo x boladão')
plt.ylabel('Eixo y boladão')

# legendas das curvas: função legend
plt.legend()

plt.show()
