#

import scipy as

def rosenbrock (x):
    return 100*(x[1]-x[0]**2)**2 + (1-x[0])**2
# estimativa inicial
x0 = [0, 0]

# minimizando!
resultado = scipy.optimize.minimize(rosenbrock, x0)

print(resultado)
