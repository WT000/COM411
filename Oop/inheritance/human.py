# Import the Inhabitant class which will be used as the super class
from inhabitant import Inhabitant
from clothing import Clothing
from clothingsize import ClothingSize

# When creating the human class, we now have to specify that it's a sub class of the
# Inhabitant class
class Human(Inhabitant):
  def __init__(self, name="Human", age=0):
    # By using super(), we now run the __init__ function inside the inhabitant class, which
    # allows us to run eat() and move() within this class, even though it's not here!
    super().__init__(name, age)
    # Once done, we now overwrite the name and age with the ones specified by the user

    self.clothing = []

  # Sub class method which only humans can do
  def display(self):
    print("Hello! My name is {} and I'm a human!".format(self.name))

  def speak(self):
    print("I am human!")

  def dress(self, clothes):
    self.clothing.append(clothes)

  def undress(self, clothes):
    self.clothing.remove(clothes)

  # Overwrite the __repr__ magic method, __str__ is fine

  def __repr__(self):
    return "human=(name={}, age={}, energy={}, clothing={})".format(self.name, self.age, self.energy, self.clothing)

if (__name__ == "__main__"):
  test = Human("John", 74)

  tshirt = Clothing("Purple", "Silk", ClothingSize.LARGE)
  test.dress(tshirt)
  print(repr(test))
  test.undress(tshirt)
  print(repr(test))