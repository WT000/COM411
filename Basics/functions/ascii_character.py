# Ask the user for an int
print("Program started!")
ascii_code = int(input("Please enter an ASCII code:"))

# Check if the input is within the ASCII range (32 - 126) and then convert it, else it will display a suitable error message
if (ascii_code in range(32, 126)):
  print("The character represented by the ASCII code {} is: {}".format(ascii_code, chr(ascii_code)))
else:
  print("ERROR: Please enter a number between 32 and 126.")

# Complete the program.
print("Program ended!")