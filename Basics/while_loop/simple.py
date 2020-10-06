# Ask the user how many cables should be removed
cables_to_remove = int(input("How many cables should I remove?\n"))

# Counter
cables_removed = 0

# While loop keeps repeating until the amount the user inputted is reached
while (cables_removed < cables_to_remove):
  print("Removed cable")
  cables_removed += 1
print("Removed {} cables.".format(cables_removed))