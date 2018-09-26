class Card(object):
  def __init__(self, possibles=[], choice=None):
    self.possible_locations = possibles # Refers to an array of classes, not an array of instances.
    self.chosen_location = choice # Refers to a class, not an instance.

  def __repr__(self):
    return str(type(self).__name__) + ' ' + str(id(self))

  def is_decided(self):
    if self.chosen_location != None:
      return True
    else:
      return False
