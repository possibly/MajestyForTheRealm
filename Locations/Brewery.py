from Location import Location

class Brewery(Location):

  def __init__(self, cards=[], side=Location.SIDE_A):
    super(Brewery, self).__init__(cards, side, 11, 12)

  def score(self, player):
    if self.side == Location.SIDE_A:
      return player.add_wealth(len(self.cards) * 2).add_meeples(len(self.cards))

  def score_other(self, player):
    if self.side == Location.SIDE_A:
      if len(self.Mill.cards) > 1:
        return player.add_wealth(2)
      return player
