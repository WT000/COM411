# Import the required lib's
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create the figure and the axes in the global program
fig, axes = plt.subplots()

# Animate function which takes the current frame as the parameter
def animate(frame):
  # The x limit is now going from 0 to 2*pi, meaning it'll fit the entire sine wave
  # instead of having to draw it on a solid axes
  axes.cla()
  axes.set_xlim(0, 2*np.pi)
  axes.set_ylim(-1, 1)

  # In the Numpy array, we now generate them from 0 to 2*pi (the same length as the
  # figure), but in steps of 0.01.
  # Then, the y value is set to the x values plus the frame number divided by 50.
  x_values = np.arange(0, 2*np.pi, 0.01)
  y_values = np.sin(x_values + frame / 50)

  axes.plot(x_values, y_values, "k", linewidth=5)

# Run function which takes no parameter
def run():
  # Specify that fig is a global variable and then run the animation
  # Specify that fig is a global variable and the
  global fig
  sine_animation = animation.FuncAnimation(fig, animate, frames=720, interval=100)

  plt.show()

# Run the program
run()