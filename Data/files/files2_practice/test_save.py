# Import os which will be used to check for and delete files.
import os

# Answer questions function which takes no parameters.
def answer_questions():
  # The function firstly creates a dict, this is where information
  # about the characters will be stored.
  answers = {}
  question_list = [("What is the characters name?", "name"), 
                   ("What is the characters health?", "health"), 
                   ("What is the characters defence?", "defence"), 
                   ("What is the characters stamina?", "stamina"), 
                   ("What is the characters weapon?", "weapon")]

  # I put the questions in a list of tuples, meaning we can
  # add an associated value to the questions instead of the
  # large question itself.

  # Now, we loop through the list and take the users input, this
  # along with the associated value are added to the dict.
  for question in question_list:
    if (question == question_list[1] or question == question_list[3]):
      answer = int(input(question[0] + "\n"))  
    else:
      answer = input(question[0] + "\n")
    
    answers[question[1]]=answer

  # Next, we use the get function to go into the dict and get the
  # name of the character.
  # If it equals 0 (the number used to exit deleting characters) we
  # discard it, else we call the generate name directory function
  # and then the save answer function.
  name = answers.get("name")
  if (name == "0"):
    print("This name is blocked as the character would be impossible to delete, returning to menu.")
    return
  directory = generate_name_dir(name)
  save_answers(answers, directory)

# The generate name directory takes in the name of the character
# and returns an appropriate file directory for them.
def generate_name_dir(name):
  save_dir = "Data/files/files2_practice/people/" + (name + ".txt")
  return save_dir

# The save answers function takes in the answers dict and the
# generated character directory.
def save_answers(answers, character_directory):
  
  # We firstly check to see if there's already a character in the
  # directory with this name, if there is we allow the user to either
  # replace the character or go back to the main menu.
  if (os.path.isfile(character_directory) == True):
    while True:
      choice = int(input("The character already exists, what do you want to do?\n1. Replace the character\n0. Go back to the menu\n"))

      # Create the file and write the data from the dict in the
      # correct format.
      if (choice == 1):
        with open(character_directory, "w") as file:
          for data in answers.items():
            file.write("{}={}\n".format(data[0], data[1]))
          print("Character created at {}".format(character_directory))
          return

      elif (choice == 0):
        return

      else:
        print("Not an option.")

# The view answers function takes no parameters and is used to
# view the stored characters.
def view_answers():
  choosing = True
  while (choosing == True):
    choice = int(input("Do you want to:\n1. View every character\n2. View a specific character\n0. Exit\n"))

    # To view every character, we go to the people folder and then
    # print them all through a loop, the [:-4] section removes the
    # last 4 characters from each name (.txt).
    if (choice == 1):
      print()
      for characters in os.listdir("Data/files/files2_practice/people"):
        print(characters[:-4])
      print()

    # To find a specific character, we ask for the characters name
    # and then call the generate name directory function again.
    elif (choice == 2):
      name = input("Enter the name of the character you want to view:\n")
      directory = generate_name_dir(name)

      # If the file exists we go through its contents and print
      # what's inside.
      if (os.path.isfile(directory) == True):
        print()
        with open(directory) as file:
            print(file.read())

      else:
        print("Couldn't find the character, make sure your input is case sensitive")

    elif (choice == 0):
      choosing = False

# The del answers function runs similarly to the view answers one,
# but instead asks for a name to delete.
def del_answers():
  deleting = True
  
  while (deleting == True):
    name = input("Who do you wish to delete? \n0. Exit)\n")
    directory = generate_name_dir(name)
      
    # If the file exists, it gets deleted and prints which character
    # was deleted.
    if (os.path.isfile(directory) == True):
      os.remove(directory)
      print("Removed {}.".format(name))
      
    elif (name == "0"):
      deleting = False
    
    else:
      print("Couldn't find the character, make sure your input is case sensitive")

# The run function takes no parameters and is used as the menu
# of the program
def run():
  menu_running = True
  
  # Infinitely loop the program in a while loop so it doesn't stop
  # once it reaches the end of a function, only exit if the user
  # inputs 0.
  while (menu_running == True):
    menu_choice = int(input("What do you want to do?\n1. Add a character\n2. View characters\n3. Delete characters\n0. Exit\n"))

    if (menu_choice == 1):
      answer_questions()
    elif (menu_choice == 2):
      view_answers()
    elif (menu_choice == 3):
      del_answers()
    elif (menu_choice == 0):
      menu_running = False
    else:
      print("Not an option")

# Run the program
run()