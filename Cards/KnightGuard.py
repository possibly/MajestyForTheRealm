from Card import Card
from Locations.Guardhouse import Guardhouse
from Locations.Barracks import Barracks

class KnightGuard(Card):
  def __init__(self):
    super(KnightGuard, self).__init__([Guardhouse, Barracks])
