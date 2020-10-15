# Algoritmo para calcular as raízes de uma Equação de 2do Grau

import math

A = float(input('Escreva o valor correspondente ao coeficiente A: '))
B = float(input('Escreva o valor correspondente ao coeficiente B: '))
C = float(input('Escreva o valor correspondente ao coeficiente C: '))

delta = (B ** 2 - 4 * A * C)

if delta < 0:
    print('O valor de DELTA é', delta)
    print('As raízes desta equação de segundo grau NÃO correspondem aos números reais, senão aos imaginários. \
Digite novamente outros valores de coeficientes')
else:
    raiz_delta = math.sqrt(delta)
    raiz1 = (0 - B + raiz_delta) / (2 * A)
    raiz2 = (0 - B - raiz_delta) / (2 * A)
    print('As raízes da equação de segundo grau em estudo são', raiz1, 'e', raiz2)
