from Card import Card
from Locations.Barracks import Barracks

class Knight(Card):
  def __init__(self):
    super(Knight, self).__init__([Barracks], Barracks)
