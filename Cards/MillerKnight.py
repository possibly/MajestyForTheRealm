from Card import Card
from Locations.Mill import Mill
from Locations.Barracks import Barracks

class MillerKnight(Card):
  def __init__(self):
    super(MillerKnight, self).__init__([Mill, Barracks])
