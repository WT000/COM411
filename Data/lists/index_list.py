# Movements function to create the list
def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return path

# Run function that calls the movement function and then
# loops through it appropriately.
def run():
  print("Moving...")
  movement = movements()

  for index in range(len(movement)):
    if (index % 2 == 0): # This makes it print the right amount (4)
      print("{} for {} steps".format(movement[index], movement[index+1]))
  
  # Or we could do
  print()
  for index in range(0, len(movement), 2):
    print("{} for {} steps".format(movement[index], movement[index+1]))

# Call the function
run()