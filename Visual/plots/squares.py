# Import matplotlib to visualise data
import matplotlib.pyplot as plt

# Small square function which draws a small red square with
# dashed lines and circular points
def small():
  x_list = [3, 3, 4, 4, 3]
  y_list = [3, 4, 4, 3, 3]

  plt.plot(x_list, y_list, "ro--")

# Medium square function which draws a medium green square with
# dashed lines and square points
def medium():
  x_list = [2, 2, 5, 5, 2]
  y_list = [2, 5, 5, 2, 2]

  plt.plot(x_list, y_list, "gs--")

# Large square function which draws a large blue square with
# solid lines and pentagon points
def large():
  x_list = [1, 1, 6, 6, 1]
  y_list = [1, 6, 6, 1, 1]

  plt.plot(x_list, y_list, "bp-")

# Run function which takes no parameters, it calls each function
# and then shows the end resulf of all the graphs combined
def run():
  small()
  medium()
  large()
  plt.show()

# Run the program
run()