# Ask the user for an amount of mountains
mountains = int(input("How many mountains should I display?\n"))
print("Displaying...")

# For loop, from 0 to the inputted value in steps of 1
for i in range(0, mountains, 1):
  print("^")

# Completed loop(s)
print("Done!")