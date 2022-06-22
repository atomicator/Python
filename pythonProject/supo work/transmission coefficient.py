import matplotlib.pyplot
import numpy
import sympy
import matplotlib.pyplot as plt

# E, hbar, m, V, a = sympy.symbols("E hbar m V a")
E = numpy.linspace(0, 1.6e-18, 10000)
m = 1.67e-27
hbar = 1.05e-34
V = 1.6e-19
a = 1e-8


k1 = numpy.sqrt((2 * m * E) / (hbar ** 2))
k2 = numpy.sqrt((2 * m * (E + V)) / (hbar ** 2))

t = numpy.absolute(((2 * k1 * k2) / (2 * k1 * k2 * numpy.cos(k2 * a) + (k1 ** 2 + k2 ** 2) * numpy.sin(a * k2)))\
    * numpy.exp(1j * k1 * a))

#  p = sympy.plot(t.subs("m", 1.67e-27).subs("hbar", 1.05e-34).subs("V", 1.6e-19).subs("a", 1e-8), (E, 0, 1.6e-19 * 5),
#           xlim=(0, 5 * 1.6e-19))
plt.plot(E, t)
plt.show()
print("done")
print(t)
