from clothingsize import ClothingSize

class Clothing:
  def __init__(self, colour, material, size):
    self.colour = colour
    self.material = material
    self.size = size
  
  def __repr__(self):
    return "clothing=(colour={}, material={}, size={})".format(self.colour, self.material, self.size)

if (__name__ == "__main__"):
  tshirt = Clothing("Purple", "Silk", ClothingSize.MEDIUM)
  print(tshirt)