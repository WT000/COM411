# Import the required matplotlib lib's, though we don't need numpy
# for this exercise
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create the global variables, we'll be accessing the squares
# variable in a function
fig, axes = plt.subplots()
squares = []

def init():
  # Specify that we're altering a global variable and then append
  # the different dicts to the squares list. Remember that each
  # dict pair (x and y) will be stored at an index number as it's
  # being appended to a list
  global squares
  squares.append({"x":[3, 3, 4, 4, 3], "y":[3, 4, 4, 3, 3]})

  squares.append({"x":[2, 2, 5, 5, 2], "y":[2, 5, 5, 2, 2]})

  squares.append({"x":[1, 1, 6, 6, 1], "y":[1, 6, 6, 1, 1]})

def animate(frame):
  # Refresh the squares each time to avoid overlap
  axes.cla()

  # We could maybe use min to get lowest value, same with max
  axes.set_xlim(0, 7)
  axes.set_ylim(0, 7)

  # To calculate which index to plot, we can get the remainder from
  # the number of the frame when dividing it by the length of 
  # the squares list
  index = frame % len(squares)
  axes.plot(squares[index]["x"], squares[index]["y"])

def run():
  global fig
  square_animation = animation.FuncAnimation(fig, animate, frames=3, init_func=init, interval=500)

  plt.show()

# Run the program
run()

#ani.save
#fig.save