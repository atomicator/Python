import numpy as np
import matplotlib.pyplot as plt
import math

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

omega = 1
gamma = [0.1, 0.2, 0.3, 0.4, 0.5]

t = np.linspace(0, 10, 100)
base = np.linspace(0, 0, 100)


def exponential(g, time):
    return math.e ** (-1 * g * time)


for value in gamma:
    y = exponential(value, t)
    plt.plot(t, y, label=(r"$\gamma = $" + " " + str(value)))

plt.xlim(0, 10)
plt.ylim(0, 1.1)
plt.xlabel("Time (s)")

plt.ylabel("Maximum Amplitude (m)")
plt.legend()
plt.title("Effects of varying damping on a lightly damped oscillator")
plt.savefig("light damping variable.pdf", format="pdf")

plt.show()

print("Done")
