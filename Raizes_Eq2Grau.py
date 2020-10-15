# Algoritmo para calcular as raízes de uma Equação de 2do Grau
A = float(input('Escreva o valor correspondente ao coeficiente A: '))
B = float(input('Escreva o valor correspondente ao coeficiente B: '))
C = float(input('Escreva o valor correspondente ao coeficiente C: '))

raiz1 = (0 - B + ((B**2 - 4 * A * C)**(1/2))) / (2 * A)
raiz2 = (0 - B - ((B**2 - 4 * A * C)**(1/2))) / (2 * A)
print('As raízes da equação de segundo grau em estudo são', round(raiz1, 2), 'e', round(raiz2, 2))
