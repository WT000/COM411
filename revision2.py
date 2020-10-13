# ask the user to input a sequence
sequence = input("Please enter a sequence.\n")

# ask the user to enter the character for the marker
marker = input("Please enter the marker for the sequence.\n")

# work out the distance between the marker, use a for loop with decisions for this
# control variable
marker_counter = 0
distance = 0

# look at each character in the sequence
for character in sequence:
  if (character == marker):
    marker_counter += 1 # if we find the marker, add 1 to the counter
  elif (marker_counter == 1):
    distance += 1 # whilst the counter is at 1, add 1 to distance
    if (distance > 2):
      break # if another marker is found, break the loop

# print the result
print(distance)

# print number 1 to 100 on a new line
for i in range(0, 101, 1):
  if ((i % 3 == 0) and (i % 5 == 0)):
    print("FizzBuzz")
  elif (i % 5 == 0):
    print("Buzz")
  elif (i % 3 == 0):
    print("Fizz")
  else:
    print(i)

# when a multiple of 3 is hit, print fizz instead of the number

# do the same with 5, but make it print buzz

# if we reach a multiple of 3 OR 5, print fizzbuzz