import matplotlib.pyplot as plt
import random

def read():
  paths = {}

  # First choice
  choosing = True
  while (choosing == True):
    possible_options = [":", "--", "-"]
    
    type_of_line = input("What type of line would you like? Dotted (:), dashed (--) or solid(-)?\n") 

    if (type_of_line not in possible_options):
      print("Not an option.")
    else:
      choosing = False
      paths["type_of_line"]=type_of_line

  # Second choice
  choosing = True
  while (choosing == True):
    possible_options = ["r", "g", "b"]
    
    colour_of_line = input("What colour do you want the line to be? Red (r), green (g) or blue (b)?\n")

    if (colour_of_line not in possible_options):
      print("Not an option.")
    else:
      choosing = False
      paths["colour_of_line"]=colour_of_line

  # Third choice
  choosing = True
  while (choosing == True):
    possible_options = ["o", "s", "^"]

    shape_of_point = input("What shape do you want each point to be? A circle (o), square (s) or triangle (^)?\n")

    if (shape_of_point not in possible_options):
      print("Not an option.")
    else:
      choosing = False
      paths["shape_of_point"]=shape_of_point
  
  return paths

def generate():
  no_lines = int(input("How many lines would you like to display?\n"))

  for count in range(no_lines):
    print("Configuring line {}...".format(count+1))
    data = read()
    x_list = random.sample(range(0, 6), 6)
    y_list = random.sample(range(0, 6), 6)
    plt.plot(x_list, y_list, "{}{}{}".format(data["type_of_line"], data["colour_of_line"], data["shape_of_point"]))
  plt.show()

def run():
  print("Running...")
  generate()
  print("Done!")

run()