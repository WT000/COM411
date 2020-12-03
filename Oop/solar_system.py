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
    for count in range(randint(1, 5)):
      # Create a planet object
      count = Planet("Planet-{}".format(count))

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

  def visualise(self):
    fig, axes = plt.subplots(1, len(self.planets), sharex="all", sharey="all")
    
    for planet in range(len(self.planets)):
      axes[planet].bar(1, len(self.planets[planet].inhabitants["humans"]))
      axes[planet].bar(2, len(self.planets[planet].inhabitants["robots"]))

    fig, axes = plt.subplots(len(self.planets), 1)
    plt.show()

  def __repr__(self):
    return "solar_system=(planets={})".format(self.planets)

  def __str__(self):
    return "The planets in this solar system are: {}".format(self.planets)
  
sol = Solar_System()

sol.generate()
sol.visualise()