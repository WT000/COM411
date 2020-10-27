# Short pattern function containing a dict which is returned
def short_pattern():
  pattern = {
           "sequence":"101",
           "occurrences":5}
  return pattern

# Medium pattern function containing a dict which is returned
def medium_pattern():
  pattern = {
           "sequence":"111000",
           "occurrences":25}
  return pattern

# Long pattern function containing a dict which is returned
def long_pattern():
  pattern = {
           "sequence":"1100110011001100",
           "occurrences":50}
  return pattern

# Run function which nests the other dicts into the all_patterns
# dict and print the result
def run():
  print("Analysing patterns...")
  all_patterns = {
           "short sequence":short_pattern(),
           "medium sequence":medium_pattern(),
           "long sequence":long_pattern()}
  print(all_patterns)

# Run the program 
run()