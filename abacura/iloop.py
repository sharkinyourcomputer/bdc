"""Interactive loop."""

import sys
import dungeon

      
def RunTheDungeon():
  # Our dungeon only has one room, and that room has no doors.
  square_room = dungeon.Room()
  
  round_room = dungeon.Room()
  
  outside = dungeon.Room('You are outside now. Is that a rumbling in your bowels? An open window leads to the square room. Stairs lead to the round room',
  {'window': square_room, 'stairs': round_room},
  {'poop': GoPoop})

  square_room.description = 'A square room. You can\'t sleep here. There is an open window.'
  square_room.doors['window'] = outside
  
      
  round_room.description = 'A round room. There\'s a bed in the corner, and stairs outside.'
  round_room.doors['stairs'] = outside
  round_room.commands['sleep'] = SleepyTime

  RunInteractiveLoop(square_room)

def GoPoop(room):
  sys.stdout.write('You squat down and squeeze out a brown log.\n')
  return room

def SleepyTime(room):
  sys.stdout.write('You curl up in the bed and close your eyes... right as you begin to drift off to sleep you take a deep breath of air... oh my god! someone pooped in the bed!!! \n')
  room.description += ' Within the ruffled sheets of the bed you think you spot a small brown nugget of poo-poo.'
  return room

def RunInteractiveLoop(room):
  """Takes commands from the user and tries to execute them."""

  sys.stdout.write(room.description + '\n')

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
      if len(user_words) == 1:
        sys.stdout.write('Go where, you idiot?\n')
      elif user_words[1] not in room.doors:
        sys.stdout.write('You can\'t go %s.\n' % user_words[1])
      else:
        sys.stdout.write('You go %s.\n' % user_words[1])
        room = room.doors[user_words[1]]
        sys.stdout.write(room.description + '\n')

    if user_words[0] in room.commands:
      room = room.commands[user_words[0]](room, *user_words[1:])


# The Python interpreter defines __name__ in every module in the program, but
# defines it to '__main__' in only one. E.g. if you $ python abacura/iloop.py,
# then this file will be '__main__'.
if __name__ == '__main__':
  RunTheDungeon()
