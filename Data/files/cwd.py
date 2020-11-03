# Import the os module
import os

# cwd function which takes no parameters, firstly it prints the
# working folder and then prints what the folder contains
def cwd():
  # Use os to get the current working directory (getcwd)
  path = os.getcwd()
  print("The current working folder is {}".format(path))

  # Then, we can use the listdir function at the cwd to print what's inside it
  print("The folder contains the following:")
  for data in os.listdir(path):
    print(data)

# Run function which takes no parameters and calls the cwd function
def run():
  print("Processing...")
  cwd()

# Run the program
run()