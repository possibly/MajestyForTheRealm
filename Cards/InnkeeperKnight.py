from Card import Card
from Locations.Inn import Inn
from Locations.Barracks import Barracks

class InnkeeperKnight(Card):
  def __init__(self):
    super(InnkeeperKnight, self).__init__([Inn, Barracks])
