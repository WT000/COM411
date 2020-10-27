# The observed function will take no parameters and ask the user to enter an
# observation 5 times
def observed():
  observations = []

  for count in range(5):
    observation = input("Please enter an observation:\n")
    observations.append(observation)

  return observations

# The remove observations function will take the observation list as a parameter
# and will infinitely ask the user to remove observations (unless it needs to
# stop)
def remove_observations(observation_list):
  while True:
    choice = input("Do you want to remove an observation (yes/no)?\n")

    if (choice.lower() == "yes"):
      observation_to_remove = input("Which observation do you wish to remove?\n")

      if (observation_to_remove in observation_list):
        observation_list.remove(observation_to_remove)
        print("Done!")
      elif (len(observation_list == 0)):
        print("There's nothing to remove.")
        return observation_list
      else:
        print("{} does not exist.".format(observation_to_remove))

    else:
      return observation_list

# The run function will call the observation list function and then put the returned
# value into the remove observation function, it will then put the returned
# values into a sorted list
def run():
  observation_list = observed()
  remove_observations(observation_list)

  observation_set = set()

  for observation in observation_list:
    observation_set.add((observation, observation_list.count(observation)))

  print("Observations:")
  for value, total in sorted(observation_set): 
    # (observation_set, inverse=True) would make it go from bottom to top
    print("{} observed {} times".format(value, total))

# Run the program
run()