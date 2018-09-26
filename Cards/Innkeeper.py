from Card import Card
from Locations.Inn import Inn

class Innkeeper(Card):
  def __init__(self):
    super(Innkeeper, self).__init__([Inn], Inn)
