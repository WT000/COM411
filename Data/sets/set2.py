def observed():
    observations = []
    print("Counting observations...")
    
    for count in range(5):
        observation = input("Please enter an observation:")
        observations.append(observation)
        
    return observations
    
def remove_observations(observation_list):
    while True:
        print(observation_list)
        choice = input("Do you wish to remove an observation from the list (yes / no)?")
        if (choice.lower() == "yes"):
            to_remove = input("What observation do you wish to remove?\n")
            if (to_remove in observation_list):
                observation_list.remove(to_remove)
                print("Done!")
            else:
                print("Observation not in the list.")
        elif (choice.lower() == "no"):
            return observation_list
        elif (len(observation_list) == 0):
            return False
        else:
            print("Please enter yes or no.")
            
def run():
    observation_list = observed()
    remove_observations(observation_list)
    observation_set = set()
    
    print("Observations:")
    
    for observation in observation_list:
        observation_set.add((observation, observation_list.count(observation)))
    
    for data in sorted(observation_set):
        print("{} observed {} times".format(data[0], data[1]))
        
run()