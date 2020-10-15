# Plote as funções arcoseno, arcocosseno e arcotangente hiperbólicas nos domínios x=[−2,2],[1,2] e ]−1,1[ ,
# respectivamente. Nomeie os eixos x e y e dê um título e uma legenda a seu gráfico.

import numpy as np
import matplotlib.pyplot as plt

####################################################

# Valores do domínio da função arcoseno hiperbólico:
x = np.linspace(-1*np.pi, 2*np.pi, 50)

# Valores da imagem da função arcoseno hiperbólico:
y = np.arcsinh(x)

# Título do gráfico:
plt.title('Gráfico do Arcoseno Hiperbólico')

# Legendas dos eixos:
plt.xlabel('Valores do eixo "X" para o Arcoseno Hiperboólico')
plt.ylabel('Valores do eixo "Y" para o Arcoseno Hiperboólico')

# Plotar a curva da função arcoseno hiperbólico:
plt.plot(x, y)
plt.show()

####################################################

# Valores do domínio da função arcocoseno hiperbólico:
x = np.linspace(np.pi, 2*np.pi, 50)

# Valores da imagem da função arcocoseno hiperbólico:
y = np.arccosh(x)

# Título do gráfico:
plt.title('Gráfico do Arcocoseno Hiperbólico')

# Legendas dos eixos:
plt.xlabel('Valores do eixo "X" para o Arcocoseno Hiperboólico')
plt.ylabel('Valores do eixo "Y" para o Arcocoseno Hiperboólico')

# Plotar curva da função arcocoseno hiperbólico:
plt.plot(x, y)
plt.show()

####################################################

# Valores do domínio da função arcotangente hiperbólico:
x = np.linspace(-1*np.pi, np.pi, 50)

# Valores da imagem da função arcotangente hiperbólico:
y = np.arctanh(x)

# Título do gráfico:
plt.title('Gráfico do Arcotangente Hiperbólico')

# Legendas dos eixos:
plt.xlabel('Valores do eixo "X" para o Arcotangente Hiperboólico')
plt.ylabel('Valores do eixo "Y" para o Arcotangente Hiperboólico')

# Plotar curva da função arcotangente hiperbólico:
plt.plot(x, y)
plt.show()
