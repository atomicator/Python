# Collision.py
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import itertools


class Canvas():
    """ This class creates the canvas object."""
    def __init__(self):
        """ With self you can access private attributes of
        the object .
        """
        self.size = 20
        self.blocks = []
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot()

    def add_block(self, block):
        """ Every time a block is created it gets put into
        the array .
        """
        self.blocks.append(block)

    def update_blocks(self):
        """ This method moves and draws all blocks."""
        self.ax.clear()
        for i, block in enumerate(self.blocks):
            block.move()
            block.draw()

    def fix_axes(self) :
        """ The axes would change with each iteration
        otherwise .
        """
        self.ax.set_xlim((- self.size / 2, self.size / 2))
        self.ax.set_ylim((-1, 1))

    def check_collision(self):
        """ This method checks if blocks are colliding."""
        combinations = list(itertools.combinations(range(len(self.blocks)), 2))
        for pair in combinations:
            self.blocks[pair[0]].collide(self.blocks[pair[1]])


class Block(object):
    """ This class creates the block object."""
    def __init__(self, canvas, mass, position=0, velocity=0):
        self.canvas = canvas
        self.mass = mass
        self.position = position
        self.velocity = velocity
        # The block is automatically added to the canvas.
        self.canvas.add_block(self)
        self.color = " black "

    def move(self):
        """ The block is moved based on the velocity."""
        self.position = self.position + self.velocity

    def draw(self):
        """ The method to draw the block.Note : if you don ’t
        specify color of the block the color of each new
        element that is plotted will be randomly assigned .
        """
        self.canvas.ax.plot(self.position, 0, " o ")

    def collide(self, other):
        # Watch out with the threshold, this should
        # be greater than velocity. If, in a single
        # iteration, blocks move relatively more than
        # what is the threshold, the collision might
        # not be triggered.
        if abs(self.position - other.position) < 0.1:
        # The velocity after collision is not modelled
        # correctly. Take a look what happens when
        # particles going in the same direction collide.
        # How to fix that?
            self.velocity *= -1
            other.velocity *= -1
            canvas = Canvas()
            block1 = Block(canvas, mass=1, position=-2, velocity=0.07)
            block2 = Block(canvas, mass=1, position=2, velocity=-0.07)
            block3 = Block(canvas, mass=1, position=4, velocity=-0.05)
            block4 = Block(canvas, mass=1, position=-5, velocity=0.05)

def animate(i):
    """ This controls the animation."""
    print("The frame is : ", i)
    canvas.update_blocks()
    canvas.check_collision()
    canvas.fix_axes()

# This calls the animate function and creates animation.
anim = animation.FuncAnimation (canvas.fig, animate, frames =500, interval =10)
# This prepares the writer for the animation.
writervideo = animation.FFMpegWriter(fps=60)
# This saves the animation.
anim.save(" blocks_animation.mp4 ", writer=writervideo, dpi=200)
