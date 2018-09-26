from Location import Location

class Barracks(Location):

  def __init__(self, cards=[], side=Location.SIDE_A):
  	super(Barracks, self).__init__(cards, side, 14, 8)

  def score(self, player):
    if self.side == Location.SIDE_A:
      return player.add_wealth(len(player.realm.Barracks.cards) * 3)

  def score_other(self, player):
    if self.side == Location.SIDE_A:
      return player._attacked(self.cards)