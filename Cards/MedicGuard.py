from Card import Card
from Locations.Cottage import Cottage
from Locations.Guardhouse import Guardhouse

class MedicGuard(Card):
  def __init__(self):
    super(MedicGuard, self).__init__([Cottage, Guardhouse])
