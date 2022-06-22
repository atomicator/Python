import numpy as np
import matplotlib.pyplot as plt
import math

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x_range = 20

omega = np.linspace(0, x_range, 1000)

y1 = np.e ** (- 0.1 * omega) * np.sin(omega)
y2 = - 0.5 * np.sin(2 * omega)
y3 = y1 + y2


plt.xlim(0, x_range)
plt.ylim(-2, 2)

plt.plot(omega, y1, ls="--", label="Transient solution")
plt.plot(omega, y2, ls="--", label="Steady state solution")
plt.plot(omega, y3, label="Combination solution")

plt.xlabel("Time (s)")
h = plt.ylabel("Amplitude")
plt.title(r"Transient and steady state oscillations")

plt.savefig("combination oscillation.pdf", format="pdf")
plt.legend()

plt.show()

print("Done")