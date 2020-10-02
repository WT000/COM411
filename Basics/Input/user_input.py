# Ask the user what their name is
name = input("What is your name, human?\n")

# Print the response
print("It's nice to meet you human,", name + "!")

################
print("\nOr, we could also do... \n")

print("It's nice to meet you, {}!".format(name))

# The users input is stored in memory, "name" itself is stored in memory using binary, by being called "name" it makes it easier for us to remember.
# Using a + is concatenation. Using , is specific to python, using + is in almost every language.