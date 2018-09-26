from Card import Card
from Locations.Cottage import Cottage
from Locations.Brewery import Brewery

class MedicBrewer(Card):
  def __init__(self):
    super(MedicBrewer, self).__init__([Cottage, Brewery])
