from Location import Location

class Mill(Location):

  def __init__(self, cards=[], side=Location.SIDE_A):
    super(Mill, self).__init__(cards, side, 10, 14)

  def score(self, player):
    if self.side == Location.SIDE_A:
      return player.add_wealth(len(self.cards) * 2)

  def score_other(self, player):
    if self.side == Location.SIDE_A:
      return player
