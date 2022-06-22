import sympy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import random


m1, m2, u1, u2, v1, v2 = sympy.symbols("m1 m2 u1 u2 v1 v2")  # creates constants for use in sympy

size = 10
time = 100  # defining the global constants
frames = 100
fps = 10


class Block(object):  # This stores all information about the blocks and allows them to be updated
    def __init__(self, mass, radius, position, velocity, colour):
        self.position = position  # the position of the block
        self.velocity = velocity  # the velocity of the block
        self.mass = mass  # the mass of the block
        self.radius = radius  # the radius when plotted
        self.colour = colour  # the colour when plotted

    def update_velocity(self, velocity):  # updates the velocity of the block (prevents scope problems)
        self.velocity = velocity

    def move(self, time):  # moves the particle, using the current state a time input
        self.position = self.position + self.velocity * time

    def update_position(self, position):  # updates the position of the particle (prevents scope problems)
        self.position = position


class System(object):  # stores all the references to the blocks and the simulation methods
    def __init__(self, wall_positions):
        self.expression = None  # the expression used to simulate the collisions
        self.derive_expression()  # derives the expressions
        print(self.expression)
        self.blocks = []  # the blocks will be added to this array
        self.simulation_results = None  # the results of the simulation will be added to the array
        self.wall_positions = wall_positions  # stores the positions of the walls

    def block_collision(self, block1, block2):  # takes two block inputs and calculates the velocities after the collision
        initial_speeds = [block1.velocity, block2.velocity]  # the initial speeds of the blocks
        final_speeds = [self.expression[0].subs(m1, block1.mass).subs(m2, block2.mass).subs(u1, initial_speeds[0]).subs(u2, initial_speeds[1])
                        , self.expression[1].subs(m1, block1.mass).subs(m2, block2.mass).subs(u1, initial_speeds[0]).subs(u2, initial_speeds[1])]
        # the final speeds are claulcated by substituting the inital values and the masses of the particles into the derived
        # expressions
        block1.update_velocity(final_speeds[0])  # updates the velocities of the blocks
        block2.update_velocity(final_speeds[1])

    def wall_collision(self, block):  # updates the position of the block when it collides with a wall
        block.update_velocity(block.velocity * -1)

    def derive_expression(self):  # uses sympy to derive an expression for the result after a collsion
        trivial_solutions = [[u1, u2]]
        momentum1 = m1 * u1 + m2 * u2  # expressions for the momentum before and after
        momentum2 = m1 * v1 + m2 * v2
        ke1 = 0.5 * (m1 * u1 ** 2 + m2 * u2 ** 2)  # expressions for the KE before and after
        ke2 = 0.5 * (m1 * v1 ** 2 + m2 * v2 ** 2)

        n = sympy.solve((momentum1 - momentum2), v1)  # conservation of momentum
        solution2 = sympy.solve((ke1 - ke2.subs(v1, n[0])), v2)  # conservation of energy
        solution1 = [sympy.solve((momentum1 - momentum2.subs(v2, solution2[0])), v1),  # calculates the second solution
                     sympy.solve((momentum1 - momentum2.subs(v2, solution2[1])), v1)]  # using the first

        solution = None
        for i in range(len(solution2)):  # for each possible solution
            valid = True
            for trivial_solution in trivial_solutions:  # for each predefined trivial solution
                if trivial_solution[0] == solution1[i] and trivial_solution[1] == solution2[i]:  # if it's trivial
                    valid = False  # the solution is invalid
            if valid:  # if it's not valid
                solution = [solution1[i][0], solution2[i]]  # save the solution
        if (momentum1 - momentum2.subs(v1, solution[0]).subs(v2, solution[1]).simplify() == 0) and \
                (ke1 - ke2.subs(v1, solution[0]).subs(v2, solution[1]).simplify() == 0):  # check that the derived
            print("The equations work")  # solution works (conserves KE and momentum)
        else:
            raise ArithmeticError("The maths does not satisfy the original equations")  # print an error code

        self.expression = solution  # saves the solution

    def add_current_state(self, t):  # saves the current state of the system
        state = []
        for block in self.blocks:  # for each block
            state.append([block.position, block.velocity])  # add the blocks data to the state
        self.simulation_results.append([t, state])  # save the state

    def simulate(self, time):  # simulate the particles
        t = 0  # stores how much time has been simulated
        self.simulation_results = []
        self.add_current_state(t)
        finished = False  # updated when the simulation has finished
        while not finished:  # until the simulation has finished
            if t > time:  # this check is here to prevent address errors later on
                finished = True
            next_collision, time_to_next_collision = self.calculate_next_collision()  # checks for the next collision
            print(next_collision, time_to_next_collision)
            for block in self.blocks:  # for each block
                block.move(time_to_next_collision)  # move the block
            t += time_to_next_collision  # update t
            if next_collision:  # if next collision is not None
                if next_collision[1] == "wall":  # if it will collide with a wall
                 #   self.wall_collision(next_collision[0])  # replaced with different code - the blocks tended to
                    pass  # pass through the walls
                else:
                    self.block_collision(*next_collision)  # collide the two blocks
            for block in self.blocks:  # for each block
                if not (self.wall_positions[0] < block.position < self.wall_positions[1]):  # if it's not between
                    # the two blocks
                    if block.position < 0:  # if it's below the lower wall
                        block.update_position(self.wall_positions[0] + abs(block.position - self.wall_positions[0]))
                        #  move the block to the other side of the wall
                        if block.velocity < 0:  # if it's moving further away
                            block.update_velocity(-1 * block.velocity)  # swap the direction
                    else:  # if the block is above the upper wall
                        block.update_position(self.wall_positions[1] - abs(block.position - self.wall_positions[1]))
                        # move it to the other side of the wall
                        if block.velocity > 0:  # if it's moving away
                            block.update_velocity(-1 * block.velocity)  # swap the direction of the movement
            self.add_current_state(t)  # save the current state of the system

    def calculate_next_collision(self):  # calculates the next collision that will happen
        time_to_next_collision = 0.01  # the maximum time for an iteration
        next_collision = None  # unless a collision occurs in the interval, the collision will be a None object
        for block1 in self.blocks:
            for block2 in self.blocks:
                if block2 != block1:  # if the two blocks are different
                    time_to_collision = (block1.position - block2.position) / (block1.velocity - block2.velocity) * -1
                    # time = distance / velocity
                    if 0 < time_to_collision < time_to_next_collision:  # if the collision will happen first and they're
                        # moving closer
                        time_to_next_collision = time_to_collision  # update the time to next collision
                        next_collision = [block1, block2]  # updates the next collision
        return next_collision, time_to_next_collision   # return the results

    def add_block(self, block):  # add a block to the list
        self.blocks.append(block)

    def add_small_block(self, number, colour):  # adds n "small" blocks to the simulation
        for i in range(number):
            self.add_block(Block(1 + random.random(), 5, -2 - random.random(), 1 + random.random(), colour))

    def add_large_block(self, number, colour):  # adds n "large" blocks to the simulation
        for i in range(number):
            self.add_block(Block(10 + 10 * random.random(), 5, 2 + random.random(), 1 + random.random(), colour))

    def add_piston(self, colour):  # adds a piston to the simulation
        self.add_block(Block(100, 20, 0, 0, colour))

    def plot_ke(self):  # plots the KE for each iteration to see if it's conserved
        time = []  # the x and y variables for the plot
        ke = []

        for result in self.simulation_results:  # for each result
            time.append(result[0])  # add the time to the list
            energy = 0
            for i in range(len(self.blocks)):  # for each particle
                energy += 0.5 * self.blocks[i].mass * result[1][i][1] ** 2  # add its KE
            ke.append(energy)  # adds the total KE to the list

        plt.clf()  # clears the plot
        plt.plot(time, ke)  # plots the KE and time
        plt.show()  # displays the plot


class Animation(object):  # used to animate the system
    def __init__(self, size, system):
        self.fig = plt.figure()
        self.size = size
        self.system = system
        self.results = None  # The result set to be used when animate is called.

    def draw_frame(self, n):
        plt.clf()  # clears the plot
        delta_t = time / frames  # calculates the time interval between frames
        t = delta_t * n  # calculates the the time for the frame being plotted
        searching = True  # updated when it finds the needed result
        n = 0
        print(self.system.simulation_results)
        while searching:
            n += 1
            print(t)
            if t < self.system.simulation_results[n][0]:  # once a result has a value of time higher than the one being
                #  looked at in the frame
                searching = False
                n -= 1

        increment = t - self.system.simulation_results[n][0]  # the amount by which the positions need to be extrapolated
        for a in range(len(self.system.blocks)):  # for each block
            print(a)
            plt.plot([self.system.simulation_results[n][1][a][0] + self.system.simulation_results[n][1][a][1] *
                      increment], [0], marker="o", markersize=self.system.blocks[a].radius,
                     color=self.system.blocks[a].colour)  # plot a circle for the block
        plt.xlim(-self.size/2, self.size/2)
        plt.ylim(-1, 1)
        plt.plot([-self.size / 2] * 2, [-1, 1], "_", color="black")  # adds the walls to the plot
        plt.plot([self.size / 2] * 2, [-1, 1], "_", color="black")
        plt.title(f"The system at t={t}")
        print(n)


if __name__ == "__main__":
    s = System((-5, 5))  # creats a system with walls at +/- 5
    s.add_small_block(5, "red")  # adds 5 small blocks on the left
    s.add_large_block(5, "blue")  # adds 5 large blocks on the right
    s.add_piston("black")  # adds a piston in the centre
    s.simulate(time)  # runs the simulation object
    print(np.array(s.simulation_results))
    a = Animation(size, s)  # creates an animation object
    anim = animation.FuncAnimation(a.fig, a.draw_frame, frames=frames, interval=100)  # These lines
    writer_video = animation.FFMpegWriter(fps=fps)  # animate and save the animation
    anim.save("collisions.mp4", writer=writer_video, dpi=200)
    print("Done")
