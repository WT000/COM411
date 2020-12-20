# Advent of code program 1! The program looks at each individual
# number (i) and then compares this number to every other number (n)
# in the list until it reaches one that sums with i to make 2020,
# i and n are then multipled 

# (2021 to include 2020 + 0)
numbers = [i for i in range(2021)]

for i in numbers:
  for n in numbers:
    if (i + n) == 2020:
      result = i * n
      print("{} + {}: CALC: {}".format(i, n, result))