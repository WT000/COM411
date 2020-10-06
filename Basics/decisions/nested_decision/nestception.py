# Ask the user for the location
location = input("Where should I look?\n")

# Ask if the user wants to go in the bedroom, bathroom or lab. Then, ask if they want to go to a specific place in the appropriate rooms, generating a response.
# Bedroom
if (location == "in the bedroom"):
  bedroom_location = input("Where in the bedroom should I look?\n")
  if (bedroom_location == "under the bed"):
    print("Found some shoes but no battery.")
  else:
    print("Found some mess but no battery.")

# Bathroom
elif (location == "in the bathroom"):
  bathroom_location = input("Where in the bathroom should I look?\n")
  if (bathroom_location == "in the bathtub"):
    print("Found a rubber duck but no battery.")
  else:
    print("Found a wet surface but no battery.")

# Lab
elif (location == "in the lab"):
  lab_location = input("Where in the lab should I look?\n")
  if (lab_location == "on the table"):
    print("Yes, I found my battery!")
  else:
    print("Found some tools but no battery.")

# Generic response
else:
  print("I do not know where that is but I will keep looking.")