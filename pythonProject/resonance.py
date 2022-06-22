import numpy as np
import matplotlib.pyplot as plt
import math

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

gamma = [0.1, 0.2, 0.5, 1, 2]
A = [-0.07735, -0.0164, -0.00395]
f = 1
n = 1

omega = np.linspace(0, 2.5, 1000)


def resonance(g, o1, o):
    return f / (np.sqrt(((o1 ** 2 - o ** 2) ** 2) + 4 * g ** 2 * o ** 2))


for num in gamma:
    y = resonance(num, n, omega)
    plt.plot(omega, y, label=r"$\gamma = $" + " " + str(num))


plt.xlim(0, 2.5)
plt.ylim(0, 6)
plt.xlabel(r"$\omega$" + " (rad." + r"s$^{-1}$)")

h = plt.ylabel(r"$\frac{A}{A_{0}}$", position=(0, 0.54), size=16)
print(h.get_position())
plt.legend()
h.set_rotation(0)
plt.title("Effects of varying damping on a forced oscillator")

plt.savefig("resonance.pdf", format="pdf")

plt.show()

print("Done")
