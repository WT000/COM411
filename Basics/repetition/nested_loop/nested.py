# Ask the user for the amount of rows they want (horizontal)
rows = int(input("How many rows should I have?\n"))

# Then ask the user how many columns they want (vertical)
columns = int(input("How many columns should I have?\n"))

print("\nHere I go:\n")

# Firstly the for loop prints the columns, then starts to print the rows, the empty print function is used to create a new line (without this it wouldn't go down!)
for a in range(0, columns, 1):
  for b in range(0, rows, 1):
    print(":-)", end="")
  print()