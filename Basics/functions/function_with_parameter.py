# An escape function that takes 1 parameter, it will produce a different response depending on parameter input.
def escape_by(plan):
  if (plan.lower() == "jumping over"):
    print("We cannot escape that way! The boulder is too big!")
  elif (plan.lower() == "running around"):
    print("We cannot escape that way! The boulder is moving too fast!")
  elif (plan.lower() == "going deeper"):
    print("That might just work! Let's go deeper!")
  else:
    print("We cannot escape that way! The boulder is in the way!")

# Call the function with all possible parameters
escape_by("jumping over")
escape_by("RUNNING AROUND")
escape_by("Going Deeper")
escape_by("left")