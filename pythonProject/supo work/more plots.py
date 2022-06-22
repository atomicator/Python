import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

inv_temp = (np.array((0, 20, 40, 60, 80, 100)) + 276.16) ** -1

pressure = 1000 * np.array((4.3, 12, 28.4, 59.3, 110.9, 192.5))

plt.plot(inv_temp, np.log(pressure))

plt.show()
