# Ladder function with steps parameter, it will display an ASCII ladder (steps) amount of times
def display_ladder(steps):
  for i in range(0, steps, 1):
    print("| |")
    print("***")
  print("| |")

# Ask the user for how many ladder steps remain
def create_ladder():
  steps = int(input("How many steps remain?\n"))
  display_ladder(steps)

# Call the create_ladder function
create_ladder()