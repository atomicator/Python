import numpy as np
import matplotlib.pyplot as plt
import math

max = 3


def hyp(a):
    return (a**2 - 1)**(1/2)


plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x = np.linspace(-max, max, 1000)
y = np.linspace(1, max, 1000)

plt.plot(x, x, linestyle='--', color="black")
plt.plot(-x, x, linestyle='--', color="black")

plt.plot(y, hyp(y), linestyle='-', color="blue")
plt.plot(y, -hyp(y), linestyle='-', color="blue")
plt.plot(-y, hyp(y), linestyle='-', color="blue")
plt.plot(-y, -hyp(y), linestyle='-', color="blue")

plt.xlim(-max, max)
plt.ylim(-max, max)

plt.title("Hyperbola")

plt.savefig("hyperbola.pdf", format="pdf")

plt.show()
