# Search function nwhich has 1 parameter, that being the files directory
def search(fileDirectory):
  print("Searching...")
  sections = []
  books = []

  # Open the file in the directory and go through each line, append each
  # item to the right list and return in a tuple
  with open(fileDirectory) as file:
    for line in file:
      line = line.strip()
      
      if (line.startswith("Section")):
        section = line.split(":")
        sections.append(section[1])
      else:
        books.append(line)

    print("Done!")
    return ((sections, books))

# Save function which takes a (hopefully new) file directory and the data
# returned from the search function
def save(fileName, data):
  print("Saving...")

  # Write the sections and books in seperate lines of the txt file,
  # it will stop adding comma's when it hits the final entry in the
  # section / books lists in the tuple
  with open(fileName, "w") as file:
    file.write("Sections: ")
    for section in data[0]:
      if (section != data[0][-1]):
        file.write("{}, ".format(section))
      else:
        file.write("{} ".format(section))

    file.write("\nBooks: ")
    for book in data[1]:
      if (book != data[1][-1]):
        file.write("{}, ".format(book))
      else:
        file.write("{} ".format(book))

    print("Done")

# Run function which takes no parameters, it firstly searches a txt file
# for data and then writes a sorted version
def run():
  data = search("Data/files/txt/books.txt")
  save("Data/files/txt/section-books.txt", data)

# Run the program
run()