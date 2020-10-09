# Ask the user to input a phrase
phrase = input("Please enter a phrase:\n")

# Counter
repeated_phrase = 0

# We could have also done phrase_characters = len(phrase) here so we didn't need to keep repeating the calculation

# Create a gap and then repeat Bop for the number of characters in the phrase
print()
while (repeated_phrase < len(phrase)):
  print("Bop ", end="")
  repeated_phrase += 1