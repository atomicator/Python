import numpy


def omega(n, m):
    return numpy.math.factorial(m + n - 1) / (numpy.math.factorial(m) * numpy.math.factorial(n - 1))


N = [2, 4]
m = [0, 1, 2, 3, 4, 5]

top = 0
combo = []
total = 0

for a in m:
    for b in m:
        for c in m:
            if a + b + c == 5:
                o = omega(2, a) * omega(4, b) * omega(4, c)
                print([[a, b, c], o])
                total += o
                if top < o:
                    top = o
                    combo = [a, b, c]
