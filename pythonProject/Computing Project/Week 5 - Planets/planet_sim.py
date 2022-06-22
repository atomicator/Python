# This program is used to simulate and render the planet system. Both leapfrog and euler methods are used, with the
# change in angular momentum (which should be conserved) was then  plotted as a function of the number of
# iterations, to compare the accuracy of both solutions.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D


G = 100  # The value of G to be used in the simulations
size = 100  # the size of the plot used for the simulation
its = 10000  # the number of iterations used in both simulations
time = 20  # the amount of time that should be simulated
frame_skip = 10  # rendering the animation takes longer than the simulation - this is the amount of frames that should be
# simulated per frame rendered, to make the script run faster.


def length(vector):  # Takes a vector and returns the length
    n = 0
    for i in vector:
        n += i ** 2
    length = np.sqrt(n)
    return length


def cross_product(v1, v2):  # takes two vectors and returns the cross product
    result = np.array((v1[0] * v2[1] - v1[1] * v2[0],
              v1[1] * v2[2] - v1[2] * v2[1],
              v1[2] * v2[0] - v1[0] * v2[2],
              ))
    return result


class Planet(object):  # a class used to store the properties of the planets, and calculate the forces acting on them
    def __init__(self, mass, position, velocity, colour, solar_system):
        self.mass = mass  # the mass of the planet
        self.position = position  # the position of the planet (updates during simulations)
        self.velocity = velocity  # the velocity of the planet (updates during simulations)
        self.acceleration = 0  # the acceleration of the planet (updates during simulations)
        self.colour = colour  # the colour to be plotted on the graph for the planet
        self.solar_system = solar_system  # a reference to the solar system object

    def update_acceleration(self, acceleration):  # updates the acceleration value
        self.acceleration = acceleration

    def calculate_acceleration(self):  # returns the acceleration the planet is currently experiencing
        force = 0  # the force exerted on the planet
        for planet in self.solar_system.planets:  # for each planet
            if planet != self:  # if the planet is not this one
                force += (self.mass * planet.mass * G) / (length(self.position - planet.position) ** 3) * \
                    (self.position - planet.position) * -1  # add the force from the planet to the total
        self.acceleration = force / self.mass
        print(force)
        return self.acceleration

    def update_position(self, delta_t):  # updates the position of the planet
        self.position = self.position + delta_t * self.velocity

    def update_velocity(self, delta_t):  # updates the velocity of the planet
        self.velocity = self.velocity + delta_t * self.acceleration


class SolarSystem(object):  # this is used to store the planet objects and run the simulations
    def __init__(self, g=G):
        self.planets = []  # the planets in the system
        self.initial_planets = []  # the inital conditions of the system (not planet objects)
        self.G = g
        self.euler_results = None  # The results of the respective simulations
        self.leapfrog_results = None

    def set_initial_planets(self, set_up):
        self.initial_planets = set_up  # updates the initial conditions for the system

    def reset_system(self):  # resets the system using the initial conditions
        self.planets = []
        for planet in self.initial_planets:
            self.planets.append(Planet(*planet))

    def simulate_euler(self, iterations, time):  # simulates the system using the euler method
        self.reset_system()  # resets the system
        results = []  # the position and velocity at each frame
        delta_t = time / iterations  # the time between frames
        for n in range(iterations):
            for planet in self.planets:
                planet.calculate_acceleration()  # calculates and updates the acceleration of the planet
            for planet in self.planets:
                planet.update_position(delta_t)  # updates the position and momentum of the planet
                planet.update_velocity(delta_t)  # updates the velocity of the planet
            state = []  # the position and momentum of the planets in this frame
            for planet in self.planets:
                state.append([planet.position, planet.velocity])  # add the planet data to the state
            results.append(state)  # add the state to the results
        results = np.array(results)
        self.euler_results = results

    def simulate_leapfrog(self, iterations, time):
        self.reset_system()  # resets the system
        results = []  # the position and velocity at each frame
        delta_t = time / iterations  # the time between frames
        for n in range(iterations):
            for planet in self.planets:
                planet.update_position(delta_t / 2)  # updates the position
            for planet in self.planets:
                planet.calculate_acceleration()  # calculates the acceleration
                planet.update_velocity(delta_t)  # updates the velocity
            for planet in self.planets:
                planet.update_position(delta_t / 2) # updates the position
            state = []  # stores the position and momentum of the planets in this frame
            for planet in self.planets:
                state.append([planet.position, planet.velocity])  # add the planets data to the state
            results.append(state)  # add the state to the results
        results = np.array(results)
        self.leapfrog_results = results

    def plot_momentum(self):  # This was originally used to plot the momentum, but the way that the particles are
        y_axis = []  # simulated means that the interactions are symmetric, and the only changes are caused by rounding
        x_axis = np.linspace(0, time, its)  # errors. The method below uses angular momentum, which has a much better
        for state in self.euler_results:  # result
            m = 0
            for planet in self.planets:
                print(state[self.planets.index(planet)])
                m += planet.mass * state[self.planets.index(planet)][1]
                print(m)
            y_axis.append(length(m))
        y_axis = np.array(y_axis)
        for i in range(len(y_axis)):
            print(y_axis[i], y_axis[0])
            y_axis[i] = (y_axis[i] - y_axis[0]) / y_axis[0]
        plt.clf()
        plt.plot(x_axis, y_axis)
        plt.show()

    def plot_angular_momentum(self):  # plots the angular momentum for the euler and leapfrog simulations
        euler_sim = []  # the angular momentum for the euler simulation
        leapfrog_sim = []  # the angular momentum for the leapfrog simulation
        x_axis = np.linspace(0, time, its)  # the x-axis for the plots
        plt.show()  # clears any existing plots
        for i in range(its):  # for each iteration
            euler_am = np.array((0, 0, 0))  # the initial values are zero vectors
            leapfrog_am = np.array((0, 0, 0))
            for planet in self.planets:
                euler_am = euler_am + planet.mass * cross_product(self.euler_results[i][self.planets.index(planet)][1],
                                                                  self.euler_results[i][self.planets.index(planet)][0])
                leapfrog_am = leapfrog_am + planet.mass * \
                    cross_product(self.leapfrog_results[i][self.planets.index(planet)][1],
                                  self.leapfrog_results[i][self.planets.index(planet)][0])
                # This adds the value of the angular momentum for each planet to the total for the state
            euler_sim.append(length(euler_am))  # This adds the result to the list (only the magnitude is plotted)
            leapfrog_sim.append(length(leapfrog_am))

        plt.plot(x_axis, euler_sim, label="Euler")  # plots the data
        plt.plot(x_axis, leapfrog_sim, label="Leapfrog")
        print(leapfrog_sim)
        plt.legend()
        plt.xlabel("Title")
        plt.ylabel("Angular momentum")
        plt.title(f"The change in angular momentum for a simulation using {its} iterations")
        plt.show()


class Animation(object):  # used to animate the system
    def __init__(self, solar_system, size):
        self.solar_system = solar_system  # This contains the data from the simulations
        self.fig = plt.figure()
        self.ax = Axes3D(self.fig, auto_add_to_figure=False)
        self.fig.add_axes(self.ax)
        self.size = size
        self.results = None  # The result set to be used when animate is called.

    def set_axis(self):  # sets the limits of the plots
        self.ax.set_xlim((-self.size/2, self.size/2))
        self.ax.set_ylim((- self.size/2, self.size/2))
        self.ax.set_zlim((- self.size / 2, self.size / 2))

    def animate(self, n):  # animates a frame
        self.set_axis()  # updates the axis of the plot
        self.draw_frame(n * frame_skip)  # draws the frame

    def draw_frame(self, n):
        self.ax.clear()  # clears the axis (removing the previous plot)
        self.set_axis()  # sets the axis for the plot
        print(n)
        for planet in self.solar_system.planets:  # for each planet
            self.ax.plot(
                *self.results[n, self.solar_system.planets.index(planet), 0],
                marker="o", markersize=10, color=planet.colour
            )  # plot a point for this planet

    def animate_comparison(self, n):  # this animates both plots on the same graph
        self.set_axis()  # sets the axis for the plot
        self.draw_comparison_frame(n * frame_skip)  # draws the frame

    def draw_comparison_frame(self, n):
        self.ax.clear()  # clears the plot
        self.set_axis()  # sets the axis for the plot
        print(n)
        for planet in self.solar_system.planets:  # for each planet
            self.ax.plot(  # plot the planet in the frame
                *self.solar_system.euler_results[n, self.solar_system.planets.index(planet), 0],
                marker="o", markersize=5, color="blue"
            )

            self.ax.plot(
                *self.solar_system.leapfrog_results[n, self.solar_system.planets.index(planet), 0],
                marker="o", markersize=5, color="red"
            )


s = SolarSystem()  # creates a solar system object
a = Animation(s, size)  # creates an animation object
s.set_initial_planets(((1, np.array((5, 0, 0)), np.array((0, 2, 0)), "red", s),
                       (1, np.array((-5, 0, 0)), np.array((0, -2, 0)), "blue", s),
                       (0.1, np.array((0, 4, 0)), np.array((3, -2, 0)), "green", s)
))  # sets the initial conditions for the solar system
s.reset_system()  # resets the system
s.simulate_euler(its, time)  # run an euler simulation of the system
s.simulate_leapfrog(its, time)  # run a leapfrog simulation of the system
anim = animation.FuncAnimation(a.fig, a.animate_comparison, frames=int(its/frame_skip), interval=100)  # These lines
writer_video = animation.FFMpegWriter(fps=60)  # animate and save the animation
anim.save("planets.mp4", writer=writer_video, dpi=200)
s.plot_angular_momentum()  # Plots thr angular momentum of the system, to gauge the accuracy of the simulation
print("Done")
