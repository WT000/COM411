# Import the human and robot classes
from human import Human
from robot import Robot

# Planet class which will hold the human and robot data
class Planet:
  def __init__(self, planet_name=None):
    self.planet = planet_name
    # Empty humans and robots list which will hold the human AND robot objects
    self.inhabitants = []

  # Add inhabitant method which appends the inhabitant to the inhabitants list
  def add_inhabitant(self, inhabitant_to_add):
    self.inhabitants.append(inhabitant_to_add)

  # Remove inhabitant method which checks if the inhabitant exists, removes if true
  def remove_inhabitant(self, inhabitant_to_remove):
    if (inhabitant_to_remove in self.inhabitants):
      self.inhabitants.remove(inhabitant_to_remove)
      print("Removed inhabitant {}".format(inhabitant_to_remove))
    else:
      print("The inhabitant doesn't exist")

  def count_inhabitants(self):
    total_humans, total_robots = 0, 0
    
    for inhabitant in self.inhabitants:
      if isinstance(inhabitant, Human):
        total_humans += 1
      elif isinstance(inhabitant, Robot):
        total_robots += 1
    
    return total_humans, total_robots

  def __repr__(self):
    return "{}=(inhabitants={})".format(self.planet, self.inhabitants)
  
  def __str__(self):
    return "### {} ### \nInhabitants: {}".format(self.planet, self.inhabitants)

if (__name__ == "__main__"):
  homeworld = Planet("Earth")

  human1 = Human("Will")
  human2 = Human("John")

  homeworld.add_inhabitant(human1)
  homeworld.add_inhabitant(human2)
  homeworld.remove_inhabitant(human1)

  print(homeworld)

  robot1 = Robot("Beep")
  robot2 = Robot("Bop")

  homeworld.add_inhabitant(robot1)
  homeworld.add_inhabitant(robot2)

  print(homeworld)
  print(homeworld.count_inhabitants())