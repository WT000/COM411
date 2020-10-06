# Firstly we need to ask the user to input the phrase
phrase = input("What phrase do you see?\n")
print("\nReversing...\n")

# Then, we create an empty string list
phrase_list=""

# Finally, the for loop looks at the inputted word(s) and adds each character it sees, though each new letter is pushed to the right (meaning h ends up at the back)
for character in phrase:
  phrase_list = character + phrase_list

# Output
print("The phrase is: {}".format(phrase_list)) 