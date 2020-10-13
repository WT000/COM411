import Basics.Output.simple_message as simple_message
import Basics.Output.multiline_message as multiline_message
import Basics.Output.ascii_art as ascii_art
import Basics.Output.escape_characters as escape_characters

def run_block_a():
  response = input("Which program in 'Block A: Basics' do you wish to run?\n")
  if (response.lower() == "simple message"):
    simple_message.run()
  elif (response.lower() == "multiline message"):
    multiline_message.run()
  elif (response.lower() == "ascii art"):
    ascii_art.run()
  elif (response.lower() == "escape characters"):
    escape_characters.run()

def run():
  is_running = True
  while (is_running):
    response = input("What would you like to do?\n[a] Run 'Block A: Basics' programs\n[q] Quit\n")
    if (response.lower() == "a"):
      run_block_a()
    elif (response.lower() == "q"):
      break
    else:
      print("ERORR: Invalid option.")

run()

#simple_message.run()
#multiline_message.run()
#ascii_art.run()
#escape_characters.run()