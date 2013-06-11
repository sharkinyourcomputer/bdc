"""Interactive loop."""

import sys
import dungeon

      
def RunTheDungeon():
  # Our dungeon only has one room, and that room has no doors.
  square_room = dungeon.Room(
      'A square room. You can\'t sleep here.');

  church = dungeon.Room(
  
  outside = dungeon.Room(
      'You\'re outside. There are people here waiting, surrounding you.')

  round_room = dungeon.Room(
      'A round room. There is a bed in the corner, and a spiral set of stairs.',
      {'stairs': outside},
      {'sleep': 

  square_room.doors['']

  RunInteractiveLoop(round_room)


def RunInteractiveLoop(room):
  """Takes commands from the user and tries to execute them."""

  while True:  # This loop only exits if we explicitly break.
    # Print a prompt to sys.stdout (the "standard output").
    sys.stdout.write('MUD> ')
    # Allow the user to enter a command.
    user_input = sys.stdin.readline()
    # Split the user's input into words (separated by the ' ' string). We use
    # all but the last character of user_input (i.e. user_input[:-1]), since the
    # last character is the '\n' (i.e. the user hit enter).
    user_words = user_input[:-1].split(' ')

    if user_words[0] == 'exit':
      sys.stdout.write('Goodbye!')
      break

    if user_words[0] == 'look':
      sys.stdout.write(room.description + '\n')

    if user_words[0] == 'go':
      if user_words[1] not in room.doors:
        sys.stdout.write('You can\'t go %s.\n' % user_words[1])
      else:
        sys.stdout.write('You go %s.\n' % user_words[1])
        room = room.doors[user_words[1]]

    if user_words[0] in room.commands:
      room = room.commands[user_words[0]](*user_words[1:])


# The Python interpreter defines __name__ in every module in the program, but
# defines it to '__main__' in only one. E.g. if you $ python abacura/iloop.py,
# then this file will be '__main__'.
if __name__ == '__main__':
  RunTheDungeon()
