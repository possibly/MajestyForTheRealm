from Card import Card
from Locations.Castle import Castle

class Queen(Card):
  def __init__(self):
    super(Queen, self).__init__([Castle], Castle)
