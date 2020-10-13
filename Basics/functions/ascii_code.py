# Start the program and ask for a single character
print("Program Started!")
character = input("Please enter a standard character:\n")

# Check that a single letter has been entered and print the ASCII code, else display an error message
if ((len(character) > 1) or (len(character) == 0)):
  print("ERROR: enter a SINGLE character.")
else:
  print(ord(character))