# This function approximates a differential equation  using the Euler and Runge-Kutta methods, comparing the results
# to the analytic solution to calculate the error in each approximation.

import matplotlib.pyplot as plt  # used to plot the graphs
import numpy as np

iterations = range(1, 1000)  # An array containing the number of iterations that should be done for each data point.
# For each number, an approximation is done using n iterations
consts = [2, 2, 1, 2, 2]  # The constants used in the equations
y0, x0 = 0, 0  # The initial x and y values
x_range = 5  # The range to be approximated over
print(x0, y0)


def y_prime(x, y, a=consts[0], b=consts[1], c=consts[2], d=consts[3], e=consts[4]):  # the value of dy/dx
    yp = a * x ** 4 + b * x ** 3 + c * x ** 2 + d * x + e
    return yp


def y_exact(x, a=consts[0], b=consts[1], c=consts[2], d=consts[3], e=consts[4]):  # the analytic solution of y
    ye = (a / 5) * x ** 5 + (b/4) * x ** 4 + (c / 3) * x ** 3 + (d / 2) * x ** 2 + e * x
    return ye


def iterate_euler(n, xr=x_range, initial_values=[x0, y0]):  # iterates using the euler method
    x, y = initial_values
    x_values, y_values = [x], [y]  # stores all of the points, can be used to plot an approximation
    delta_x = xr / n  # the step in x
    for i in range(n):
        y += delta_x * y_prime(x, y)  # update y
        x += delta_x  # update x
        x_values.append(x)  # add the points to the list
        y_values.append(y)
    return [x_values, y_values]  # return the points


def iterate_runge(n, xr=x_range, initial_values=[x0, y0]):  # iterates using the runge-kutta method
    x, y = initial_values
    x_values, y_values = [x], [y]  # stores all of the points
    delta_x = xr / n  # the step in x
    for i in range(n):
        k1 = delta_x * y_prime(x, y)
        k2 = delta_x * y_prime(x + delta_x / 2, y + k1 / 2)
        k3 = delta_x * y_prime(x + delta_x / 2, y + k2 / 2)
        k4 = delta_x * y_prime(x + delta_x, y + k3)  # calculates the constants used in the iteration
        y += (1/6) * (k1 + 2 * k2 + 2 * k3 + k4)  # updates y
        x += delta_x  # updates x
        x_values.append(x)
        y_values.append(y)  # add the values to the list
    return [x_values, y_values]  # returns the points


def plot_approximation(n):  # This method imports variables from global scope
    data = iterate_euler(n)  # creates an euler approximation for n
    plt.plot(*data, label="Euler Approximation")  # plots the data

    base = np.linspace(x0, x0 + x_range, 10000)
    analytic_function = y_exact(base)
    plt.plot(base, analytic_function, label="Analytic solution")  # plots the analytical solution

    data = iterate_runge(n)  # creates a runge-kutta approximation usind n iterations
    plt.plot(*data, label="Runge-Kutta Approximation")

    plt.legend()  # adds a legend to the plot
    plt.title(f"A comparison of the analytic solution and euler approximation \n using {n} iterations")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()  # displays the plot
    return True


euler_errors = []  # stores all of the errors in the final value of the euler approximations
runge_errors = []  # same as above, for the runge-kutta approximations
for N in iterations:  # for each desired number of approximations
    print(N)
    y = iterate_euler(N)  # euler approximate the solution
    euler_errors += [np.log(abs(y[1][-1] - y_exact(x0 + x_range)))]  # add the result to jthe list
    y = iterate_runge(N)  # runge-kutta approximate the solution
    runge_errors += [np.log(abs(y[1][-1] - y_exact(x0 + x_range)))]  # add the result to the list

print("Plotting")
plt.plot(np.log(iterations), euler_errors, label="Euler approximation")  # Plot the results
plt.plot(np.log(iterations), runge_errors, label="Runge-Kutta approximation")
plt.xlabel("ln(Number of iterations)")
plt.ylabel("ln(abs(Error))")
plt.title("The error for increasing numbers of iterations")
plt.legend()
plt.show()
