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

      # perhaps make planet return a tuple with the no of robots and humans, these can then be directly used for x and y