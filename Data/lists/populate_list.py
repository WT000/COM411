# Directions function that creates the list and returns it
def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

# Menu function that asks the user to choose a direction
def menu():
  print("Please select a direction:")
  directions_list = directions()
  
  # Print all the items in the list with their index
  for index in range(len(directions_list)):
    print("{}: {}".format(index, directions_list[index]))
  
  # Keep users in an infinite loop until they choose a direction
  choosing = True
  
  while (choosing == True):
    chosen_direction = int(input("Choose a direction: "))
    if (chosen_direction < 4 and chosen_direction > -1):
      return directions_list[chosen_direction]
      break
    else:
      print("Invalid number.")

# Run the menu function 5 times to add directions to the route list
def run():
  route = []
  print("Working out escape route...")
  
  for count in range(5):
    route.append(menu())
  print("Escape route: {}".format(route))

# Run the program
run()