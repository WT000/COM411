# Ask the user what adventure Beep should take
adventure = input("What type of adventure should I have?\n")

# Output an appropriate response based on multiple inputs
if (adventure == "scary" or adventure == "short"):
  print("Entering the dark forest!")
elif (adventure == "safe" or adventure == "long"):
  print("Taking the safe route!")

# Generic response
else:
  print("Not sure which route to take.")