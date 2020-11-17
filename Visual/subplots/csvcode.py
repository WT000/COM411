# Importing the modules for pyplot and csv
import matplotlib.pyplot as plt
import csv

# The read data function takes no parameters, it firstly 
# opens the data.csv file and takes the headers from the top
# row, using these it makes a dict from them and appends the
# remaining values to them
def read_data():
  with open("Visual/subplots/data.csv") as csvfile:
    csv_data = csv.reader(csvfile)

    headers = next(csv_data)

    data = {
      headers[0]: [],
      headers[1]: []
    }
    
    for line in csv_data:
      data[headers[0]].append(line[0])
      data[headers[1]].append(line[1])
    
    return data

# Run function which takes no parameters, it firstly collects the
# data from the read_data function and then plots the data next
# to each other.
def run():
  data = read_data()

  fig, axes = plt.subplots(2, 1, sharey="all")

  fig.suptitle("Temperature Data")

  axes[0].plot(range(1, 8), data.get("week1"), "bo-")
  axes[0].set_xlabel("Week 1")
  axes[0].set_ylabel("Temp")

  axes[1].plot(range(1, 8), data.get("week2"), "bo-")
  axes[1].set_xlabel("Week 2")
  axes[1].set_ylabel("Temp")
  
  fig.tight_layout()
  
  plt.show()

# Run the program
run()

# Additional lecture notes #

# to stack vertically, use 2, 1 (opposite of last time)
# sharex all when specifying the subplots
# use global variables or a loop for dict to plot on the subplots 
# when using a global variable, use global header inside the function
# plt.tight_layout
# next(csv reader) takes the values and goes to next line