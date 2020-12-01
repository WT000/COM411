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

  # Methods
  def display(self):
    print("I am {}".format(self.name))

  def grow(self):
    self.age += 1

  def eat(self, amount):
    self.energy += amount

    if (self.energy > 100):
      print("I'm full, I can't eat more!")
      self.energy = MAX_ENERGY
    else:
      print("Yum!")

  def move(self, distance):
    self.energy -= distance

    if (self.energy < 0):
      print("I'm too tired to keep walking!")
      self.energy = 0
    else:
      print("That was a nice walk!")

  # Debugging output
  def __repr__(self):
    return "human(name={}, age={}, energy={}".format(self.name, self.age, self.energy)

  # String output
  def __str__(self):
    return "My name is {}, my age is {} and my energy is {}!".format(self.name, self.age, self.energy)

if (__name__ == "__main__"):
  human = Human("Will")
  print(human)

  human.move(101)
  print(human)
  human.eat(100)
  print(human)