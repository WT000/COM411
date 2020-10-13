# Identify function that takes no parameters, ask the user what they see and generate an appropriate response
def identify():
  sight = input("What lies before us?\n")

  if (sight.lower() == "a large boulder"):
    print("It's time to run!")
  else:
    print("We will be fine.")

# Call the function
identify()