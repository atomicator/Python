import numpy as np
import matplotlib.pyplot as plt
import math

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

omega = 1
gamma = 0.1

t = np.linspace(0, 30, 100)
base = np.linspace(0, 0, 100)


def exponential(g, time):
    return math.e ** (-1 * g * time)


def oscillation(o, g, time):
    return exponential(g, time) * np.cos(o * t)


y = exponential(gamma, t)
z = -1 * y
a = oscillation(omega, gamma, t)


plt.plot(t, y, "k", linestyle="dashed")
plt.plot(t, z, "k", linestyle="dashed")
plt.plot(t, a)
plt.plot(t, base, "k")

plt.xlim(0, 30)

plt.xlabel("Time (s)")

plt.ylabel("Amplitude (m)")
plt.title("Motion of a lightly damped oscillator")

plt.savefig("light damping.pdf", format="pdf")

plt.show()

print("Done")
