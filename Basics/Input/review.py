# Ask the user for their name and species, make the AI seem interested, it should look different than where the user inputs text
name = input("\t\tWhat is your name?\n")
species = input("\t\tI see... \"{}\" is an interesting name. What species are you?\n".format(name))
age = int(input("\t\tSo... You are \"{}\" of the \"{}\" species... How many earth-years have you existed for?\n".format(name, species)))

# Do some interesting ASCII math with the inputs of the user
print("\t\tSo, you've existed for {} earth-years? How interesting, that's {} diamonds!\n\t\t".format(str(age), str(age)) + "♦️" * age + "\n\t\tSee? Did you find that cool?")
choice = input()
print("\t\t\"{}\" is what you said... Sadly, I have absolutely no idea how to make decisions. But, I can turn the amount of characters you inputted into diamonds!\n\t\t".format(choice) + "♦️" * len(choice) + "\n\t\tSee, that was cool, right?")

# Do another calculation but with the sum of all the characters inputted by the user
second_choice = input()
print("\t\tYou realise I still can't read that, right? Here, have your input turned into diamonds and to the power of two.\n\t\t" + "♦️" * len(second_choice)**2 + "\n\t\tIt's been fun, but I'm afraid my battery is about to run out, \"{}\" of the \"{}\" species. Will you enjoy your organic life without me?".format(name, species))
third_choice = input()

# Do a final calculation with the diamonds, the AI will hopefully make the user laugh
final_diamonds = (len(name) + len(species) + len(str(age)) + len(choice) + len(second_choice) + len(third_choice)) * 2
print("\t\t...I STILL can't read that. But here, have all your inputted characters doubled and turned into diamonds!\n\t\t" + "♦️" * final_diamonds)