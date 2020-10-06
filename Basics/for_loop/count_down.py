# Ask the user for the distance from the cave in steps
distance = int(input("How far are we from the cave?\n"))

# Loop downwards from the users inputted value
for steps in range(distance, 0, -1):
  print("{} steps remaining...".format(steps))

# End of the loop
print("We have reached the cave!")