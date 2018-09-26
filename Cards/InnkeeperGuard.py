from Card import Card
from Locations.Inn import Inn
from Locations.Guardhouse import Guardhouse

class InnkeeperGuard(Card):
  def __init__(self):
    super(InnkeeperGuard, self).__init__([Inn, Guardhouse])
