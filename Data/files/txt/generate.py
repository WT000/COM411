# Search function which takes one parameter, that being the
# directory of the file to search for
def search(fileName):
  print("Searching...")
  
  # Create an empty dict
  data = {}

  # Open the file for reading (no arguments needed)
  with open(fileName) as file: 
    for line in file:
      line = line.strip()

      # If a line startswith with "Section", split at : and
      # make the variable equal the name of the section
      # (located in the the list which .split creates)
      if (line.startswith("Section")):
        section = line.split(":")
        section = section[1]

      # If it doesn't start with section it's a book, if
      # the section doesn't exist add it and the stored
      # section and book to the dict, else append the
      # new book if the section already exists
      else:
        if (section in data):
          data[section].append(line)
        else:
          data[section]=[line]

    # Return the dict to the main program
    return data

# Run function which takes no parameters
def run():
  data = search("Data/files/txt/books.txt")

  # This uses a nested loop, it loops through the number of keys
  # (sections) in the dict and then loops through the number of
  # books (values) inside the associated list
  with open("Data/files/txt/generated.csv", "w") as file:
    for section in data.items():
      for book in section[1]:
        file.write("{},{}".format(section[0], book + "\n"))
  
  print("Done!")

# Run the program
run()