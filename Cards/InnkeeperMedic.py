from Card import Card
from Locations.Inn import Inn
from Locations.Cottage import Cottage

class InnkeeperMedic(Card):
  def __init__(self):
    super(InnkeeperMedic, self).__init__([Inn, Cottage])
