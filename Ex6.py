import numpy as np

A = np.array([[1, 2], [3, 4]])
print(A)

B = np.array([[5, 6], [7, 8]])
print(B)

# operador @: usado na forma A@B, efetua a multiplicação entre duas matrizes A e B.
# Obs: a função np.matmul (A,B) também efetua a multiplicação entre matrizes;
C = A@B
print(C)
C = np.matmul(A, B)
print(C)

# operador *: usado na forma A*B, efetua a multiplicação entre duas matrizes A e B calculando os produtos entre
# os elementos de posições equivalentes, a chamada operação elemento a elemento, ou element-wise.
# Obs: a função np.multiply (A,B) também efetua a multiplicação elemento a elemento;
D = A*B
print(D)

# atributo T: armazena a transposta da matriz. Acessado na forma D.T, sendo D a matriz que se está transpondo;
E = D.T
print(E)

# np.linalg.inv (A): calcula a inversa da matriz A;
F = np.linalg.inv(A)
print(F)

# np.linalg.norm (B): calcula a norma da matriz ou vetor B;
G = np.linalg.norm(B)
print(G)

# np.linalg.eigvals (A): calcula os autovalores da matriz A.
H = np.linalg.eigvals(A)
print(H)

