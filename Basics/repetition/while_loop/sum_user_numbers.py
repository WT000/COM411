# Ask the user how many numbers should be summed up
numbers_to_sum = int(input("How many numbers should I sum up?\n"))

# Control variables
numbers_added = 0
while_input = 0
total = 0

# Ask the user to input a number on each loop, this number is then added to the total which is outputted at the end
while (numbers_added < numbers_to_sum):
  while_input = int(input("Please enter number {} of {}\n".format(numbers_added+1, numbers_to_sum)))
  total += while_input
  numbers_added += 1

# Result
print("The answer is {}".format(total))