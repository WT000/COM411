# Ask the user what they've heard and seen
hear = input("What did I hear?\n")
see = input("What did I see?\n")

# Give the user a specific response if the following responses are given
if (hear == "grrr" and see == "two red eyes"):
  print("There is a scary creature. I should get out of here!")

# Generic response
else:
  print("I am a little scared but I will continue.")