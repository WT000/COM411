# Ask the user for their name, age, height and weight.
name = input("What is your name, human?\n")

age = int(input("How old are you (in years)?\n"))

height = float(input("How tall are you (in meters)?\n"))

weight = int(input("How much do you weigh (in kilograms)?\n"))

# Calculation
bmi = weight/(height**2)

print("{} you are {} years old and your BMI is {:.2f}".format(name, age, bmi))

# Explicit is int, we're specifically saying that the data must be a number. it KNOWS it's a number.

# Implicit is the bmi calculation, we can only do math with int but it already knew they were numbers. It WORKS it out.