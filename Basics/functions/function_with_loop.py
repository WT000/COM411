# The program has a cross bridge parameter taking the steps of user
# instead of range(0, steps, 1), we can just do range(steps)
def cross_bridge(steps):
  for distance in range(0, steps, 1):
    print("Crossed Step.")
  if (steps > 5):
    print("The bridge is collapsing!")
  else:
    print("We must keep going!")

# Call the function
cross_bridge(3)
cross_bridge(6)