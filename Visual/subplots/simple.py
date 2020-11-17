# Importing the pyplot module from matplotlib
import matplotlib.pyplot as plt

# Read data function which takes one parameter, the file path of the data
def read_data(file_path):
  # Read the file and append the data to a list which is then returned out of
  # the program
  with open(file_path) as file:
    data = []
    
    for line in file:
      line = float(line.strip())
      data.append(line)
    
    return data

# Run function which takes no parameters
def run():
  # Call the read data function and store it in a data variable
  data = read_data("Visual/subplots/temps.txt")

  # Create the subplots which share the same x axis
  fig, axs = plt.subplots(1, 2, sharex="all")

  # Figure title
  fig.suptitle("Temperature Data")
  
  # Plot the two pieces of data in different formats
  axs[0].plot(range(1, 8), data, "bo-")
  axs[1].bar(range(1, 8), data)
  plt.tight_layout()
  
  # Show the plot now that it's created
  plt.show()

# Run the program
run()