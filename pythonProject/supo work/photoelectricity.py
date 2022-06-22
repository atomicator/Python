import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

e = 1.6e-19
n = 0.5


def first_guess(d, v0, w, n):
    global e
    v = (1 / e) * (w - e * v0 * d ** n)
    return v


data_set = 4

data = [[
    [0.253, 28],
    [0.305, 14],
    [0.358, 7],
    [0.410, 3]
], [
    [0.829, 44],
    [0.881, 20],
    [0.934, 10],
    [0.986, 4]
], [
    [0.934, 82],
    [0.986, 55],
    [1.039, 36],
    [1.091, 24],
    [1.143, 3]
], [
    [1.353, 67.5],
    [1.405, 36],
    [1.458, 19],
    [1.510, 11],
    [1.562, 4]
], [
    [1.929, 52],
    [1.981, 29],
    [2.034, 12],
    [2.086, 5],
    [2.138, 2.5]
]]

for data_set in range(5):
    data_to_use = np.array(data[data_set])#[data_set]

    #print(data)

    data_to_use = np.array(data_to_use)
    result = scipy.optimize.curve_fit(first_guess, data_to_use[:, 1], data_to_use[:, 0])
    errors = np.sqrt(np.diag(result[1]))
    print(result[0], errors)
    plt.plot(data_to_use[:, 1], data_to_use[:, 0], label='data')
    plt.plot(data_to_use[:, 1], first_guess(data_to_use[:, 1], *result[0]), label='model')
plt.legend()
plt.show()

    #print(result[0][1]/e)
