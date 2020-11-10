# Importing the matplotlib module to visualise data
import matplotlib.pyplot as plt

# Display function which takes two parameters, the x list and y list
def display(x_list, y_list):
  plt.plot(x_list, y_list)
  plt.xlabel("x border")
  plt.ylabel("y border")
  plt.show()

# Run function which takes no parameters, it asks the user to
# enter how many values they wish to add, then the program adds them
# all up
def run():
  total_loop = int(input("How many X/Y values do you wish to add?\n"))

  x_list = []
  y_list = []

  for count in range(total_loop):
    print("Coordinate {}:".format(count+1))
    x_value = int(input("Enter a number for the x coordinate: "))
    y_value = int(input("Enter a number for the y coordinate: "))
    x_list.append(x_value)
    y_list.append(y_value)

  print("Processing...")
  display(x_list, y_list)

run()