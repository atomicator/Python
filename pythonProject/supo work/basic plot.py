import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize


def straight_line(x, m, c):
    return x*m + c


plt.rc('text', usetex=True)
plt.rc('font', family='serif')

data = np.array([
    [0, -1642],
    [0.5, -1483],
    [1, -1300],
    [1.5, -1140],
    [2, -948],
    [2.5, -781],
    [3, -590],
    [3.5, -426],
    [4, -263],
    [4.5, -77],
])

N = 10
M = 19208/55
C = - 90793/55
variance = 0

result = scipy.optimize.curve_fit(straight_line, data[:, 0], data[:, 1])
errors = np.sqrt(np.diag(result[1]))
print(result[0], errors)

for result in data:
    variance += (result[1] - (M * result[0] + C)) ** 2

variance = (1/N) * variance

print(variance)

print(data[:, 0])

plt.plot(data[:, 0], data[:, 1], 'x')

plt.title(r"A graph")
plt.minorticks_on()
plt.grid(which="minor", axis="both")
plt.grid(which="major", axis="both", color="k")

plt.savefig("basic plot.pdf", format="pdf")

plt.show()

print("Done")
