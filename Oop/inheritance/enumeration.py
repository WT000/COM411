from enum import Enum

class Sizes(Enum):
  def __init__(self): 
    X_SMALL = 1
    SMALL = 2
    MEDIUM = 3
    LARGE = 4
    X_LARGE = 5

if (__name__ == "__main__"):
  #size can be specified in the __init__
  size = Sizes.LARGE

  print(size)