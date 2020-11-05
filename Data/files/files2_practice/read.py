def search(file_name):
  print("Searching...")

  with open(file_name) as file:
    for line in file:
      line = line.strip()
      print("Looked in {}".format(line))
    print("...Done!\n")

  with open(file_name) as file:
    print("This reads a singular line:")
    print("Looked in {}".format(file.readline()))

  with open(file_name) as file:
    print("This will read all lines:")
    print(file.read())

  with open(file_name) as file:
    print("\nThis will turn all the lines into a list:")
    print(file.readlines())

def run():
  search("Data/files/files2_practice/locations.txt")

run()