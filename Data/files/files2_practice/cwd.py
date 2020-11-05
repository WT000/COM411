import os

def cwd():
  print("The current working idrectory is {}".format(os.getcwd()))

  print("The directory contains the following:")
  for item in os.listdir():
    print(item)

def run():
  print("Processing...")
  cwd()

run()