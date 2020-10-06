# Ask the user for the first and second number
first_number = int(input("Please enter the first number.\n"))
second_number = int(input("Please enter the second number.\n"))

# Use an if, elif and else statement to generate an appropriate result
if (first_number < second_number):
  print("The first number is the smallest.")
elif (second_number < first_number):
  print("The second number is the smallest.")
else:
  print("Both are equal!")