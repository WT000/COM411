#user_web_browsers = ["Chrome", "Firefox", "Chrome", "Firefox", "Edge", "Firefox"]
#unique_web_browsers = set(user_web_browsers)
#print(unique_web_browsers)
#unique_web_browsers.add(("Opera", 2))
#print(unique_web_browsers)
#unique_web_browsers.remove("Edge")
#print(unique_web_browsers)

# Observed function which takes no parameters, it should create
# a list and ask the user to input 4 observations
def observed():
  observations = []
  for count in range(4):
    observation = input("Please enter an observation:\n")
    observations.append(observation)

  return observations


# The run function will take no parameters and will display how many
# times each observation appeared
def run():
  print("Counting observations...")
  observation_list = observed()

  #observation_filter = set(observation_list)
  observation_set = set()

  #for observation in observation_filter:
    #observation_set.add((observation, observation_list.count(observation)))
  
  for observation in observation_list:
    observation_set.add((observation, observation_list.count(observation)))
    
  print(observation_set)

  for value, total in observation_set:
    print("{} observed {} times.".format(value, total))

run()