# Tell the user that a calculation is being done
print("Calculating the sum of the first 100 numbers...")

# Counter
number_loop = 0
final_number = 0

# Use a while loop to add final_number by the current loop number, this repeats for every loop
while (number_loop < 101):
  final_number += number_loop
  number_loop += 1

# Final result
print("...Done! The answer is {}".format(final_number))