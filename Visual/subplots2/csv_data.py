import csv
import matplotlib.pyplot as plt

def read_data():
  with open("Visual/subplots2/temps.csv") as csvfile:
    # Use the csv.reader function to get data from the csv file, 
    # then use the next function to take the headers from the
    # file
    csv_reader = csv.reader(csvfile)
    headers = next(csv_reader)

    # Using an empty dict, use a loop to append the headers as
    # keys, each key will store a list
    data = {}
    for header in headers:
      data[header]=[]

    # Then, for every other line in the file, repeated by the number
    # of headers, we append the data to their appropriate header
    for line in csv_reader:
      for count in range(len(headers)):
        data[headers[count]].append(line[count] + "°")

    # Return the dict
    return data

# Run function which takes no parameters
def run():
  # Firstly, call the read_data function and store its contents
  # in a variable, I use a second variable to get the items in
  # the dict
  data = read_data()
  formatted_data = data.items()

  # Next, using a loop, we find out how many subplots will be needed
  subplots_needed = 0
  for count in range(len(formatted_data)):
    subplots_needed += 1
  
  # Using the variable above, we can dynamically add more subplots
  # if additional data is added to the temps.csv file
  fig, axes = plt.subplots(subplots_needed, 1, sharex="all", sharey="all")
  fig.suptitle("Dynamic Temperature Data")

  # We can do the same for plotting data, a count variable is used
  # to decide which subplot should be plotted to
  count = 0
  for line in formatted_data:
    axes[count].plot(range(1, 8), line[1], "bo-")
    count += 1

  # Finally, I set an x label, make the figure use a tight layout
  # and show the plot
  axes[-1].set_xlabel("Day")

  fig.tight_layout()
  plt.show()

# Run the program
run()