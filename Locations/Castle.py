from Location import Location

class Castle(Location):

  def __init__(self, cards=[], side=Location.SIDE_A):
    super(Castle, self).__init__(cards, side, 16, 16)

  def score(self, player):
    if self.side == Location.SIDE_A:
      return player.add_wealth(len(self.cards) * 5).add_meeples(len(self.cards))

  def score_other(self, player):
    if self.side == Location.SIDE_A:
      return player
