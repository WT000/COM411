# A function that adds the weights together and returns it
def sum_weights(beep_weight, bop_weight):
  total_weight = beep_weight + bop_weight
  return total_weight

# A function that calls the sum function, divides it by 2 and returns
def calc_avg_weight(beep_weight, bop_weight):
  avg_weight = sum_weights(beep_weight, bop_weight) / 2
  return avg_weight

# A function that asks the user for the weights of the robots and then asks what they want to do with it
def run():
  beep_weight = float(input("What is the weight of Beep?\n"))
  bop_weight = float(input("What is the weight of Bop?\n"))

  user_decision = input("What would you like to calculate (sum or average)\n")

  if (user_decision.lower() == "sum"):
    print(sum_weights(beep_weight, bop_weight))
  elif (user_decision.lower() == "average"):
    print(calc_avg_weight(beep_weight, bop_weight))
  else:
    print("ERROR: Please enter the word \"sum\" or \"average\"")

# Run the program
run()