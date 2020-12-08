from inhabitant import Inhabitant

class Human(Inhabitant):
  def __init__(self, name="Human", age=0):
    super().__init__()
    self.name = name
    self.age = age

  def display(self):
    print("Hello! My name is {} and I'm a human!".format(self.name))

  def __str__(self):
    return "My name is {} and I'm a human, I'm currently {} with an energy of {}.".format(self.name, self.age, self.energy)

  def __repr__(self):
    return "human=(name={}, age={}, energy={})".format(self.name, self.age, self.energy)

if (__name__ == "__main__"):
  test = Human("John", 74)
  print(test)
  test.move(50)
  test.eat(50)
  test.eat(1)