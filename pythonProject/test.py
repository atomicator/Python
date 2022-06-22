import numpy as np
import matplotlib.pyplot as plt
import math

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

omega = np.linspace(0, 10, 1000)

y1 = np.sin(omega)
y2 = - 0.5 * np.sin(2 * omega)
y3 = y1 + y2


plt.xlim(0, 10)
plt.ylim(-2, 2)
plt.xlabel("time (s)")

plt.plot(omega, y1, ls="--", label=r"$\sin \omega_{0}$")
plt.plot(omega, y2, ls="--", label=r"$- \frac{1}{2} \sin 2 \omega_{0}$")
plt.plot(omega, y3, label=r"$\sin \omega_{0} - \frac{1}{2} \sin 2 \omega_{0}$")

h = plt.ylabel("Amplitude")
plt.title(r"$\sin \omega_{0} - \frac{1}{2} \sin \omega_{0}$")
plt.legend()
plt.savefig("test.pdf", format="pdf")

plt.show()

print("Done")
