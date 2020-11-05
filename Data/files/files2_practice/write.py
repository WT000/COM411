def search(file_name):
  print("Searching...")

  sections = []
  books = []

  with open("Data/files/files2_practice/books.txt") as file:
    for line in file:
      line = line.strip()
      
      if (line.startswith("Section")):
        line_parts = line.split(":")
        sections.append(line_parts[1])

      else:
        books.append(line)

    return (sections, books)

def save(new_file, returned_data):
  print("Saving...")

  with open(new_file, "w") as file:
    file.write("Simple way:\n")
    file.write("Sections: {}\n".format(returned_data[0]))
    file.write("Books: {}\n".format(returned_data[1]))
    
    
    file.write("\nHard way:\n")
    file.write("Sections: ")
    for section in returned_data[0]:
      if (section == returned_data[0][-1]):
        file.write(section)
      else:
        file.write(section + ", ")
    
    file.write("\nBooks: ")
    for book in returned_data[1]:
      if (book == returned_data[1][-1]):
        file.write(book)
      else:
        file.write(book + ", ")

def run():
  data = search("Data/files/files2_practice/books.txt")

  save("Data/files/files2_practice/section-books.txt", data)

run()