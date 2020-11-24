# Import the matplotlib pyplot and animation lib's
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create the  figure and axes in the MAIN program, these will be
# referenced as global variables
fig, axes = plt.subplots()

# Animate function which is called on each frame of the animation
def animate(frame):
  # If the frame is 0, it means the animation is starting again,
  # clear the plots
  if (frame == 0):
    axes.cla()

  # Set the xlim and ylim from 0 to 10 to ensure the animation doesn't
  # go off screen, then plot the points
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