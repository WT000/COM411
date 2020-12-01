# Human class
class Human:

  # Class attribute
  MAX_ENERGY = 100

  # Initialiser
  def __init__(self, name="Human", age=0):
    # Instance attributes
    self.name = name
    self.age = age
    self.energy = Human.MAX_ENERGY

  # Methods
  def display(self):
    print("I am {}".format(self.name))

  def grow(self):
    self.age += 1

  def eat(self, amount):
    temp = self.energy + amount
    # or if (amount + self.energy > MAX_ENERGY)
    if (temp > 100):
      print("I'm full, I can't eat more!")
      self.energy = 100
    else:
      self.energy = temp
      print("Yum!")

  def move(self, distance):
    temp = self.energy - distance

    if (temp < 0):
      print("I'm too tired to keep walking!")
      self.energy = 0
    else:
      self.energy = temp
      print("That was a nice walk!")

  # Debugging output
  def __repr__(self):
    return "human(name={}, age={}, energy={})".format(self.name, self.age, self.energy)

  # String output
  def __str__(self):
    return self.name
    
if (__name__ == "__main__"):
  human = Human("Will")
  print(human)

  human.move(101)
  print(human)
  human.eat(100)
  print(human)
  print(repr(human))