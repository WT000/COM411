# Import human, robot and planet classes for creating the
# planets and inhabitants
from human import Human
from robot import Robot
from planet import Planet

# Import random for random numbers and matplotlib for
# plotting
from random import randint
import matplotlib.pyplot as plt

# The solar system class immediately creates a list of planets when
# called
class Solar_System:
  def __init__(self):
    self.planets = []

  # The generate method takes no parameters, it will create a
  # random amount of planets and append a random amount of humans
  # and robots to each planet
  def generate(self):
    for count in range(randint(1, 4)):
      # Create a planet object
      count = Planet("Planet-{}".format(count+1))

      # Add a random amount of people and robots to the planet
      for person in range(randint(0, 5)):
        name = "Human-{}".format(person)
        age = randint(0, 120)
        count.inhabitants.append(Human(name, age))

      for robot in range(randint(0, 5)):
        name = "Robot-{}".format(robot)
        age = randint(0, 120)
        count.inhabitants.append(Robot(name, age))
      
      # Append the finished planet to the planets in the solar system
      self.planets.append(count)

  # The display method prints the __str__ representation of each
  # planet
  def display(self):
    for planet in self.planets:
      print(planet)
      print()

# Visulaise function which will visualise the planets in a solar 
# system, to do this it firstly creates an amount of axes equal to how
# many planets there are, it then loops through the list of planets and
# plots their data onto the appropriate planet bar chart. Humans are blue,
# robots are red.
  def visualise(self):
    fig, axes = plt.subplots(1, len(self.planets), sharey="all")
    
    for planet in range(len(self.planets)):
      data = self.planets[planet].count_inhabitants()

      axes[planet].bar(1, data[0], color="b")

      axes[planet].bar(2, data[1], color="r")

      axes[planet].set_xticks([1, 2])
      axes[planet].set_xticklabels(["Humans", "Robots"])
      axes[planet].set_title("Planet-{}".format(planet+1))

    plt.tight_layout()
    plt.show()

  def __repr__(self):
    return "solar_system=(planets={})".format(self.planets)

  def __str__(self):
    return "The planets in this solar system are: {}".format(self.planets)

if (__name__ == "__main__"):
  sol = Solar_System()

  sol.generate()
  sol.visualise()