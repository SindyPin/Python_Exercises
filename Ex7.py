# Crie uma array com todos os números pares entre 100 e 200.

import numpy as np

A = np.arange(100, 202, 2)
print(A)

# Crie duas matrizes de formato 2x3, chamadas A e B, com elementos aleatórios amostrados da distribuição normal padrão:
A = np.random.standard_normal((2, 3))
print(A)

B = np.random.standard_normal((2, 3))
print(B)

# Multiplique A pela transposta de B, guardando o resultado na matriz D:
C = B.T
print(C)

D = A@C
print(D)

# Multiplique A e B elemento a elemento, guardando o resultado na matriz E:
E = A*B
print(E)

# Multiplique os elementos da primeira coluna de D pelo elemento E11 e substitua a segunda coluna de A pelo resultado:


