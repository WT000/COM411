# Import pyplot, animation and Numpy, Numpy will be used for
# calulcations on the sine plot
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create the  figure and axes in the MAIN program, these will be
# referenced as global variables
fig, axes = plt.subplots()

# The animate function takes one paramter, that being the current
# frame number
def animate(frame):
  # Firstly, we set the x limit to the total amount of frames, then
  # we set the y limit to be -1 to 1
  axes.set_xlim(0, 720)
  axes.set_ylim(-1, 1)

  # Then, we need to calculate the sine values. To do this, we firstly
  # generate a list from 0 to the current frame. These will be the x
  # values
  # To get the y values, we then multiply this list by pi / 180 and
  # then use the np.sin function on the result of this calculation,
  # the returned value will be the y value
  x_values = np.arange(0, frame)
  y_values = np.sin(x_values * (np.pi / 180))

  axes.plot(x_values, y_values, "k")

# Run function which takes no parameters
def run():
  # Like the previous programs, we specify that fig is a global
  # variable and use this for the animation, then we set the frames
  # to 720 with an interval of 100 milliseconds and then show
  # the fig
  global fig
  sine_animation = animation.FuncAnimation(fig, animate, frames=720, interval=100)

  plt.show()

# Run the program
run()