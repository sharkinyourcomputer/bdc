"""Classes for constructing dungeons."""


class Room(object):
  """A simple class for rooms in the dungeon.

  Say 'room' to yourself enough times and it ceases to be an English word.
  """
  # The constructor (in Python, must be named __init__) is executed when you
  # instantiate the class, e.g. by executing r = Room('A round room.').
  def __init__(self, description=None, doors=None, commands=None, contents=None):
    """Constructs a room with a string description and links to other rooms.

    The rooms parameter should be a dict mapping direction strings (e.g. east)
    too other instances of the Room class.
    """
    self.description = description 
    self.doors = doors or { }
    self.commands = commands or { }
    self.contents = contents or { }

class Item(object):
  def __int__(self, name=None, description=None):
    
    self.name = name
    self.description = description

class Dungeon(object):
  """A set of interconnected Rooms, containing Players and Items."""

  def __init__(self):
    self.rooms = []

  def AddRoom(room):
    self.rooms.apped(room)
