# The program has a cross bridge parameter taking the steps of user
def cross_bridge(steps):
  for distance in range(0, steps, 1):
    print("Crossed Step.")
  if (steps > 5):
    print("The bridge is collapsing!")
  else:
    print("We must keep going!")

cross_bridge(3)
cross_bridge(6)