# Ask the user for an int
print("Program started!")
ascii_code = abs(int(input("Please enter an ASCII code: ")))
# abs makes it a whole number

# Check if the input is within the ASCII range (32 - 126) and then convert it, else it will display a suitable error message
# could also be done by number => 36 and number <= 126
if (ascii_code in range(32, 126)):
  print("The character represented by the ASCII code {} is: {}".format(ascii_code, chr(ascii_code)))
else:
  print("ERROR: Please enter a number between 32 and 126.")

# Complete the program.
print("Program ended!")