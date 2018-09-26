from Card import Card
from Locations.Cottage import Cottage

class Medic(Card):
  def __init__(self):
    super(Medic, self).__init__([Cottage], Cottage)
