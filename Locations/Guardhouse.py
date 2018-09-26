from Location import Location

class Guardhouse(Location):

  def __init__(self, cards=[], side=Location.SIDE_A):
    super(Guardhouse, self).__init__(cards, side, 13, 8)

  def score(self, player):
    if self.side == Location.SIDE_A:
      wealth = len(self.cards) + len(player.realm.Barracks.cards) + len(player.realm.Inn.cards)
      return player.add_wealth(wealth * 2)

  def score_other(self, player):
    if self.side == Location.SIDE_A:
      return player