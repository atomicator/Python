import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')


def effective_potential(k, r, a):
    js = m * r ** 3 * k 
    v = - (k / r) * np.exp(- r / a)
    return v


r = 1e-10
a = 1e-9

k = np.linspace(0, 1e-10, 10000)

y = effective_potential(k, r, a)

plt.plot(k, y)
plt.show()
