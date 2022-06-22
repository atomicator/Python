import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

plt.rc('text', usetex=True)
plt.rc('font', family='serif')


def equation(x, u, mu0, r, m):
    return (3 * u * mu0 * (r ** 2) * m * x) / (2 * (r ** 2 + x ** 2) ** (5/2))


x = np.linspace(-10, 10, 10000)

u = 1
mu0 = 4 * np.pi * 1e-7
r = 1
m = 1

plt.plot(x, equation(x, u, mu0, r, m))

plt.title(r"A graph")

plt.savefig("stuff.pdf", format="pdf")

plt.show()

print("Done")