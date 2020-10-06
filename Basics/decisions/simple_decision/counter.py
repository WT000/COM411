# Ask the user for three whole numbers.
first_number = int(input("Please enter the first whole number.\n"))
second_number = int(input("Please enter the second whole number.\n"))
third_number = int(input("Please enter the third whole number.\n"))

# Odd and Even counter
odd_numbers = 0
even_numbers = 0

# Work out if the numbers are odd or even
if (first_number % 2 == 0):
  even_numbers += 1
else:
  odd_numbers += 1

if (second_number % 2 == 0):
  even_numbers += 1
else:
  odd_numbers += 1

if (third_number % 2 == 0):
  even_numbers += 1
else:
  odd_numbers +=1

print("There were {} even and {} odd numbers.".format(even_numbers, odd_numbers))