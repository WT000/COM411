def search(file_name):
  print("Searching...")
  data = {}

  with open("Data/examrevision/week6/books.txt") as file:
    for line in file:
      line = line.strip()

      if (line.startswith("Section")):
        parts = line.split(":")
        key = parts[1]

      else:
        if (key in data):
          data[key].append(line)
        else:
          data[key]=[line]

    print("Done!")
    return data

def run():
  data = search("Data/examrevision/week6/books.txt")
 
  with open("Data/examrevision/week6/generated.csv", "w") as file:
    for section in data.items():
      for book in section[1]:
        file.write("{},{}\n".format(section[0], book))

run()