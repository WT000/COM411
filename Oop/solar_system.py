# Import dictplanet for the planets and random for random number
# gen
from dictplanet import Planet
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
        count.inhabitants["humans"].append("Human-{}".format(person))

      for robot in range(randint(0, 5)):
        count.inhabitants["robots"].append("Robot-{}".format(robot))
      
      # Append the finished planet to the planets in the solar system
      self.planets.append(count)

  # The display method prints the __str__ representation of each
  # planet
  def display(self):
    for planet in self.planets:
      print(planet)
      print()

# Visulaise function which will visualise the planets in a solar 
# system, to do this it creates axes with a
  def visualise(self):
    fig, axes = plt.subplots(1, len(self.planets), sharey="all")
    
    for planet in range(len(self.planets)):
      axes[planet].bar(1, len(self.planets[planet].inhabitants["humans"]), color="b")
      axes[planet].bar(2, len(self.planets[planet].inhabitants["robots"]), color="r")

      axes[planet].set_xticks([1, 2])
      axes[planet].set_xticklabels(["Humans", "Robots"])
      axes[planet].set_title("Planet-{}".format(planet+1))

    plt.tight_layout()
    plt.show()

  def __repr__(self):
    return "solar_system=(planets={})".format(self.planets)

  def __str__(self):
    return "The planets in this solar system are: {}".format(self.planets)
  
sol = Solar_System()

sol.generate()
sol.visualise()