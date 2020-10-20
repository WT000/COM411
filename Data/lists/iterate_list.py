def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print("Please enter a direction:")
  direction_list = directions()

  for count in range(len(direction_list)):
    print("{}: {}".format(count, direction_list[count]))

def run():
  menu()

run()