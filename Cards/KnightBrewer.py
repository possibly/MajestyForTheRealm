from Card import Card
from Locations.Brewery import Brewery
from Locations.Barracks import Barracks

class KnightBrewer(Card):
  def __init__(self):
    super(KnightBrewer, self).__init__([Brewery, Barracks])
