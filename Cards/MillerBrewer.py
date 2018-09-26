from Card import Card
from Locations.Mill import Mill
from Locations.Brewery import Brewery

class MillerBrewer(Card):
  def __init__(self):
    super(MillerBrewer, self).__init__([Mill, Brewery])
