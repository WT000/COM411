def search(fileName):
  print("Searching...")
  data = {}

  with open(fileName) as file: 
    
  
  print("Done!")
  return data

def run():
  data = search("Data/files/txt/books.txt")

run()