# Import the Inhabitant class which will be used as the super class
from inhabitant import Inhabitant

# When creating the robot class, we now have to specify that it's a sub class of the
# Inhabitant class
class Robot(Inhabitant):
  LAWS = "Protect, Obey, Survive"
  
  def __init__(self, name="Robot", age=0):
    # By using super(), we now run the __init__ function inside the inhabitant class, which
    # allows us to run eat() and move() within this class, even though it's not here!
    super().__init__(name, age)

  # This method is unique to robots, that being to print the robot laws
  def the_laws(self):
    print(Robot.LAWS)

  # Override the __repr__ magic method, __str__ is fine

  def __repr__(self):
    return "robot=(name={}, age={}, energy={})".format(self.name, self.age, self.energy)

if (__name__ == "__main__"):
  test = Robot("Beep", 3)
  print(test)
  test.move(50)
  test.eat(50)
  test.eat(1)