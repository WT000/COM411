# Import os to use specific functions
import os

# Search function which includes one parameter, that being
# the directory of a file
def search(fileDirectory):
  # Print the working directory and what's inside it
  print("The current working directory is: {}".format(os.getcwd()))
  
  print("And what's in the working directory is:")
  for data in os.listdir():
    print(data)
  
  # In a new section, go through the txt file and print every line
  # inside it
  print()
  print("Searching...")
  with open(fileDirectory) as file:
    for line in file:
      print("Looked in {}".format(line[:-1]))
      print("Looked in {}".format(line), end="")
    print()
  
  # or this could go inside
  #lines = file.read().split("\n")
  #for line in lines:
    #print(line)

# Run function which calls the search function with a directory
def run():
  search("Data/files/txt/locations.txt")

# Run the program
run()