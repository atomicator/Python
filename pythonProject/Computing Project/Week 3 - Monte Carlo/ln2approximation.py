# ln2approximation.py - This approximates the value of ln(2) by comparing it to the area below the line y = 1 / x
# for floats 1 < x < 2 and 0 < y < 1. By integration, it can be shown that this area equals ln(2). RNG is used to
# generate values of x and y in this range. The number of points that lie within this range is recorded, and used to
# calculate the fraction of points that lie in this region, from which ln(2) can be estimated. This data was then used
# to plot the approximation and error as a function of the number of iterations. This program initially tries to use
# latex, however if this raises an error (due to a local latex compiler not being installed) it will default to using
# normal strings.

import math  # used to get an exact value of ln 2
import time
import matplotlib.pyplot as plt  # used to create the plots
import random  # used to generate the random numbers


N = 10000000  # The number of iterations to be used
area = 1  # The area of the x and y range that the points can be in. This is used to convert the fraction to a value


def calculate_data(n, area):
    in_range = 0  # The number of guesses that where within the desired range
    estimations = []  # Records the guess for each iteration
    errors = []  # Records the absolute error for each iteration
    for i in range(n+1)[1:]:  # This adds one to each value in range(N), preventing a zero error
        y = random.random()  # creates a random float between 0 and 1
        x = random.random() + 1  # creates a random float between 1 and 2
        if y < (1 / x):  # If it is within the range
            in_range += 1  # update the number of points within the range
        value = (in_range / i) * area  # calculates an estimate of ln 2
        estimations.append(value)  # adds the value to the list
        error = abs(math.log(2, math.e) - value)  # calculates the absolute error in the calculated value
        errors.append(error)  # adds the error to the list
        print(f"The {i}th estimate is {value}, with an error of {error}.")  # print the value and its error
    return [estimations, errors]  # returns the calculated values


def plot_data(data, strings):  # plots the data
    estimations, errors = data
    plt.figure()
    plt.plot(range(N+1)[1:], estimations, "b", label=strings[0])  # plot the estimations
    plt.plot(range(N+1)[1:], [math.log(2, math.e)] * N, "r", label=strings[1])  # plot the actual value of ln 2
    plt.legend()  # add a legend to the plot
    ax = plt.subplot(111)  # this line and the one below sets the x-axis to be logarithmic
    ax.set_xscale('log')
    plt.title(strings[2])  # adds a title to the plot
    plt.savefig("value.pdf", format="pdf")  # saves the figure as a pdf
    plt.show()  # display the plot
    plt.figure()  # creates a new figure
    ax = plt.subplot(111)
    ax.set_yscale('log')  # sets both axis to be logarithmic
    ax.set_xscale('log')
    plt.plot(range(N+1)[1:], errors, "b", label=strings[3])  # plots the errors
    plt.legend()  # adds a legend to the plot
    plt.title(strings[4])
    plt.savefig("error.pdf", format="pdf")  # saves the figure as a pdf
    plt.show()  # displays the plot


if __name__ == "__main__":
    results = calculate_data(N, area)  # calculate the results
    try:  # The program tries to run using latex
        plt.rc('text', usetex=True)  # Tells matplotlib to use latex. This requires a compiler to be installed locally,
        plt.rc('font', family='serif')  # or it will raise an error (which will be
        titles = [r"Numerical $\ln (2)$", r"Analytical $\ln (2)$",  # an array used to store the various titles and
                  r"Numerical approximations for the value of $\ln (2)$.",  # labels and titles in the graphs
                  r"$ \left|  \textrm{Error}  \right| $", "The absolute error as the number of iterations increases"]
        plot_data(results, titles)  # plots the data sets
        time.sleep(10)
    except:  # if it raises an error, it defaults to normal text
        plt.close()  # resets the matplotlib environment
        print("Error - defaulting to normal text")
        titles = [r"Numerical ln (2)", r"Analytical ln (2)", r"Numerical approximations for the value of ln (2).",
                  r"|Error|", "The absolute error as the number of iterations increases"]  # updates the titles so that
        # don't use latex.
        plt.rc('text', usetex=False)  # Tells matplotlib not to use latex.
        plt.rc('font', family='serif')
        plot_data(results, titles)  # plots the data

