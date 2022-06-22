import numpy as np
import matplotlib.pyplot as plt
import math

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

max = 4
min = -4

t = np.linspace(-max, max, 1000)


def cosh(x):
    return (math.e ** x + math.e ** -x)/2


def sinh(x):
    return (math.e ** x - math.e ** -x)/2


def tanh(x):
    return sinh(x)/cosh(x)


functions = [cosh, sinh, tanh]
name = ["cosh", "sinh", "tanh"]

for func in functions:

    y = func(t)

    plt.plot(t, y, label=name[functions.index(func)])


plt.xlim(min, max)
plt.ylim(-5, 5)


plt.title("Hyperbolic functions")
plt.legend()

plt.savefig("hyperbolic functions.pdf", format="pdf")

plt.show()

print("Done")
