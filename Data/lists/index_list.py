# Movements function to create the list
def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return path

# Run function that calls the movement function and then
# loops through it appropriately.
def run():
  print("Moving...")
  movement = movements()

  for count in range(len(movement)):
    if (count % 2 == 0): # This makes it print the right amount (4)
      print("{} for {} steps".format(movement[count], movement[count+1]))

# Call the function
run()