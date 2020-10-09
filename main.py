# This is going to be used as a command index, allowing me to refer to it if I get confused.

# 1 - Basics
print("Hello!")
print("\n\tFancy Hello with a new line and tab!\n")

greeting = "\"Hello\""
greeting2 = "Hello2"
print(greeting)

print("{} is greeting, {} is greeting 2.".format(greeting, greeting2))

greeting3 = float(input("Enter some numbers here, include some decimal places since this is a float!\n"))
print(str(greeting3))
# without string also works
# to limit deciman places
print("{:.2f}".format(greeting3))

greeting4 = int(input("Enter a whole number\n"))
greeting5 = greeting4 * (1+1)

print(greeting5)
print("*" * greeting5)

# 2 - Decisions and Loops
# remember that a variable within a function is local, it needs to be defined and then returned inside itself
decision1 = int(input("Please enter the number 1.\n"))
if (decision1 == 1):
  print("Thank you :)")
else:
  decision1_wrong = int(input("Seriously?! Try to enter it again:\n"))
  if (decision1_wrong > 15):
    print("That's way too big!")
  elif (decision1_wrong > 10):
    print("That's too big!")
  elif (decision1_wrong > 5):
    print("That's big!")
  else:
    print("Why.")

decision2 = input("Now, enter \"two\" (not the number).\n")
if ((decision1 == 1) and (decision2.lower() == "two")):
  print("You did everything correctly!")
else:
  print("Somethings wrong.")

# while loop control variable and final sum
count = 0
final_sum = 0

while (count < 100):
  count += 1
  final_sum += count
print("The total sum of that is {}".format(final_sum))

factorial = int(input("Enter a number:\n"))

# control variable
loop_multiply = 0
final_factorial = 1

while (loop_multiply < factorial):
  loop_multiply += 1
  final_factorial *= loop_multiply
print(final_factorial)