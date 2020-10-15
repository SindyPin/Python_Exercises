import numpy as np

A = np.arange(0.0, 5.0, 0.5)
print(A)

B = np.linspace(0.0, 5.0, 3)
print(B)

C = np.zeros(3)
print(C)

D = np.zeros((2, 3))
print(D)

E = np.ones((4, 5))
print(E)

F = np.zeros_like(E)
print(F)

G = np.random.standard_normal((2, 3))
print(G)
