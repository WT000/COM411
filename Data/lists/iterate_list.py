# Create the list with the desired directions
def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

# Menu function which goes through each index in the list
def menu():
  print("Please enter a direction:") # (won't have functionality)
  direction_list = directions()

  for index in range(len(direction_list)):
    print("{}: {}".format(index, direction_list[index]))

# Function which calls the menu
def run():
  menu()

# Call the run function
run()