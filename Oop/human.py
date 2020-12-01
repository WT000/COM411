# Human class
class Human:

  # Class attribute
  MAX_ENERGY = 100

  # Initialiser
  def __init__(self, name="Human", age=0, energy=MAX_ENERGY):
    # Instance attributes
    self.name = name
    self.age = age
    self.energy = energy

  # Method
  def display(self):
    print("I am {}".format(self.name))

if (__name__ == "__main__"):
  human = Human("Will")
  human.display()