# Ask the user for their favourite colour
first_colour = input("What's your favourite colour?\n")

# Ask questions if the user inputs red
if (first_colour == "red"):
  red_shade = input("Red is an interesting colour, do you prefer light or dark shades of it?\n")
  if (red_shade == "light" or red_shade == "Light"):
    print("Light shades of red look nice!")
  elif (red_shade == "dark" or red_shade == "Dark"):
    print("Dark shades of red are scary...")
  else:
    print("I don't know that shade but I'm sure it's cool!")

# Ask questions if the user inputs purple
elif (first_colour == "purple"):
  purple_response = input("Purple's my favourite colour too! Would you say that other colours are as cool as purple?\n")
  if (purple_response == "yes" or purple_response == "Yes"):
    print("No colours come close to it!")
  elif (purple_response == "no" or purple_response == "No"):
    second_purple_response = input("I agree! We should have a world of only purple, correct?\n")
    if (second_purple_response == "yes" or "Yes"):
      print("You get it!")
    elif (second_purple_response == "no" or "No"):
      print("What?!")
    else:
      print("I don't know what you said, but I hope the answer was close to \"yes\"!")

# Ask the user for other questions and then generate a response
second_colour = input("Do you have another favourite colour?\n")
third_colour = input("...And possibly another favourite colour?\n")

if ((first_colour == "purple" or first_colour == "red") and second_colour == "blue" and third_colour == "black" or third_colour == "red"):
  print("Those are my favourite colours too!")
else:
  print("Those are some cool colours!")

#upper and lowercase can be response.lower()