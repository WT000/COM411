from inhabitant import Inhabitant

class Robot(Inhabitant):
  LAWS = "Protect, Obey, Survive"
  
  def __init__(self, name="Robot", age=0):
    super().__init__()
    self.name = name
    self.age = age

  def the_laws(self):
    print(Robot.LAWS)

  def __str__(self):
    return "Greetings. I am a robot named {}. I have existed for {} years. My energy {}.".format(self.name, self.age, self.energy)

  def __repr__(self):
    return "robot=(name={}, age={}, energy={})".format(self.name, self.age, self.energy)

if (__name__ == "__main__"):
  test = Robot("Beep", 3)
  print(test)
  test.move(50)
  test.eat(50)
  test.eat(1)