import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

data = np.loadtxt("/home/thomas/OneDrive/Documents/laser presentation/circle stuff.csv",
                  delimiter=",", skiprows=1)

m = 0.016502

data = np.transpose(data)

plt.scatter(data[0], data[1], marker="_")
plt.title("Circular aperture results")
plt.ylabel("Radius (m)")
plt.xlabel(r"Calculated Bessel coefficient $\times \frac{1}{\pi}$")

plt.errorbar(data[0], data[1], yerr=0.003, ecolor="black", fmt="none",
             elinewidth=1, capsize=2)

x = np.linspace(min(data[0]), max((data[0])), 1000)
y = m * x

plt.plot(x, y, linestyle="dotted", color="red", label=f"{m}" + r"$\times$ Bessel coefficient $\times \frac{1}{\pi}$")
plt.legend()
plt.savefig("circle stuff.pdf", format="pdf")

plt.show()
