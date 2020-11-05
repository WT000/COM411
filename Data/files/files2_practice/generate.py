def search(file_name):
  print("Searching...")
  data = {}

  with open(file_name) as file:
    for line in file:
      line = line.strip()
      
      if (line.startswith("Section")):
        section = line.split(":")[1]
      
      else:
        if (section not in data):
          data[section]=[line]
        else:
          data[section].append(line)

  print("Done!")
  return data

def run():
  data = search("Data/files/files2_practice/books.txt")

  with open("Data/files/files2_practice/generated.csv", "w") as file:
    for item in data.items():
      for book in item[1]:
        file.write("{}, {}\n".format(item[0], book))

run()