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