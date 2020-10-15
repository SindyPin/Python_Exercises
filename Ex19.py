# Resolva o seguinte sistema de equações lineares:
# 3.5x  + 2y           = 5
# -1.5x + 2.8y  + 1.9z = -1
#         -2.5y + 3z   = 2

import numpy as np

A = np.array([[3.5, 2.0, 0.0], [-1.5, 2.8, 1.9], [0, -2.5, 3.0]])
b = np.array([5, -1, 2])

x = np.linalg.solve(A, b)

print(x)
