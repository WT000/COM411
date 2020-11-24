import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, axes = plt.subplots()

def animate(frame):
  axes.set_xlim(0, 720)
  axes.set_ylim(-1, 1)

  x_values = np.arange(0, frame)
  degrees = x_values * (np.pi / 180)
  y_values = np.sin(degrees)

  axes.plot(x_values, y_values, "k")
  print(x_values)
  print(degrees)
  print(y_values)
  print()

def run():
  global fig
  sine_animation = animation.FuncAnimation(fig, animate, frames=720, interval=100)

  plt.show()

run()