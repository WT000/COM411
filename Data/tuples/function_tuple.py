# Likelihood function which creates a tuple and returns the min and
# max values
def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return (min(likelihoods), max(likelihoods))

# Run function which prints t
def run():
  acquired = likelihood()
  print("Minimum likelihood of falling: {}% \nMaximum likelihood of falling: {}%".format(acquired[0], acquired[1]))

run()