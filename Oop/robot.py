# This is the Robot class, the blueprint for creating a robot
class Robot:

  # A class attribute, shared by every object
  def the_laws():
    LAWS = "Protect, Obey and Survive"
    print(LAWS)

  # Initialise method which will run whenever the class is called
  # Default values are provided if nothing is given
  def __init__(self, name="Robot", age=0):
    # Attributes of the robot objects
    self.name = name
    self.age = age

  # An additional method which is used to display the name
  def display(self):
    print("I am {}!".format(self.name))

  def grow(self):
    self.age += 1

  def eat(self, amount):
    print("I'm a robot, I cannot eat {} food.".format(amount))

  def move(self, distance):
    print("Moved {}, I'm a robot with infinite energy.".format(distance))

  # Used mostly for debugging
  def __repr__(self):
    return "robot(name={}, age={})".format(self.name, self.age)

  # Commonly used to display the attributes of a specific object
  def __str__(self):
    return "My name is {} and I am {} years old.".format(self.name, self.age)

# If the name of the file is main, it means this is the running file,
# execute the test code
if (__name__ == "__main__"):
  beep = Robot("Beep")
  beep.display()

  Robot.the_laws()

  print(beep)