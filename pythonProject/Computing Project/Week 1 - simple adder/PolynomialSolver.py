# PolynomialSolver.py
# A function to solve polynomials. The goal is to plot the polynomial, then locate any zeroes in the function, within a
# defined range. This range can then be integrated over, with a separate option for area. This can be done easily using
# numpy, however this defeats the purpose of the exercise. The polynomials have to have constants in front of the powers 
# of x, and they can be of any order. This means Taylor approximations could be analysed using this software (currently
# set to e^x).

import matplotlib.pyplot as plt  # used to display the graph


def derivative(n):  # returns the derivative at the point being expanded around, using a known expression in terms of n
    value = 1
    return value


def factorial(n):  # returns n!
    if n == 0:
        value = 1
    else:
        value = n
        for i in range(n)[1:]:
            value *= i
    return value


def taylor_terms(terms):  # returns the
    coefficients = []
    for i in range(terms):
        coefficients.append(derivative(i) / factorial(i))
    return coefficients


# Defining the constants used
xrange = [0, 2, 1000]  # The minimum, maximum and number of points used
constant_values = taylor_terms(10)  # The values in front of each power of x, starting from the x ^ 0 th power.
search_iterations = 1000  # The number of iterations used when searching for zeroes / minimums / maximums
print(f"The values of the constants are {constant_values}")


class Main(object):  # used to store global variables and the functions to call when the program is run
    def __init__(self, xrange, constant_values, iterations):
        self.iterations = iterations
        self.x_range = xrange
        self.constant_values = constant_values
        self.integral = 0
        self.area = 0
        self.y_values = []
        self.x_values = []
        self.rough_zeroes = []  # a 2D array, used as the initial estimate
        self.accurate_zeroes = []  # a 1D array, stores the values of the zeroes after the searching algorithm
        self.plot = plt  # creates a plot object
        self.find_values()  # calculates the values of x and y
        wants_to_exit = False
        while not wants_to_exit:
            choice = input("Do you want to:\n1) Look for zeroes in the function\n2) Integrate the function\n3) "
                           "Calculate the area of the function\n4) Plot the function\n5) Exit\n")
            if choice == "1":
                print("looking for zeroes")
                self.zeroes()
            elif choice == "2":
                self.integrate()
            elif choice == "3":
                self.integrate(area=True)
            elif choice == "4":
                self.plot_data()
            elif choice == "5":
                wants_to_exit = True
            else:
                print("Please enter a number from 1 - 4 to select an option")

    def integrate(self, area=False):  # integrates the function. Area means it calculates the area (ensures the function
        total = 0
        width = (self.x_values[-1] - self.x_values[0]) / len(self.x_values)
        for i in range(len(self.x_values) - 1):  # is always above zero):
            x0, x1 = self.x_values[i:i+2]
            if [x0, x1] in self.rough_zeroes:
                zero_num = self.rough_zeroes.index([x0, x1])
                exact_zero = self.accurate_zeroes[zero_num]
                if area:
                    total += abs((exact_zero - x0) * self.find_y(x0) / 2) + abs((- exact_zero + x1) * self.find_y(x0)
                                                                                / 2)
                else:
                    total += (exact_zero - x0) * self.find_y(x0) / 2 + (- exact_zero + x1) * self.find_y(x0) / 2
            else:
                if area:
                    total += abs((self.find_y(x0) + self.find_y(x1)) * width / 2)
                else:
                    total += (self.find_y(x0) + self.find_y(x1)) * width / 2
        if area:
            text = "area"
        else:
            text = "integral"
        print(f"The {text} of this function is {total}")
        return total

    def find_values(self):
        self.calculate_x_values()
        self.calculate_y_values()

    def zeroes(self):
        self.search_for_zeroes()
        self.iterate_zeroes()
        print(f"The accurate values for the zeroes are {self.accurate_zeroes}")

    def calculate_x_values(self):  # creates a list of all the x values
        min_x = self.x_range[0]
        max_x = self.x_range[1]
        length = self.x_range[2]
        step = (max_x - min_x) / length
        for i in range(length):
            self.x_values.append(min_x + step * i)
        return True

    def find_y(self, x):  # calculates y for a given value of x
        y = 0
        i = 0
        while i < len(self.constant_values):
            y += (self.constant_values[i]) * (x ** i)
            i += 1
        return y

    def calculate_y_values(self):  # calculates the values of y for each value of x
        for x in self.x_values:
            self.y_values.append(self.find_y(x))
        return True

    def plot_data(self):  # uses matplotlib to plot the function, using the previously calculated y values
        self.plot.plot(self.x_values, self.y_values, label="Function")
        self.plot.ylabel("f(x)")
        self.plot.legend()
        self.plot.xlabel("x")
        self.plot.title("f(x)")
        self.plot.show()
        return True

    def search_for_zeroes(self):  # searches for zeroes by checking for a change in sign between two consecutive points
        for i in range(len(self.y_values) - 1):
            if (abs(self.y_values[i]) != self.y_values[i]) ^ (abs(self.y_values[i+1]) != self.y_values[i+1]):
                self.rough_zeroes.append([self.x_values[i], self.x_values[i+1]])
        return True

    def iterate_zeroes(self):  # uses a binary search to more accurately find the zero point
        for x0, x1 in self.rough_zeroes:
            x_mid = (x1 + x0) / 2
            y0, y1 = self.find_y(x0), self.find_y(x1)
            for i in range(self.iterations):
                x_mid = (x1 + x0) / 2
                y_mid = self.find_y(x_mid)
                if (abs(y0) != y0) ^ (abs(y_mid) != y_mid):
                    x1 = x_mid
                    y1 = y_mid
                else:
                    x0 = x_mid
                    y0 = y_mid
                if x0 == x1:
                    break
            self.accurate_zeroes.append(x_mid)


if __name__ == "__main__":  # This returns True if the program is run directly, False if the program is imported.
    Main(xrange, constant_values, search_iterations)
