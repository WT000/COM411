from dictplanet import Planet
import random

class Universe:
  def __init__(self):
    self.planets = []

  def generate(self, amount):
    for count in range(amount):
      # create planet object
      count = Planet(count)
      # add a random number of humans and robots
      # add the planet to the planets list

      # get the len of the planet directly from humans
      # use a for loop with count / index numbers to generate the names for humans / robots

      # use a loop to count the len of planets in the universe, then use this for plotting