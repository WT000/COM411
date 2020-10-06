# Ask the user what type of book the user has (soft or hard).
book_cover = input("What type of cover does the book have?\n")

# Ask if it's soft or hard, otherwise give a generic response
if (book_cover == "soft"):
  # Ask if the book is perfect bound or not
  perfect_bound = input("Is the book perfect bound?\n")
  if (perfect_bound == "yes"):
    print("Soft cover, perfect bound books are very popular!")
  else:
    print("Soft covers with coils or stiches are great for short books")

elif (book_cover == "hard"):
  print("Books with hard covers can be more expensive!")
else:
  print("That's cool!")