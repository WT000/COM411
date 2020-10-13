# Listen function with 0 parameters, it should ask the user to enter a sound and print a response with it
def listen():
  sound = input("What sound did I hear?\n")
  print("That was a loud {}!".format(sound))

# Call the function
listen()