class Card(object):

  def __repr__(self):
    return str(type(self).__name__) + ' ' + str(id(self))
