from Location import Location
from Infirmary import Infirmary

class Cottage(Location):

  def __init__(self, workers=[], side=Location.SIDE_A):
    super(Cottage, self).__init__(workers, side, 12, 12)

  def score(self, player):
    if self.side == Location.SIDE_A:
      return player._heal().add_wealth(len(self.cards) * 3)

  def score_other(self, player):
    return player
