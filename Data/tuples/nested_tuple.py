# Add tuples within a list and then return it
def steps():
  likelihoods = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
  return likelihoods

# Create good and bad lists, if a tuple within steps() fits the bad
# criteria, add it to the bad list. Else, add to good.
def run():
  likelihood_list = steps()
  good = []
  bad = []
  
  for tuples in likelihood_list:
    if (tuples[1] >= 50): # Goes through the tuples inside the list and looks at position 1 within them (the numbers)
      bad.append(tuples)
    else:
      good.append(tuples)
  
  # Print the results
  print("Good steps: {}, Bad steps: {}\n".format(len(good), len(bad)))
  
  # Additional results to see what's in the lists
  print("Good steps: {}".format(good))
  print("Bad steps: {}".format(bad))

# Run the program
run()