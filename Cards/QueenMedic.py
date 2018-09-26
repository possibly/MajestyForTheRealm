from Card import Card
from Locations.Castle import Castle
from Locations.Cottage import Cottage

class QueenMedic(Card):
  def __init__(self):
    super(QueenMedic, self).__init__([Castle, Cottage])
