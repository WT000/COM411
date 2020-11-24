# Import the matplotlib pyplot and animation lib's
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create the  figure and axes in the MAIN program, these will be
# referenced as global variables
fig, axes = plt.subplots()

# Animate function which is called on each frame of the animation
def animate(frame):
  axes.cla()
  axes.set_xlim(0, 10)
  axes.set_ylim(0, 10)
  axes.plot(frame, frame, "ro")

# Run function which takes no parameters
def run():
  # Use fig from the global program so the program knows we
  # want to use that, then create the animation (10 frames, 1
  # sec interval)
  global fig
  simple_animation = animation.FuncAnimation(fig, animate, frames=10, interval=1000)

  plt.show()

# Run the program
run()