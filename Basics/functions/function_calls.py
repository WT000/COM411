# Print the given word in an ASCII box
def ascii_box(word):
  length = 2 + len(word)
  print("*" * length)
  print("*" + word + "*")
  print("*" * length)

# Make the given word lowercase
def lower_case(word):
  print(word.lower())

# Make the given word uppercase
def upper_case(word):
  print(word.upper())

# Mirror the given word
def mirrored(word):
  reverse = word[::-1]
  print(reverse)
  #which means go through the entire word from the back

  #for character in range(len(word)-1, -1, -1):
   #print(word[character], end="")

  #for letter in reversed(word):
  # reverse_word += letter

# Repeat the given word between upper and lowercase
def repeat(count, word):
  for i in range(count):
    if (i % 2 == 0):
      print(word.upper())
    else:
      print(word.lower())

# Ask the user to input a word and let them decide what they're going to do with it
def run():
  infinite_loop = True
  while (infinite_loop == True):
    word = input("Enter a word, any word!\n")
    if (word.isdigit()):
      print("That's a number!")
    else:
      break

  decision = int(input("""Now, what do you want to do with the word?\n
  1 - ASCII Box
  2 - Make it lowercase
  3 - Make it uppercase
  4 - Mirror the word
  5 - Repeat the word in lowercase and uppercase\n\n"""))
  
  if (decision == 1):
    ascii_box(word)
  elif (decision == 2):
    lower_case(word)
  elif (decision == 3):
    upper_case(word)
  elif (decision == 4):
    mirrored(word)
  elif (decision == 5):
    count = int(input("How many times do you want it to be printed?\n")) # Ask for the amount of times the word will be looped
    repeat(count, word)
  else:
    print("ERROR: Please enter a number between 1 and 5.")

run()