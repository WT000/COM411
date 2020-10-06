# Ask the user for the direction
direction = input("Towards which direction should I paint (up, down, left or right)?\n")

# Output a response based on user input
if (direction == "up"):
  print("I am painting in the upward direction!")
elif (direction == "down"):
  print("I am painting in the downward direction!")
elif (direction == "left"):
  print("I am painting in the leftward direction!")
elif (direction == "right"):
  print("I am painting in the rightward direction!")
else:
  print("I don't know what direction that is.")