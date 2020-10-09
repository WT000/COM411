# Ask the user for a sequence and then get the marker used within it
user_sequence = input("Please enter a sequence:\n")
marker = input("\nPlease enter the marker in the sequence:\n")

# Control variables
mark_count = -1
space = -1

# Here, the loop will go through each character in the inputted sequence. Once we reach the users inputted marker, mark_count becomes 0, meaning it can now start adding to the spaces.
for character in user_sequence:
  if (character == marker):
    mark_count += 1
    if (mark_count >= 1):
      break
      # Now that mark_count has been reached again, we can break the loop and make the program a bit more efficient
  if (mark_count == 0):
    space += 1

# End result
print("\nThe distance between the markers is {}".format(space))

print("This could also be done through:")
is_counting = False
counter = 0

for character in user_sequence:
  if (character == marker and is_counting == False):
    print("Found first marker")
    is_counting = True
  elif (character != marker and is_counting == True):
    counter += 1
  elif (character == marker and is_counting == True):
    print("Found last marker")
    break

print(counter)