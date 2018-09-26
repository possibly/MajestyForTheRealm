from Card import Card
from Locations.Brewery import Brewery

class Brewer(Card):
  def __init__(self):
    super(Brewer, self).__init__([Brewery], Brewery)
