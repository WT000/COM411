# Ask the user to input a number
user_number = int(input("Please enter a number: "))

# Control variable, factorial_total is 1 as multiplying by 0 would always result IN 0
loop = 0
factorial_total = 1

# On each loop the value increases by 1 and then the factorial is multiplied by that amount until it reaches the number inputted by the user
while (loop < user_number):
  loop += 1
  factorial_total *= loop

# End result
print("The factorial is {}".format(factorial_total))