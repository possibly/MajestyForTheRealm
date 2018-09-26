from Card import Card
from Locations.Castle import Castle
from Locations.Guardhouse import Guardhouse

class QueenGuard(Card):
  def __init__(self):
    super(QueenGuard, self).__init__([Castle, Guardhouse])
