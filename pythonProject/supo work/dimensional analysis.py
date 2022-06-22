import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt


def power_law(r, a, b):
    return a * r + b


aluminium_data = np.log(np.array([[1.5, 3.0, 6.0, 12.0],
                                  [0.167, 0.33, 0.58, 0.88]
                                  ]))

steel_data = np.log(np.array([[11.0, 17.5, 30.0, 52.5],
                             [0.89, 1.50, 2.65, 3.30]
                              ]))

density = 2.7e3
result = scipy.optimize.curve_fit(power_law, aluminium_data[0], aluminium_data[1])
errors = np.sqrt(np.diag(result[1]))
values = result[0]

print(values, "\n", errors)

density = 7.83e3
result = scipy.optimize.curve_fit(power_law, steel_data[0], steel_data[1])
errors = np.sqrt(np.diag(result[1]))
values = result[0]

print(values, "\n", errors)

plt.plot(aluminium_data[0], aluminium_data[1])
plt.plot(steel_data[0], steel_data[1])
plt.show()
