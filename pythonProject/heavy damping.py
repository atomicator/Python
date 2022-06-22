import numpy as np
import matplotlib.pyplot as plt
import math

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

omega = 1
gamma = [2, 4, 8]
A = [-0.07735, -0.0164, -0.00395]

t = np.linspace(0, 10, 100)


def heavy_damping(g, time, a, b, o):
    return a * math.e ** (-1*(g + math.sqrt(g**2 - o**2)) * time) + b * math.e ** (-1*(g - math.sqrt(g**2 - o**2)) *
                                                                                   time)


for num in gamma:
    b = 1 - A[gamma.index(num)]
    y = heavy_damping(num, t, A[gamma.index(num)], b, omega)

    plt.plot(t, y, label=(r"$\gamma = $" + " " + str(num)))


plt.xlim(0, 10)
plt.ylim(0, 1.1)
plt.xlabel("Time (s)")

plt.ylabel("Maximum Amplitude (m)")
plt.legend()
plt.title("Effects of varying damping on a heavily damped oscillator")

plt.savefig("heavy damping variable.pdf", format="pdf")

plt.show()

print("Done")
