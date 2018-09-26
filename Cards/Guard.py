from Card import Card
from Locations.Guardhouse import Guardhouse

class Guard(Card):
  def __init__(self):
    super(Guard, self).__init__([Guardhouse], Guardhouse)
