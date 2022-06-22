import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

m = 3.293

data = np.loadtxt("/home/thomas/OneDrive/Documents/laser presentation/slit width.csv",
                  delimiter=",", skiprows=1)

fixed_slit_data = np.transpose(data[:, 0:2])
variable_slit_data = np.transpose(data[0:-2, 2:])

plt.scatter((1 / fixed_slit_data[0]), fixed_slit_data[1], marker="_", label="Fixed slit mean")
plt.title("Fixed slit results")
plt.ylabel("Distance to first minima (mm)")
plt.xlabel(r"Inverse slit width (mm)$^{-1}$")

plt.errorbar((1 / fixed_slit_data[0]), fixed_slit_data[1], yerr=1, ecolor="black", fmt="none",
             elinewidth=1, capsize=2, label="fixed slit error")

x = np.linspace(min((1 / fixed_slit_data[0])), max((1 / fixed_slit_data[0])), 1000)
y = m * x

plt.plot(x, y, linestyle="dotted", color="red", label=f"{m} $\\times$ inverse slit width")
plt.legend()
plt.savefig("fixed slit.pdf", format="pdf")

plt.show()

plt.scatter((1 / fixed_slit_data[0]), fixed_slit_data[1], marker="_", label="Fixed slit mean")
plt.errorbar((1 / fixed_slit_data[0]), fixed_slit_data[1], yerr=1, ecolor="black", fmt="none",
             elinewidth=1, capsize=2, label="Fixed slit error")

plt.scatter((1 / variable_slit_data[0]), variable_slit_data[1], marker="_", label="Variable slit mean")
plt.errorbar((1 / variable_slit_data[0]), variable_slit_data[1], yerr=5, ecolor="black", fmt="none",
             elinewidth=1, capsize=2, label="Variable slit error")

x = np.linspace(min((1 / fixed_slit_data[0])), max((1 / fixed_slit_data[0])), 1000)
y = m * x
plt.plot(x, y, linestyle="dotted", color="red", label=f"{m} $\\times$ inverse slit width")

plt.ylabel("Distance to first minima (mm)")
plt.xlabel(r"Inverse slit width (mm)$^{-1}$")
plt.title("All of the single slit data")

plt.legend()
plt.savefig("all points.pdf", format="pdf")
plt.show()
