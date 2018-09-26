from Card import Card
from Locations.Mill import Mill

class Miller(Card):
  def __init__(self):
    super(Miller, self).__init__([Mill])
