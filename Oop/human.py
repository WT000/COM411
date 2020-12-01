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

  # Debugging output
  def __repr__(self):
    return "human(name={}, age={}, energy={}".format(self.name, self.age, self.energy)

  # String output
  def __str__(self):
    return "My name is {}, my age is {} and my energy is {}!".format(self.name, self.age, self.energy)

if (__name__ == "__main__"):
  human = Human("Will")
  human.display()
  print(human)