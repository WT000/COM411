# Ask the user for the brightness value
bot_brightness = int(input("What level of brightness is required?"))
print("\nAdjusting brightness...\n")

# Print Beep's and Bop's brightness level in increments of 2
for level in range(0, bot_brightness+2, 2):
  print("Beep's brightness level: " + "*" * level)
  print("Bop's brightness level: " + "*" * level)
  print()

# Loop completed
print("Adjustments complete!")