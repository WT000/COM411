# Import the Inhabitant class which will be used as the super class
from inhabitant import Inhabitant

# When creating the human class, we now have to specify that it's a sub class of the
# Inhabitant class
class Human(Inhabitant):
  def __init__(self, name="Human", age=0):
    # By using super(), we now run the __init__ function inside the inhabitant class, which
    # allows us to run eat() and move() within this class, even though it's not here!
    super().__init__()
    # Once done, we now overwrite the name and age with the ones specified by the user
    self.name = name
    self.age = age

  # Sub class method which only humans can do
  def display(self):
    print("Hello! My name is {} and I'm a human!".format(self.name))

  # Overwrite the __str__ and __repr__ magic methods
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