# Ask the user how many cables should be avoided
cables_to_avoid = int(input("How many live cables should I avoid?\n"))

# Counter
avoided_cables = 0

# While loop, repeats until avoided_cables reaches cables_to_avoid
while (avoided_cables < cables_to_avoid):
  avoided_cables += 1
  print("Avoiding... Done! {} live cables avoided.".format(avoided_cables))

# Loop completed
print("All live cables have been avoided. We can also print on the same line by doing this:")

counter = 0

while (counter < 5):
  print("Same Line ", end="")
  counter += 1