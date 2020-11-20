# Import matplotlib for plotting data
import matplotlib.pyplot as plt

# Read data function which takes one parameter, the
# file path of a file.
def read_data(file_path):
  # Open the file and put its data into a list which
  # is returned
  with open(file_path) as file:
    temp_data = []
    next(file)
    
    for line in file:
      line = line.strip()
      temp_data.append(int(line))
    
    return temp_data

# Run function which takes no parameters
def run():
  # Firstly, we read the data and store it in a
  # variable
  data = read_data("Visual/subplots2/temps.txt")

  # Next, we create the horizontally placed subplots
  # and give the figure a title
  fig, axes = plt.subplots(1, 2, sharex="all")
  fig.suptitle("Temperature Data")

  # This creates a line graph of the data...
  axes[0].plot(range(1, 8), data, "bo-")
  axes[0].set_xlabel("Days")
  axes[0].set_ylabel("Temperature")

  # Whilst this creates a bar graph of the data,
  # meaning viewers can see the data in different
  # ways
  axes[1].bar(range(1, 8), data)
  axes[1].set_xlabel("Days")
  axes[1].set_ylabel("Temperature")

  # Finally, we use tight_layout on the figure to
  # improve the formatting and then show the finished
  # subplots
  fig.tight_layout()
  plt.show()

# Run the program
run()