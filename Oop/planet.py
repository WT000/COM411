# Import the human and robot classes
from human import Human
from robot import Robot

# Planet class which will hold the human and robot data
class Planet:
  def __init__(self):
    # Empty humans and robots lists which will hold the objects
    self.humans = []
    self.robots = []

  # Add human method which simply appends to the human list
  def add_human(self, human_to_add):
    self.humans.append(human_to_add)

  # Remove human method which checks if the human exists, removes if true
  def remove_human(self, human_to_remove):
    if (human_to_remove in self.humans):
      self.humans.remove(human_to_remove)
      print("Removed human {}".format(human_to_remove))
    else:
      print("The human doesn't exist")

  # The robot functions perform identically to the human methods, but with the
  # robot objects / robot list instead
  def add_robot(self, robot_to_add):
    self.robots.append(robot_to_add)

  def remove_robot(self, robot_to_remove):
    if (robot_to_remove in self.robots):
      self.robots.remove(robot_to_remove)
      print("Removed robot {}".format(robot_to_remove))
    else:
      print("The robot doesn't exist")

  def __repr__(self):
    return ""

  def __str__(self):
    return "Humans: {} \nRobots: {}".format(self.humans, self.robots)

if (__name__ == "__main__"):
  homeworld = Planet()

  human1 = Human("Will")
  human2 = Human("John")

  homeworld.add_human(human1)
  homeworld.add_human(human2)
  homeworld.remove_human(human1)

  print(homeworld)

  robot1 = Robot("Beep")
  robot2 = Robot("Bop")

  homeworld.add_robot(robot1)
  homeworld.add_robot(robot2)
  homeworld.remove_robot(robot2)

  print(homeworld)