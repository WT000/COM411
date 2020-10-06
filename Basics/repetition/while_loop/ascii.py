# Ask the user how many bars need to be charged
bars_to_charge = int(input("How many bars should be charged?\n"))

# Counter
charged_bars = 0

# Loops until charged_bars is equal to what the user inputted
while (charged_bars < bars_to_charge):
  charged_bars += 1
  print("Charging: " + "█" * charged_bars)

# Loop complete
print("The battery is fully charged.")