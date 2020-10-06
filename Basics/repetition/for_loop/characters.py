# Ask the user for an input
markings = input("What strange markings do you see?\n")
print("\nIdentifying...\n")

# Use a for loop to go through the word, taking each character out of the text and displaying it seperately.
for character in range(0, len(markings), 1):
  print("index {}: ".format(character) + markings[character])

# Finished loop
print("\nDone!")