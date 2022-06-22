import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

plt.rc('text', usetex=True)
plt.rc('font', family='serif')


def exponential(x, k, amp):
    return amp * np.cos(k * x + (np.pi / 2))


ka = np.pi
kb = - np.pi

base = np.linspace(0, 5, 1000)

A = 2
B = 1

plt.plot(base, exponential(base, ka, A))
plt.plot(base, exponential(base, kb, B))
plt.plot(base, exponential(base, ka, A) + exponential(base, kb, B))

plt.title(r"A graph")

plt.savefig("test.pdf", format="pdf")

plt.show()

print("Done")
