from Card import Card
from Locations.Inn import Inn
from Locations.Castle import Castle

class InnkeeperQueen(Card):
  def __init__(self):
    super(InnkeeperQueen, self).__init__([Inn, Castle])
