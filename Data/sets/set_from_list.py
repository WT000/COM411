#user_web_browsers = ["Chrome", "Firefox", "Chrome", "Firefox", "Edge", "Firefox"]
#unique_web_browsers = set(user_web_browsers)
#print(unique_web_browsers)
#unique_web_browsers.add(("Opera", 2))
#print(unique_web_browsers)
#unique_web_browsers.remove("Edge")
#print(unique_web_browsers)

def observed():
  observations = []
  for count in range(4):
    observation = input("Please enter an observation:\n")
    observations.append(observation)

  return observations

def run():
  print("Counting observations...")
  observation_list = observed()

  observation_set = set()

  for observation in observation_list:
    observation_set.add((observation, observation_list.count(observation)))
    
  print(observation_set)

run()