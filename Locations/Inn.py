from Location import Location
from Brewery import Brewery
from copy import deepcopy

class Inn(Location):

  def __init__(self, cards=[], side=Location.SIDE_A):
    super(Inn, self).__init__(cards, side, 15, 12)

  def _get_brewers(self, p):
    return len(p.locations[Brewery].cards)

  def _score_brewers(self, p):
    if _get_brewers > 0:
      return p.wealth + 3
    else:
      return 0

  def score(self, player):
    if self.side == Location.SIDE_A:
      wealth = (len(self.cards) * 4) + (self._score_brewers(player))
      return player.add_wealth(wealth)

  def score_other(self, player):
    if self.side == Location.SIDE_A:
      return player.add_wealth(self._score_brewers(player))
