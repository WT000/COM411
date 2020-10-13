# Import the randrange function from random
from random import randrange

def minimum_number():
  # Ask the user for a minimum number
  minimum = int(input("Please enter the minimum value: "))
  return minimum
  
def maximum_number():
  # Ask the user for a maximum number
  maximum = int(input("Please enter the maximum value: "))
  return maximum

def play_guess_the_number():
  # Call the number input functions and store what the user enters
  minimum = minimum_number()
  maximum = maximum_number()

  # Generate the number and ask the user to pick a number
  random_number = randrange(minimum, maximum, 1)
  picked_number = int(input("I am thinking of a number between {} and {}. Can you guess what it is?\n".format(minimum, maximum)))

  # Loop until the user guesses the correct number
  while (picked_number != random_number):
    if (picked_number < random_number):
      print("Your guess is too low.")
    elif (picked_number > random_number):
      print("Your guess is too high")
    elif (picked_number == random_number):
      break
    picked_number = int(input("Try again:\n"))
  
  # Repeat the game if the user wants to play again, stop if otherwise
  finish = input("Do you want to play again? (yes or no)\n")
  if (finish.lower() == "yes"):
    play_guess_the_number()
  else:
    print("It was fun playing with you!")

# Start the game
play_guess_the_number()