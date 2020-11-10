# Import matplotlib as plt to visualise data
import matplotlib.pyplot as plt

# Coordinate function which takes no parameters, it simply assk for
# an x coord and y coord which is returned in a tuple
def coordinate():
  x = input("Please enter an x value: ")
  y = input("Please enter a y value: ")

  return (x, y)

# Path function which takes no parameters, it calls the coordinate
# function 4 times and adds the x / y parameters inside the tuples
# to seperate x and y lists. Then, these lists are returned inside
# another list
def path():
  print("Retrieving path...")

  x_values = []
  y_values = []

  for count in range(4):
    data = coordinate()

    x_values.append(data[0])
    y_values.append(data[1])
  
  return [x_values, y_values]

# The run function takes no parameters, it calls the path function
# and makes a red chart with the returned values
def run():
  values = path()

  plt.plot(values[0], values[1], "ro--")
  plt.show()

# Run the program
run()