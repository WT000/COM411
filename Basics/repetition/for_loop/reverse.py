# Ask the user for a phrase
phrase = input("What phrase do you see?\n")
print("\nReversing...\n")

# We firstly use an end"" to make sure everything's on the same line, then we can go through each character from the back by going in increments of -1 and printing what it's on
print("The phrase is: ", end="")
for character in range(len(phrase) - 1, -1, -1):
  print(phrase[character], end="")