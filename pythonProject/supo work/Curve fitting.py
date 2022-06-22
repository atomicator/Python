import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

plt.rc('text', usetex=True)
plt.rc('font', family='serif')


def offset_sin(t, mean, amplitude, phi):
    displacement = mean + amplitude * np.sin(t * omega + phi)
    return displacement


omega = np.pi / 2

data = np.array((2, 6, 6, 12, 1, 4, 9, 7, 5, 5, 9, 3, 2, 12, 5, 8, 6, 5, 6, 6,
        4, 4, 6, 11, 3, 1, 8, 1, 3, 4, 9, 7, 2, 3, 6, 6, 3, 1, 5, 4,
        3, 7, 2, 4, 2, 6, 6, 6, 0, 4, 11, 3, 2, 4, 9, 4, 0, 2, 5, 8,
        0, 6, 7, 8, 1, 6, 10, 7, 0, 2, 9, 9, 2, 4, 6, 5, 6, 3, 8, 12,
        6, 2, 8, 9, 3, 3, 9, 4, 1, 3, 9, 4, 3, 3, 5, 5, 9, 10, 8, 3))

t_range = 99

t_base = np.linspace(0, t_range, 100)

sin_points = np.linspace(0, t_range, 10000)

result = scipy.optimize.curve_fit(offset_sin, t_base, data)
errors = np.sqrt(np.diag(result[1]))
values = result[0]

print(values, "\n", errors)

plt.plot(t_base/4, data, label="The raw data")

plt.plot(sin_points/4, offset_sin(sin_points, *values), label="The fitted curve")

plt.ylabel("Amplitude")
plt.xlabel("Oscillations")
plt.legend()
plt.title("The raw data and the fitted curve")

plt.savefig("fitted curve.pdf", format="pdf")

plt.show()

noise = data - offset_sin(t_base, *values)

plt.plot((t_base / 4), noise)

plt.ylabel("Amplitude")
plt.xlabel("Oscillations")
plt.title("The noise at each measurement")

plt.savefig("noise.pdf", format="pdf")

plt.show()

print(t_base)

print("Done")
