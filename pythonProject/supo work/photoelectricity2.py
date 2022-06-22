import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

e = 1.6e-19
c = 3e8


def stopping_potential(lam, h, w):
    global e, c
    vs = (1 / e) * (((h * c * 1e9) / lam) - w)
    return vs


data = np.array([
    [546, 0.3315],
  #  [434, 1.5804],
    [405, 1.1601],
    [365, 1.8393],
    [313, 3.2784]
])

result = scipy.optimize.curve_fit(stopping_potential, data[:, 0], data[:, 1])
errors = np.sqrt(np.diag(result[1]))
print(result[0], errors)
plt.plot(data[:, 0], data[:, 1], label='data')
plt.plot(data[:, 0], stopping_potential(data[:, 0], *result[0]), label='model')
plt.legend()
plt.show()
